#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Verify the prepared vendor payloads against their recorded sizes and hashes."""

import hashlib
import json
from pathlib import Path
import sys


def main():
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'docs/payload-sha256.json').read_text())
    if manifest['algorithm'] != 'sha256':
        raise ValueError('Unsupported hash algorithm')
    scopes = ('proprietary', 'boot', 'firmware', 'configs', 'Xpan')
    expected = manifest['files']
    actual = {str(path.relative_to(root)) for name in scopes
              for path in (root / name).rglob('*') if path.is_file()}
    if set(expected) != actual:
        missing = sorted(set(expected) - actual)
        extra = sorted(actual - set(expected))
        raise ValueError(f'Payload inventory differs: missing={missing}, extra={extra}')
    failures = []
    for name, entry in sorted(expected.items()):
        path = root / name
        if not path.resolve().is_relative_to(root):
            raise ValueError('Payload path escapes repository: ' + name)
        if path.stat().st_size != entry['bytes']:
            failures.append(name + ': size mismatch; retrieve Git LFS objects if needed')
            continue
        with path.open('rb') as stream:
            digest = hashlib.file_digest(stream, 'sha256').hexdigest()
        if digest != entry['sha256']:
            failures.append(name + ': SHA-256 mismatch')
    if failures:
        raise ValueError('\n'.join(failures))
    print(f'PASS: {len(expected)} vendor payload sizes and SHA-256 hashes')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, KeyError) as error:
        sys.exit(str(error))

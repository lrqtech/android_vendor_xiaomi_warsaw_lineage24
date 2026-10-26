# Xiaomi warsaw vendor files

Prepared inputs for unofficial LineageOS 24.0, based on the
OS4.0.0.15.XHPCNXM Android 17 OTA.

## Checkout

Use `warsaw-20261027` with the matching
[device](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24) and
[kernel](https://github.com/lrqtech/android_kernel_xiaomi_warsaw_lineage24) tags.
All three repositories use the `lineage-24.0` development branch.

```sh
git lfs install
git clone --branch warsaw-20261027 https://github.com/lrqtech/android_vendor_xiaomi_warsaw_lineage24.git vendor/xiaomi/warsaw
git -C vendor/xiaomi/warsaw lfs pull
git -C vendor/xiaomi/warsaw lfs fsck
python3 vendor/xiaomi/warsaw/verify-files.py
```

The actual LFS payloads are required. Follow the device
[build instructions](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/warsaw-20261027/docs/BUILD.md)
for the pinned platform and companion patches.

## Contents

| Directory | Contents |
| --- | --- |
| `proprietary/` | 5,559 userspace inputs: HALs, libraries, configuration and selected OEM apps |
| `boot/` | DTB/DTBO, OEM modules and recovery inputs |
| `boot/gki-no-kunit/` | 4 KiB Image, 78 paired GKI modules, config, public certificate and hashes |
| `firmware/` | Firmware images selected for packaging |
| `configs/`, `Xpan/` | Vendor integration inputs |

The GKI set includes the October 25 protected-export repair. Its source snapshot
and hashes are recorded in `boot/gki-no-kunit/manifest.json`; the kernel tree's
`warsaw/check-vendor.py` checks the pairing. Only the public signing certificate
is included. Keep Image and its complete signed module set together.

## Vega / SenseTime removal

The Vega/SenseTime SDK, Mi FD node, ECD engine and snapshot plugin/preprocessor,
face ROI encoding filter, three Vega models, and earlier portrait-repair inputs
are removed. Their optional features are disabled. Six selector references use
the retained Qti FD node, and the anchor library always takes its existing ECD
bypass, including when an older persistent property has a different value.

Two retained ELF files have exact-hash preparation scripts in the device tree.
Their public ABI and segment layouts are unchanged. The original Qti FD library
is retained. Camera routing and missing-metadata paths have host checks; camera
inference, image quality and codec operation still require device validation.
See [DIFFERENCES.md](docs/DIFFERENCES.md) for the full changes from stock.

## Startup cleanup and validation

The October 27 cleanup removes 40 unavailable or unrunnable OEM service
definitions, their callers, and nine dedicated files. The current Settings fan
implementation remains selected. Debug property triggers can no longer stop
`mi_thermald` or change modem log paths to 777. Obsolete service labels and
permissions are removed in the matching device policy.

`docs/payload-sha256.json` records all 6,214 prepared payloads. The device tree
reproduces vendor metadata from the prepared baseline and rejects retired inputs.
Raw OTA and running-device extraction are not yet supported.

The latest source defaults to SELinux enforcing in normal boot and recovery.
The clean full Android build from `warsaw-20261027` completed on October 27.
The OTA and matching first-install images passed host signature, AVB, partition,
VINTF and embedded-policy checks. The packaged GKI and its 78 modules match this
vendor input set. No physical-device test was performed. See the device
[build results](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/lineage-24.0/docs/BUILD_RESULT_20261027.txt)
and [status page](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/lineage-24.0/docs/STATUS.md).

## Licensing

Proprietary files remain subject to their owners' terms. This repository does
not grant redistribution rights or relicense those files. Existing licenses and
copyright notices are retained.

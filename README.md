# Xiaomi warsaw vendor files

Proprietary files for LineageOS 24 on Xiaomi warsaw, based on the
OS4.0.0.15.XHPCNXM Android 17 OTA. Place this repository at
`vendor/xiaomi/warsaw` and follow the
[device build instructions](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/lineage-24.0/docs/BUILD.md).

## Git LFS

Install Git LFS before cloning. After checkout, download and check the files:

```sh
git lfs pull
git lfs fsck
```

The build requires the actual files, not LFS pointers.

## Contents

| Directory | Contents |
| --- | --- |
| `proprietary/` | HALs, libraries, configuration and OEM app files |
| `firmware/` | OTA firmware images used by the device tree |
| `boot/` | Boot configuration, DTB/DTBO, OEM modules and stock GKI fallback |
| `boot/gki-no-kunit/` | Source-built 4 KiB Image, 78 GKI modules, config, public signing certificate and hashes |

The 538 OEM modules and six recovery variants are unchanged from the OTA.
GKI source and build instructions are in the
[kernel repository](https://github.com/lrqtech/android_kernel_xiaomi_warsaw_lineage24).

[DIFFERENCES.md](docs/DIFFERENCES.md) lists changes from the OTA, including
the camera library fixups and repacked Mi Remote APK.
[payload-sha256.json](docs/payload-sha256.json) records the file hashes.
Known hardware issues are tracked in the
[device tree](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/lineage-24.0/docs/STATUS.md).

## Licensing

Proprietary files remain subject to their owners' terms. This repository
does not grant redistribution rights or apply an open-source license to
those files. Existing source licenses and copyright notices are retained.

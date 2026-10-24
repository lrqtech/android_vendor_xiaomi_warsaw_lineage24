# Xiaomi warsaw vendor files

Prepared vendor inputs for unofficial LineageOS 24.0, based on the
OS4.0.0.15.XHPCNXM Android 17 OTA.

## Checkout

Use the `warsaw-20261024` source set with the matching
[device tree](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24)
and [kernel](https://github.com/lrqtech/android_kernel_xiaomi_warsaw_lineage24).
All three repositories use the `lineage-24.0` branch.

```sh
git lfs install
git clone --branch warsaw-20261024 https://github.com/lrqtech/android_vendor_xiaomi_warsaw_lineage24.git vendor/xiaomi/warsaw
git -C vendor/xiaomi/warsaw lfs pull
git -C vendor/xiaomi/warsaw lfs fsck
python3 vendor/xiaomi/warsaw/verify-files.py
```

The build requires the actual LFS payloads. Follow the
[device build instructions](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/lineage-24.0/docs/BUILD.md)
for the pinned platform and required patches.

## Contents

| Directory | Contents |
| --- | --- |
| `proprietary/` | 5,589 userspace inputs, including HALs, libraries, configuration, and OEM apps |
| `boot/` | Boot inputs, DTB/DTBO, OEM modules, recovery modules, and stock GKI fallback |
| `boot/gki-no-kunit/` | 4 KiB Image, 78 matching GKI modules, config, public certificate, and hashes |
| `firmware/` | Firmware images selected for packaging |
| `configs/`, `Xpan/` | Vendor integration inputs |

The kernel Image and GKI modules are unchanged from the October 15 source set.
This update includes startup and service fixes and the recovery touch modules.
See [DIFFERENCES.md](docs/DIFFERENCES.md) for the changes from stock firmware.

The device tree supplies prepared-blob import and metadata generation tools.
They reproduce this baseline; raw OTA and running-device extraction remain
unsupported. The device [status page](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/lineage-24.0/docs/STATUS.md)
records the remaining runtime checks. Normal boot and recovery remain permissive.

## Licensing

Proprietary files remain subject to their owners' terms. This repository does
not grant redistribution rights or relicense those files. Existing source
licenses and copyright notices are retained.

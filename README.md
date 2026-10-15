# Xiaomi Warsaw proprietary inputs for LineageOS 24

Private vendor snapshot for `warsaw`, based on the Xiaomi
OS4.0.0.15.XHPCNXM Android 17 OTA and the paired source-built no-KUnit GKI.
This repository belongs at `vendor/xiaomi/warsaw` in the pinned platform
workspace described by the [device repository](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24).

## Fetching files

Git LFS is mandatory. Install it before cloning, authenticate to the private
repository, then run `git lfs pull` and `git lfs fsck` in this checkout.
Small LFS pointer files are not valid build inputs.

## Contents

- `proprietary/`: selected HALs, libraries, firmware configuration and OEM
  application inputs, with their Android build definitions.
- `firmware/`: retained OTA firmware images required by the device configuration.
- `boot/`: OTA boot geometry, DTB/DTBO, vendor modules and stock fallback inputs.
- `boot/gki-no-kunit/`: the paired source-built Image and 78 production GKI
  modules, build configuration, public signing certificate and hash manifest.

The 538 unique OEM vendor modules and six recovery-specific variants retain
the reference OTA bytes. This is not a claim that those OEM modules have been
reproduced from source. The GKI source is in the
[kernel repository](https://github.com/lrqtech/android_kernel_xiaomi_warsaw_lineage24).

Read [DIFFERENCES.md](docs/DIFFERENCES.md) before comparing with the OTA.
`docs/payload-sha256.json` records the exact files published in this snapshot.
This is an unofficial development input set; device acceptance and on-device
functional validation remain separate tasks.

## Licensing

Proprietary components remain subject to their original owners' terms.
Existing source notices are retained. No blanket open-source license or
redistribution permission is asserted over these binaries. Private storage
does not change their licensing status.

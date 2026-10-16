# Changes from the Xiaomi OTA

Reference: **OS4.0.0.15.XHPCNXM**, Android 17,
build `17OS4.0.260920.220420124.QCPECN.S`.

## Kernel and modules

The default kernel is a source-built 4 KiB GKI Image with 78 matching
production modules and KUnit disabled. Stock GKI files are kept as a fallback.
The 538 OEM modules and six recovery variants retain their original OTA bytes.

The GKI file manifest uses repository-relative paths. Its paths have changed;
the Image and module bytes have not. Only the public module-signing
certificate is included.

## Libraries and apps

- Six ODM camera libraries have their AHardwareBuffer import version metadata
  adjusted for the system ABI. These files differ from the OTA.
- Camera and metadata bridge libraries support the retained face-unlock
  implementation. Selected OTA camera engines and CameraX dependencies are
  also included.
- Mi Remote is repacked to meet native-library installation requirements and
  is signed during the ROM build. It no longer has the original OEM signature.
- Camera and Mi Remote are the only additional OEM consumer apps selected by
  the product. MIUI Security Center is excluded.
- Five IMS/data libraries require 4 KiB pages. They have per-library build
  exceptions; the device tree rejects kernels with a different page size.

## Startup and hardware configuration

Init services, sockets and node labels are adapted for LineageOS. Unused
HyperOS and debug startup paths are removed. Vendor module loading waits for
the load operation to finish and checks its result.

GNSS uses OEM assistance/XTRA settings and Android CA paths. An outdoor fix
has not yet been confirmed; see the device [known issues](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/lineage-24.0/docs/STATUS.md).

## File hashes and extraction

[payload-sha256.json](payload-sha256.json) lists the hashes of the files in
this repository, including modified files. It is not a list of original OTA
hashes. A portable extraction and fixup script for the full vendor tree is
still needed.

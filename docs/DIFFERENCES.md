# Differences from the reference Xiaomi OTA

Reference: Warsaw OS4.0.0.15.XHPCNXM, build
`17OS4.0.260920.220420124.QCPECN.S`, Android 17.
This repository is a curated integration input set, not an unchanged OTA dump.

| Area | Published behavior or change |
| --- | --- |
| GKI | Source-built 4 KiB Image and 78 production modules; KUnit disabled; stock fallback inputs retained separately |
| OEM modules | 538 unique vendor modules and six recovery variants retain their OTA bytes |
| Camera ABI | Six ODM libraries have only the affected AHardwareBuffer import version metadata adjusted for the build/runtime ABI; they are not byte-identical OTA blobs |
| Face bridge | Dedicated camera/metadata bridge dependencies isolate the retained face implementation from incompatible system ABI changes |
| Camera runtime | Selected OTA camera engines and CameraX dependencies are supplied for the retained camera integration |
| Mi Remote | Selected APK is repacked for native-library installation requirements and signed by the ROM build; it is not the original OEM-signed APK |
| Init and policy | Service, socket and node labels are adapted to LineageOS; dead debug/HyperOS startup paths are omitted; vendor module loading waits for the real result |
| GNSS | OEM-native assistance/XTRA inputs and Android CA paths are selected; an outdoor position fix is still unconfirmed |
| Consumer apps | Camera and Mi Remote are the selected additional OEM consumer apps; MIUI Security Center is not included in the product |
| Page size | Five IMS/data libraries remain 4 KiB-only; scoped build exceptions apply and the device configuration rejects another kernel page size |

The hash manifest identifies the exact published inputs, including modified
files. It must not be interpreted as proof that every proprietary file is
unchanged from the OTA. There is no complete portable extraction/fixup script
for this whole input set yet; see the device repository's status document.

The GKI manifest's old machine-specific paths are replaced with portable
repository paths. This metadata cleanup does not alter the Image or module
bytes. Only the public module-signing certificate is stored; no private
signing key or GitHub credential is part of this repository.

# Changes from the Xiaomi OTA

Reference: **OS4.0.0.15.XHPCNXM**, Android 17,
build `17OS4.0.260920.220420124.QCPECN.S`.

## Kernel and modules

The default kernel is a source-built 4 KiB GKI Image with 78 matching
production modules and KUnit disabled. The unused OEM GKI Image, boot.img and
system_dlkm.img fallback inputs were removed on October 26; the paired
source-built GKI inputs are retained.
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
the load operation to finish and checks its result. The October 24 update adds
service domains, narrows startup ordering, and aligns boot-time node access with
the matching device policy. The qvrd USB MTU command runs in its dedicated domain.
Recovery receives the retained Xiaomi touch and Goodix module inputs.

GNSS uses OEM assistance/XTRA settings and Android CA paths. An outdoor fix
has not yet been confirmed; see the device [known issues](https://github.com/lrqtech/android_device_xiaomi_warsaw_lineage24/blob/lineage-24.0/docs/STATUS.md).

## File hashes and extraction

[payload-sha256.json](payload-sha256.json) lists the hashes of the files in
this repository, including modified files. It is not a list of original OTA
hashes. The device tree now provides prepared-input verification, import, and metadata
generation. Raw OTA and running-device extraction still need reproducible fixups
and a validated round trip.

## October 26 official-requirements cleanup

Removed libportrait_repair_qnn.so, its com.xiaomi.plugin.portraitrepair loader,
SensePR_scene_configs.json and the corresponding facesr model. The SDK exports
stm_portrait_repair APIs and embeds st_mobile code. It is excluded under the
LineageOS prohibition on SenseTime components. Six Xiaomi snapshot graphs now
connect the predecessor directly to the successor of PortraitRepairInstance0;
both portrait-repair support masks are zero. Other graph nodes, including beauty
and AWB, are unchanged. This optional portrait-restoration feature is disabled.

Also removed five uninstalled init scripts, the unused original libmiface.so,
the unused system_ext DPM library copy and the unused prebuilt vndservicemanager.
Their selected repaired/shared/source implementations remain in place.

Only seven retained payload files changed in this cleanup: six graph JSON files
and camxoverridesettings.txt. No retained ELF, APK, kernel, module or firmware
bytes were rewritten. Input lists, generator rules and both hash inventories
were synchronized and checked against isolated raw-generator output.

At this review stage libvega_common.so still blocked its removal because the
Mi FD node imported eight XMFaceAttribute/XMFaceEmotion entry points. That
dependency is removed by the subsequent October 27 change described below.
Megvii-marked wrapper provenance and the other official-support gaps remain open.

## October 27 Vega/SenseTime removal

The nine remaining SDK inputs and consumers are removed together. Six Mi FD
loader references in com.qti.chiusecaseselector.so now select the already-shipped
com.qti.node.fd.so. The input/output descriptors, properties and prune variant
of these nodes match the original Qti FD descriptor. No sensor, crop, AWB or
camera ID selection is changed. The unused Mi FD loader string is cleared only
after all its relocation references are redirected and direct code references
are checked. Host execution also verifies that the RTB face helper clears its
output and exits when extended FD data is missing; ordinary timestamp dependency
registration is unchanged.

The anchor plugin's ECD bypass is unconditional, so a saved property cannot
reactivate closed-eye frame selection. Three snapshot graphs bypass four ECD
nodes, both codec configurations remove the automatic face ROI filter, and
FDEnableAttribute is zero. The SenseTime Chat allowlist entry is removed.

Only two retained ELF files are adapted, using exact input/output SHA256 and
site checks; their public build IDs are updated. The retained Qti FD binary and
all other retained ELF/APK/kernel/module/firmware payloads are unchanged. Seven
configuration payloads are updated. Source preparation and the closed branches
have host checks; real camera inference, image quality, codec processing and
device boot have not been validated on hardware.

## October 27 startup service cleanup

Removed forty disabled OEM service definitions whose executables are absent or
whose entry points have no valid SELinux transition. This includes the unused
legacy fan control and diagnostic/test services; Settings still owns manual PWM
control. Matching RC and shell callers are removed, including references to the
absent wcnss, logcatlog and qvirt services. Upstream ABI/APEX alternatives remain.

Nine dedicated payloads are removed. No retained ELF, APK, kernel, module or
firmware bytes change in this cleanup. Five retained RC files and four shell
scripts change. The legacy property that stopped mi_thermald and the two debug
properties that changed modem log permissions to 777 no longer have init actions.
Normal RIL startup, modem configuration copying, thermal service startup and
current fan control remain intact. The matching device policy removes the
obsolete IRQ-balance and wigig-socket labels and grants.

The current inventory is 5,559 userspace inputs, 2,265 Blueprint modules and
6,214 payload hashes. Prepared import refuses retired files and startup hooks.

LOCAL_PATH := $(call my-dir)
include $(CLEAR_VARS)
LOCAL_MODULE := XpanResTarget_Vendor
LOCAL_MODULE_CLASS := APPS
LOCAL_MODULE_TAGS := optional
LOCAL_MODULE_SUFFIX := $(COMMON_ANDROID_PACKAGE_SUFFIX)
LOCAL_MODULE_PATH := $(TARGET_OUT_VENDOR)/overlay
LOCAL_SRC_FILES := ../proprietary/vendor/overlay/XpanResTarget_Vendor.apk
LOCAL_CERTIFICATE := PRESIGNED
LOCAL_SDK_VERSION := 35
LOCAL_IS_RUNTIME_RESOURCE_OVERLAY := true
# The verified OTA RRO contains resources and a manifest, with no DEX to precompile.
LOCAL_DEX_PREOPT := false
include $(BUILD_PREBUILT)

# Custom ABI configuration for the OpenCV Android build.
# Consumed by opencv/platforms/android/build_sdk.py via the --config argument.
# The ABI() class is injected into this file's scope by build_sdk.py at exec time.
#
# 4 ABIs (full build). To slim down, remove entries or switch to arm64-v8a only.

ABIs = [
    ABI("2", "armeabi-v7a", None, 21, cmake_vars=dict(ANDROID_ABI='armeabi-v7a with NEON')),
    ABI("3", "arm64-v8a",   None, 21, cmake_vars=dict(ANDROID_SUPPORT_FLEXIBLE_PAGE_SIZES='ON')),
    ABI("5", "x86_64",      None, 21, cmake_vars=dict(ANDROID_SUPPORT_FLEXIBLE_PAGE_SIZES='ON')),
    ABI("4", "x86",         None, 21),
]

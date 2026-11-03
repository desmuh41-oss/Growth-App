[app]
title = GrowthCalc
package.name = growthcalc
package.domain = com.muhumuza.growth
source.dir = .
source.include_exts = py
version = 1.0
requirements = python3,kivy
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
archs = arm64-v8a, armeabi-v7a

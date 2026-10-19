[app]
title = Tarot App
package.name = tarotapp
package.domain = org.tarot
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec
source.include_patterns = assets/*,images/*
version = 0.1
requirements = python3,kivy
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk_accept_license = True
android.private_storage = True
orientation = portrait
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_root = 1

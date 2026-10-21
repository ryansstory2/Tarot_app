[app]

# (str) Title of your application
title = My App

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source files where the let it live (relative to directory of spec)
source.dir = .

# (list) Source files to include (let it empty to include all the files)
source.exts = py,png,jpg,kv,atlas

# (str) Application versioning (versioning method 1)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API your APK will support
android.min_api = 21

# (bool) Enable Android SDK accept license
android.accept_sdk_license = True

# (str) Android NDK version to use
android.ndk = 25b

[buildozer]
# (int) Log level (1 = info)
log_level = 1

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

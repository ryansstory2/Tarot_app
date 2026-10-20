[app]

# (str) Title of your application
title = Tarot App

# (str) Package name
package.name = tarotapp

# (str) Package domain (needed for android packaging)
package.domain = org.tarot

# (list) Source files to include (let it pick up everything standard)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source directory where the application lives
source.dir = .

# (list) Application requirements
requirements = python3,kivy

# (list) Supported orientations
orientation = portrait

#
# Android specific
#

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Enable Android auto backup
android.enable_androidx = True

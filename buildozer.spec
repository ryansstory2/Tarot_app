[app]

# (str) Title of your application
title = Tarot App

# (str) Package name
package.name = tarotapp

# (str) Package domain (needed for android packaging)
package.domain = org.tarot

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Source directory where the application files are located
source.dir = .

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,pillow

# (str) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 31

# (int) Minimum API your APK will support.
android.minAPI = 21

# (str) Android entry point
android.entrypoint = main.py

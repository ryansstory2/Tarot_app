[app]

# (str) Title of your application
title = Tarot App

# (str) Package name
package.name = tarotapp

# (str) Package domain (needed for android packaging)
package.domain = org.tarot

# (list) Source files to include (let it find python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (optional)
source.exclude_exts = spec

# (list) List of inclusion/exclusion patterns
source.include_patterns = assets/*,images/*

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Specify Kivy and its dependencies explicitly
requirements = python3,kivy

# (str) Custom source folders for dependencies
#source.dev_libs = ../../lib

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Supported orientations
orientation = portrait

# (list) The format used to package the app for each architecture
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1
# (str) Title of your application
title = Tarot App

# (str) Package name
package.name = tarotapp

# (str) Package domain (needed for android packaging)
package.domain = org.tarot

# (list) Source files to include (let it find python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (optional)
source.exclude_exts = spec

# (list) List of inclusion/exclusion patterns
source.include_patterns = assets/*,images/*

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Specify Kivy and its dependencies explicitly
requirements = python3,kivy

# (str) Custom source folders for dependencies
#source.dev_libs = ../../lib

# (list) Permissions
android.permissions = INTERNET

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (int) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Supported orientations
orientation = portrait

# (list) The format used to package the app for each architecture
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_root = 1

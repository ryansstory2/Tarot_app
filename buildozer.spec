[app]

# (str) Title of your application
title = My Kivy App

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source directory where the main.py file lives
source.dir = .

# (list) Source files to include (let it default or specify your python files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

[buildozer]
log_level = 2

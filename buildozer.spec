[app]

# (str) Title of your application
title = Tmz up du Peuple

# (str) Package name
package.name = tmz_up_du_peuple

# (str) Package domain (needed for android/ios packaging)
package.domain = org.rubangchynnovation

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf

# (list) List of inclusions using pattern matching
source.include_patterns = Fredoka-Regular.ttf

# (str) Application versioning (method 1)
version = 1.0

# ⚠️ CHANGEMENT CRITIQUE: Requirements complètes avec versions compatibles
requirements = python3,kivy==2.3.0,pyjnius,android,plyer,sdl2_ttf,pillow

# (str) Icon of the application
icon.filename = icon.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# ⚠️ CHANGEMENT: Permissions étendues pour éviter les crashes
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK,VIBRATE

# ⚠️ CHANGEMENT: API compatibles avec le workflow - build-tools stable
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2

# ⚠️ CHANGEMENT: Architecture double comme dans le workflow
android.archs = armeabi-v7a, arm64-v8a

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (bool) Skip byte compile for .py files
android.no-byte-compile-python = False

# (str) The format used to package the app for debug mode
android.debug_artifact = apk

# (bool) Skip byte compile for .py files
android.allow_backup = True

#
# Python for android (p4a) specific
#

# (str) python-for-android URL to use for checkout
p4a.url = https://github.com/kivy/python-for-android

# ⚠️ CHANGEMENT: Bootstrap explicite pour SDL2
p4a.bootstrap = sdl2

# ⚠️ CHANGEMENT: Branche stable
p4a.branch = master

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1

# (str) Path to build artifact storage, absolute or relative to spec file
build_dir = ./.buildozer
log_dir   = ./.buildozer/logs
bin_dir   = ./bin
dist_dir  = ./.buildozer/dist
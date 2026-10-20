name: CI

on:
  push:
    branches: [ main, master ]

jobs:
  build:
    runs-on: ubuntu-22.04
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
      cancel-in-progress: true

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Cache Buildozer global directory
        uses: actions/cache@v4
        with:
          path: |
            .buildozer
            bin/
          key: buildozer-${{ hashFiles('buildozer.spec') }}
          restore-keys: |
            buildozer-

      - name: Build APK with Official Buildozer Docker Image
        run: |
          echo "y" | docker run --rm -it \
            -v ${{ github.workspace }}:/home/user/hostcwd \
            -e BUILDOZER_ALLOW_ROOT=1 \
            kivy/buildozer:latest \
            android debug

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: kivy-android-apk
          path: bin/*.apk
          retention-days: 7

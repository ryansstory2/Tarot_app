name: CI

on:
  push:
    branches: [ main, master ]

jobs:
  build:
    runs-on: ubuntu-latest
    concurrency:
      group: ${{ github.workflow }}-${{ github.ref }}
      cancel-in-progress: true

    steps:
      - name: Checkout Code
        uses: actions/checkout@v4

      - name: Maximize build disk space
        uses: AdityaGarg8/maximize-build-space@v5
        with:
          remove-dotnet: 'true'
          remove-android: 'false'
          remove-haskell: 'true'
          remove-codeql: 'true'
          reserve-swap: '4096'

      - name: Cache Buildozer global directory
        uses: actions/cache@v3
        with:
          path: ~/.buildozer
          key: ${{ runner.os }}-buildozer-${{ hashFiles('buildozer.spec') }}
          restore-keys: |
            ${{ runner.os }}-buildozer-

      - name: Build APK with Official Buildozer Docker Image
        uses: ArtemSBulgakov/buildozer-action@v1
        with:
          command: buildozer -v android debug

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: package
          path: bin/*.apk

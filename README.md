# Google Sans web fonts
Google Sans, Google Sans Display, Google Sans Text & Gallery Icons web fonts.

This repository provides automatic scripts to convert font files from .ttf format into .woff and .woff2 formats.

## Sources
Fonts available in .ttf format (placed in the `TTF` directory):
* Google Sans, Google Sans Display, and Gallery Icons: [Google Git](https://bit.ly/GoogleSans)
* Google Sans Text: [GMS APK](https://bit.ly/gms12)

## Generating .woff and .woff2 webfonts
### Prerequisite: conversion programs
* **TTF to WOFF**: `sfnt2woff` (from package [`woff-tools`](https://packages.ubuntu.com/woff-tools))
* **TTF to WOFF2**: `woff2_compress` (from package [`woff2`](https://packages.ubuntu.com/woff2))

### Generating all webfonts
Run
```shell
make
```
to generate .woff and .woff2 webfonts.

* The .woff webfonts will be put in the `WOFF` directory.
* The .woff2 webfonts will be put in the `WOFF2` directory.

### Cleanup
Run
```shell
make clean
```
to clean up.

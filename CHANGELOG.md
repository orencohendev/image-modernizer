# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0]

### Added

- Rebranded the software as Image Modernizer.
- Added a theme to make the UI more inviting.
- Added support for JPEG and JPG files.

### Fixed

- Removed the console window that was opening when launching the built binary by adding `--noconsole` to pyinstaller.
- Made sure the original file name carried over to the webp save file dialog.

## [0.1.1] - 2023-06-14

### Added

- support for windows and mac releases.
- initial release

### fixed

- changes to CI yaml to correctly build.

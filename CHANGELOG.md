# CHANGELOG
Inspired from [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)

## [Unreleased]
### Added
### Changed
### Deprecated
### Removed
### Fixed
### Security
### Dependencies

## [0.2.4]
### Added
- Add Dockerfile and Github action ([#24](https://github.com/MechanicalFlower/magic_combo/pull/24))
- Add command to easily setup new project ([#23](https://github.com/MechanicalFlower/magic_combo/pull/23))
### Changed
- Add the no-clobber option to curl command ([#26](https://github.com/MechanicalFlower/magic_combo/pull/26))
### Deprecated
### Removed
### Fixed
- Use the magic combo cli in the Dockerfile ([#27](https://github.com/MechanicalFlower/magic_combo/pull/27))
- Use local links for license files when generate CREDITS.md ([#29](https://github.com/MechanicalFlower/magic_combo/pull/29))
- Ensure .combo directory is created before install godot or templates ([#31](https://github.com/MechanicalFlower/magic_combo/pull/31))
### Security
### Dependencies
- Bump `pre-commit` from 3.4.0 to 3.5.0 ([#25](https://github.com/MechanicalFlower/magic_combo/pull/25))
- Bump `pytest-mock` from 3.11.1 to 3.12.0 ([#28](https://github.com/MechanicalFlower/magic_combo/pull/28))

## [0.2.3]
### Fixed
- Remove unexcepted quotation mark ([#21](https://github.com/MechanicalFlower/magic_combo/pull/21))

## [0.2.2]
### Fixed
- Correctly create Github release in CD ([#20](https://github.com/MechanicalFlower/magic_combo/pull/20))

## [0.2.1]
### Added
- Add Github release creation in CD ([#15](https://github.com/MechanicalFlower/magic_combo/pull/15))
- Add urls to pyproject.toml ([#16](https://github.com/MechanicalFlower/magic_combo/pull/16))
### Changed
- Use black as formatter instead of yapf ([#17](https://github.com/MechanicalFlower/magic_combo/pull/17))
### Fixed
- Correctly define default values ([#18](https://github.com/MechanicalFlower/magic_combo/pull/18))

## [0.2.0]
### Added
- Add Pull Request title linter in CI ([#9](https://github.com/MechanicalFlower/magic_combo/pull/9))
- Add support for python versions from 3.10 to 3.12 ([#10](https://github.com/MechanicalFlower/magic_combo/pull/10))
- Add link checker in CI ([#11](https://github.com/MechanicalFlower/magic_combo/pull/11))
### Changed
- Update the README to make it standard ([#8](https://github.com/MechanicalFlower/magic_combo/pull/8))
- Refactor scripts to use it as one program with pyinvoke ([#5](https://github.com/MechanicalFlower/magic_combo/pull/5))
### Dependencies
- Bump `sigstore/gh-action-sigstore-python` from 2.0.1 to 2.1.0 ([#6](https://github.com/MechanicalFlower/magic_combo/pull/6))
- Bump `actions/checkout` from 2 to 4 ([#13](https://github.com/MechanicalFlower/magic_combo/pull/13))
- Bump `stefanzweifel/git-auto-commit-action` from 4 to 5 ([#12](https://github.com/MechanicalFlower/magic_combo/pull/12))

[Unreleased]: https://github.com/MechanicalFlower/magic_combo/compare/0.2.4...HEAD
[0.2.4]: https://github.com/MechanicalFlower/magic_combo/compare/0.2.3...0.2.4
[0.2.3]: https://github.com/MechanicalFlower/magic_combo/compare/0.2.2...0.2.3
[0.2.2]: https://github.com/MechanicalFlower/magic_combo/compare/0.2.1...0.2.2
[0.2.1]: https://github.com/MechanicalFlower/magic_combo/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/MechanicalFlower/magic_combo/compare/0.1.1...0.2.0

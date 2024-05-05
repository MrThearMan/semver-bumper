# SemVer Bumper

> This is a work in progress.

[//]: # ([![Coverage Status][coverage-badge]][coverage])
[//]: # ([![GitHub Workflow Status][status-badge]][status])
[//]: # ([![PyPI][pypi-badge]][pypi])
[//]: # ([![GitHub][licence-badge]][licence])
[//]: # ([![GitHub Last Commit][repo-badge]][repo])
[//]: # ([![GitHub Issues][issues-badge]][issues])
[//]: # ([![Downloads][downloads-badge]][pypi])
[//]: # ([![Python Version][version-badge]][pypi])

[//]: # (```shell)
[//]: # (pip install semver-bumper)
[//]: # (```)

---

**Documentation**: [https://mrthearman.github.io/semver-bumper/](https://mrthearman.github.io/semver-bumper/)

**Source Code**: [https://github.com/MrThearMan/semver-bumper/](https://github.com/MrThearMan/semver-bumper/)

**Contributing**: [https://github.com/MrThearMan/semver-bumper/blob/main/CONTRIBUTING.md](https://github.com/MrThearMan/semver-bumper/blob/main/CONTRIBUTING.md)

---

Automatically determine semantic version bumping from changes in your app's
interface, i.e., existing functions, classes and variables, as well as their
arguments and types.

https://semver.org/

https://datatracker.ietf.org/doc/html/rfc2119

### Spec (WIP):

1. Go through all python files in the project.
	1. MUST be able to exclude folders and files from this scan.
2. For each file, note all functions, classes and variables that exist,
   as well as the arguments for each function and method, and their types.
   This is the `NEW API` for the project.
	1. If the name of the variable, function, class or method begins with
	   an underscore (`_foo`), or double-underscore (`__foo`), but it is not
	   a "dunder method" (e.g., `__init__`), it MUST be excluded.
	2. If the file contains an `__all__` declaration, only those variables,
	   functions and classes MUST be considered.
3. Now, do the same for the previous version in the git history.
   This is the `OLD API` for the project.
	1. If there is no previous tag, the previous version is the initial commit.
	2. MUST be able to configure that the previous tag should look like.
	3. If not configured, the previous tag MUST be in SemVer.
4. Compare the `NEW API` and the `OLD API`:
	1. If there are no additions, modifications or deletions in the `NEW API`
	   (meaning only insides have changed), `NEW API` version MUST be a **PATCH** version.
	2. If there are only additions in the `NEW API`, but no modifications or deletions,
	   the `NEW API` version MUST be a **PATCH** version.
		1. If the change is significant enough, the `NEW API` version MAY also be
		   a **MINOR** version. The user MUST decide this.
	3. If a variable, function, class, or a method has been moved from one file to another,
	   this SHOULD NOT be considered a deletion or an addition.
	4. If there are any modifications in the `NEW API`:
		1. If the only modifications are for new keyword-only arguments for functions
		   or methods, which have default parameters, the `NEW API` version MUST be a **PATCH** version.
		2. If the only modifications are in the types of arguments for variables, functions
	       or methods. The type in the `NEW API` is still a subclass of the type in the `OLD API`,
	       the `NEW API` version MUST be a **PATCH** version.
		3. TODO ...
		4. Otherwise:
			1. If the current **MAJOR** version is 0, the new version MUST be a **MINOR** version.
			2. Else, the new version MUST be a **MAJOR** version.

[coverage-badge]: https://coveralls.io/repos/github/MrThearMan/semver-bumper/badge.svg?branch=main
[status-badge]: https://img.shields.io/github/actions/workflow/status/MrThearMan/semver-bumper/test.yml?branch=main
[pypi-badge]: https://img.shields.io/pypi/v/semver-bumper
[licence-badge]: https://img.shields.io/github/license/MrThearMan/semver-bumper
[repo-badge]: https://img.shields.io/github/last-commit/MrThearMan/semver-bumper
[issues-badge]: https://img.shields.io/github/issues-raw/MrThearMan/semver-bumper
[version-badge]: https://img.shields.io/pypi/pyversions/semver-bumper
[downloads-badge]: https://img.shields.io/pypi/dm/semver-bumper

[coverage]: https://coveralls.io/github/MrThearMan/semver-bumper?branch=main
[status]: https://github.com/MrThearMan/semver-bumper/actions/workflows/test.yml
[pypi]: https://pypi.org/project/semver-bumper
[licence]: https://github.com/MrThearMan/semver-bumper/blob/main/LICENSE
[repo]: https://github.com/MrThearMan/semver-bumper/commits/main
[issues]: https://github.com/MrThearMan/semver-bumper/issues

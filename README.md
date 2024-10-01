# dynamic-lcia-app

[![PyPI](https://img.shields.io/pypi/v/dynamic-lcia-app.svg)][pypi status]
[![Status](https://img.shields.io/pypi/status/dynamic-lcia-app.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/dynamic-lcia-app)][pypi status]
[![License](https://img.shields.io/pypi/l/dynamic-lcia-app)][license]

[![Read the documentation at https://dynamic-lcia-app.readthedocs.io/](https://img.shields.io/readthedocs/dynamic-lcia-app/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/TimoDiepers/dynamic-lcia-app/actions/workflows/python-test.yml/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/TimoDiepers/dynamic-lcia-app/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi status]: https://pypi.org/project/dynamic-lcia-app/
[read the docs]: https://dynamic-lcia-app.readthedocs.io/
[tests]: https://github.com/TimoDiepers/dynamic-lcia-app/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/TimoDiepers/dynamic-lcia-app
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Installation

You can install _dynamic-lcia-app_ via [pip] from [PyPI]:

```console
$ pip install dynamic-lcia-app
```

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide][Contributor Guide].

## License

Distributed under the terms of the [BSD 3 Clause license][License],
_dynamic-lcia-app_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue][Issue Tracker] along with a detailed description.


<!-- github-only -->

[command-line reference]: https://dynamic-lcia-app.readthedocs.io/en/latest/usage.html
[License]: https://github.com/TimoDiepers/dynamic-lcia-app/blob/main/LICENSE
[Contributor Guide]: https://github.com/TimoDiepers/dynamic-lcia-app/blob/main/CONTRIBUTING.md
[Issue Tracker]: https://github.com/TimoDiepers/dynamic-lcia-app/issues


## Building the Documentation

You can build the documentation locally by installing the documentation Conda environment:

```bash
conda env create -f docs/environment.yml
```

activating the environment

```bash
conda activate sphinx_dynamic-lcia-app
```

and [running the build command](https://www.sphinx-doc.org/en/master/man/sphinx-build.html#sphinx-build):

```bash
sphinx-build docs _build/html --builder=html --jobs=auto --write-all; open _build/html/index.html
```
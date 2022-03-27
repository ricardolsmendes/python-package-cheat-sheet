# python-package-cheat-sheet

Notes &amp; thoughts on clean Python package design.

[![license](https://img.shields.io/github/license/ricardolsmendes/python-package-cheat-sheet.svg)](https://github.com/ricardolsmendes/python-package-cheat-sheet/blob/master/LICENSE)
[![issues](https://img.shields.io/github/issues/ricardolsmendes/python-package-cheat-sheet.svg)](https://github.com/ricardolsmendes/python-package-cheat-sheet/issues)

## Get to know the concepts behind this code

[A Python Package Developer’s Cheat Sheet][1] @ Better Programming / Medium

- [Polish version][2], translated by [Paulina Wyszyńska-Górecka][3]

## Core files

- `setup.py`: the package’s descriptor file, consists of a Python script where multiple properties can be set
  declaratively. Properties declared in this file are recognized by package managers such as `pip` and IDEs such as
  _PyCharm_, which means this is a must-have for any package.

- `setup.cfg`: used to customize setup scripts, such as setting `pytest` as the default runner for
  `python setup.py test` command.

- `.coveragerc`: controls the coverage script scope. This is pretty useful when you have folders in your project that
  don’t need to be monitored by the tool. In the proposed clean structure, only the `src` folder needs to be covered.

## How to contribute

Please make sure to take a moment and read the [Code of
Conduct](https://github.com/ricardolsmendes/python-package-cheat-sheet/blob/master/.github/CODE_OF_CONDUCT.md).

### Report issues

Please report bugs and suggest features via the [GitHub
Issues](https://github.com/ricardolsmendes/python-package-cheat-sheet/issues).

Before opening an issue, search the tracker for possible duplicates. If you find a duplicate, please
add a comment saying that you encountered the problem as well.

### Contribute code

Please make sure to read the [Contributing
Guide](https://github.com/ricardolsmendes/python-package-cheat-sheet/blob/master/.github/CONTRIBUTING.md)
before making a pull request.

[1]: https://medium.com/better-programming/a-python-package-developers-cheat-sheet-3efb9e9454c7?source=friends_link&sk=9ed542198923da7fee0b61bde5b9b61e
[2]: https://bulldogjob.pl/news/804-sciaga-z-robienia-pakietow-w-pythonie
[3]: https://www.linkedin.com/in/paulina-wyszy%C5%84ska

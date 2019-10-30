# python-package-cheat-sheet

Notes &amp; thoughts on clean Python package design.

## Understand the concepts behind this code

[A Python Package Developer’s Cheat Sheet][1] @ Better Programming / Medium
- [Polish version][2], translated by [Paulina Wyszyńska-Górecka][3]

## Core files

- `setup.py`: the package’s descriptor file, consists of a Python script where multiple properties can be set
declaratively. Properties declared in this file are recognized by package managers such as `pip` and IDEs such as
*PyCharm*, which means this is a must-have for any package.

- `setup.cfg`: used to customize setup scripts, such as setting `pytest` as the default runner for
`python setup.py test` command. 

- `.coveragerc`: controls the coverage script scope. This is pretty useful when you have folders in your project that
don’t need to be monitored by the tool. In the proposed clean structure, only the `src` folder needs to be covered. 


[1]: https://medium.com/better-programming/a-python-package-developers-cheat-sheet-3efb9e9454c7?source=friends_link&sk=9ed542198923da7fee0b61bde5b9b61e
[2]: https://bulldogjob.pl/news/804-sciaga-z-robienia-pakietow-w-pythonie
[3]: https://www.linkedin.com/in/paulina-wyszy%C5%84ska

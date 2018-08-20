📦 setup.py (for humans)
=======================

This repo exists to provide [an example setup.py] file, that can be used
to bootstrap your next Python project. It includes some advanced
patterns and best practices for `setup.py`, as well as some
commented–out nice–to–haves.

For example, this `setup.py` provides a `$ python setup.py upload`
command, which creates a *universal wheel* (and *sdist*) and uploads
your package to [PyPi] using [Twine], without the need for an annoying
`setup.cfg` file. It also creates/uploads a new git tag, automatically.

In short, `setup.py` files can be daunting to approach, when first
starting out — even Guido has been heard saying, "everyone cargo cults
thems". It's true — so, I want this repo to be the best place to
copy–paste from :)

[Check out the example!][an example setup.py]

## Additions for binder

It is convenient to provide an [example Jupyter notebook ](example_notebook/import_mypackage.ipynb) for a new package and add the hooks necessary to run the example with Binder. However, normally the package will not be included in the python path. To do that, one needs a `setup.py` for the package (see [binder docs](https://mybinder.readthedocs.io/en/latest/using.html#setup-py)). Once this is done, it is possible to import the package in a notebook running within Binder. [![Binder](https://mybinder.org/badge.svg)](https://mybinder.org/v2/gh/cranmer/setup.py/master?filepath=example_notebook%2Fimport_mypackage.ipynb)


![image]

To Do
-----

-   Tests via `$ setup.py test` (if it's concise).

Pull requests are encouraged!

More Resources
--------------

-   [What is setup.py?] on Stack Overflow
-   [The Hitchhiker's Guide to Packaging]
-   [Cookiecutter template for a Python package]

License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any means.

✨🍰✨

  [an example setup.py]: https://github.com/kennethreitz/setup.py/blob/master/setup.py
  [PyPi]: https://docs.python.org/3/distutils/packageindex.html
  [Twine]: https://pypi.python.org/pypi/twine
  [image]: https://farm1.staticflickr.com/628/33173824932_58add34581_k_d.jpg
  [What is setup.py?]: https://stackoverflow.com/questions/1471994/what-is-setup-py
  [The Hitchhiker's Guide to Packaging]: https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html
  [Cookiecutter template for a Python package]: https://github.com/audreyr/cookiecutter-pypackage

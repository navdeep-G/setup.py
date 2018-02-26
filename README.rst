📦 setup.py (for humans)
========================

This repo exists to provide  `an example setup.py <https://github.com/kennethreitz/setup.py/blob/master/setup.py>`_ file, that can be used to bootstrap your next Python project. It includes some advanced patterns and best practices for ``setup.py``, as well as some commented–out nice–to–haves.

For example, this ``setup.py`` provides a ``$ python setup.py upload`` command, which creates a *universal wheel* (and *sdist*) and uploads your package to `PyPi <https://docs.python.org/3/distutils/packageindex.html>`_ using `Twine <https://pypi.python.org/pypi/twine>`_, without the need for an annoying ``setup.cfg`` file. It also creates/uploads a new git tag, automatically.

In short, ``setup.py`` files can be daunting to approach, when first starting out — even Guido has been heard saying, "everyone cargo cults thems". It's true — so, I want this repo to be the best place to copy–paste from :)

`Check out the example! <https://github.com/kennethreitz/setup.py/blob/master/setup.py>`_

.. image:: https://farm1.staticflickr.com/628/33173824932_58add34581_k_d.jpg


To Do
-----

- Tests via ``$ setup.py test`` (if it's concise).

Pull requests are encouraged!

More Resources
--------------

- `What is setup.py? <https://stackoverflow.com/questions/1471994/what-is-setup-py>`_ on Stack Overflow
- `The Hitchhiker's Guide to Packaging <https://the-hitchhikers-guide-to-packaging.readthedocs.io/en/latest/creation.html>`_
- `Cookiecutter template for a Python package <https://github.com/audreyr/cookiecutter-pypackage>`_


License
-------

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

✨🍰✨

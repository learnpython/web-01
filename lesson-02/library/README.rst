============
Test Library
============

Test library which shows default structure of Python library.

Requirements
============

* `Python <http://www.python.org/>`_ 2.7

Installation
============

.. note:: Actually this doesn't work, just add note on how it should works.

To install, just::

    # pip install libraryname

Or install via::

    # python setup.py install

Testing
=======

Library ships with test project. To run test project you need to bootstrap it
with::

    $ make -C testproject/ bootstrap

and then run server with::

    $ make -C testproject/ server

and finally points browser to ``http://127.0.0.1:8080/`` to see results.

If you want to run test, you need to::

    $ make -C testproject/ test

after test project was successfully bootstrapped.

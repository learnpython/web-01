============
Test Project
============

Test project which shows default structure of Python project.

Requirements
============

* `Python <http://www.python.org/>`_ 2.7
* `Make <http://www.gnu.org/make>`_
* `bootstrapper <http://pypi.python.org/pypi/bootstrapper>`_

Installation
============

To install you need just to run::

    $ make bootstrap

and then place proper values to ``project/settings_local.py`` file.

Running
=======

To run project's HTTP server exec::

    $ make server

and point your browser to ``http://127.0.0.1:8080`` to see results.

Testing
=======

To run tests use::

    $ make test

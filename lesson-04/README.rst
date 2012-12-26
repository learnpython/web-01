============
Zapis Online
============

Requirements
============

* `Python <http://www.python.org/>`_ 2.7
* `virtualenv <http://virtualenv.org/>`_ 1.6 or higher
* `PIL <http://pypi.python.org/pypi/PIL>`_ 1.1.17
* `bootstrapper <http://pypi.python.org/pypi/bootstrapper>`_ 0.1 or higher

Installation
============

First you need to bootstrap project, with::

    $ bootstrapper

And then sync database with::

    (env)$ python manage.py sycndb

Running
=======

To run project, just execute::

    (env)$ python manage.py runserver_plus 8000

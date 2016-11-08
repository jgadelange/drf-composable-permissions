drf-composable-permissions
======================================

|build-status-image| |pypi-version|

Overview
--------

Compose your permission classes for django-rest-framework.

Requirements
------------

-  Python (2.7, (3.5, 3.6 (not in test suite))
-  Django (1.8, 1.10, 1.11)
-  Django REST Framework (3.4, 3.4, 3.6)

Installation
------------

Install using ``pip``\ …

.. code:: bash

    $ pip install drf-composable-permissions

Example
-------

When we want to create a permission class that allows read access to authenticated users and write access
to superusers we can use the following code:

.. code:: python

    from rest_framework.permissions import IsAuthenticated
    from drf_composable_permissions.p import P
    from drf_composable_permissions.permissions import IsReadOnly, IsSuperuser

    MyPermission = P(IsSuperuser) | (P(IsAuthenticated) & P(IsReadOnly))

Testing
-------

Install testing requirements.

.. code:: bash

    $ pip install -r requirements.txt

Run with runtests.

.. code:: bash

    $ ./runtests.py

You can also use the excellent `tox`_ testing tool to run the tests
against all supported versions of Python and Django. Install tox
globally, and then simply run:

.. code:: bash

    $ tox

Documentation
-------------

To build the documentation, you’ll need to install ``mkdocs``.

.. code:: bash

    $ pip install mkdocs

To preview the documentation:

.. code:: bash

    $ mkdocs serve
    Running at: http://127.0.0.1:8000/

To build the documentation:

.. code:: bash

    $ mkdocs build

.. _tox: http://tox.readthedocs.org/en/latest/

.. |build-status-image| image:: https://secure.travis-ci.org/jgadelange/drf-composable-permissions.svg?branch=master
   :target: http://travis-ci.org/jgadelange/drf-composable-permissions?branch=master
.. |pypi-version| image:: https://img.shields.io/pypi/v/drf-composable-permissions.svg
   :target: https://pypi.python.org/pypi/drf-composable-permissions

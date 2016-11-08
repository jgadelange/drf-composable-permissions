<div class="badges">
    <a href="http://travis-ci.org/jgadelange/drf-composable-permissions">
        <img src="https://travis-ci.org/jgadelange/drf-composable-permissions.svg?branch=master">
    </a>
    <a href="https://pypi.python.org/pypi/drf-composable-permissions">
        <img src="https://img.shields.io/pypi/v/drf-composable-permissions.svg">
    </a>
</div>

---

# drf-composable-permissions

Compose your permission classes for django-rest-framework.

---

## Overview

Compose your permission classes for django-rest-framework.

To compose a new `Permission` class to be used by the django rest framework views you have to wrap the original class in
a `P` class then can use the logical operators from python:
 
  - `~` (not)
  - `|` (or)
  - `&` (and)

This package also contains a few permission that can be used.

## Requirements

*  Python (2.7, (3.5, 3.6 (not in test suite))
*  Django (1.8, 1.10, 1.11)
*  Django REST Framework (3.4, 3.5, 3.6)

## Installation

Install using `pip`...

```bash
$ pip install drf-composable-permissions
```

## Example

When we want to create a permission class that allows read access to authenticated users and write access
to superusers we can use the following code:

```python
from rest_framework.permissions import IsAuthenticated
from drf_composable_permissions.p import P
from drf_composable_permissions.permissions import IsReadOnly, IsSuperuser

MyPermission = P(IsSuperuser) | (P(IsAuthenticated) & P(IsReadOnly))
```

## Testing

Install testing requirements.

```bash
$ pip install -r requirements.txt
```

Run with runtests.

```bash
$ ./runtests.py
```

You can also use the excellent [tox](http://tox.readthedocs.org/en/latest/) testing tool to run the tests against all supported versions of Python and Django. Install tox globally, and then simply run:

```bash
$ tox
```

## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```

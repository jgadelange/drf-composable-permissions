# DRF Composable Permissions

Compose your permission classes for django-rest-framework.

## Usage
To compose a new `Permission` class to be used by the django rest framework views you have to wrap the original class in
a `P` class then can use the logical operators from python:
 
  - `~` (not)
  - `|` (or)
  - `&` (and)

This package also contains a few permission that can be used.

For example, when we want to create a permission class that allows read access to authenticated users and write access
to superusers we can use the following code:

```
from rest_framework.permissions import IsAuthenticated
from drf_composable_permissions.p import P
from drf_composable_permissions.permissions import IsReadOnly, IsSuperuser

MyPermission = P(IsSuperuser) | (P(IsAuthenticated) & P(IsReadOnly))
```

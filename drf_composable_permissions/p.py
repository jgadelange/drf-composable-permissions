from __future__ import unicode_literals

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Composable(object):
    def __or__(self, other):
        return Or(self, other)

    def __and__(self, other):
        return And(self, other)

    def __invert__(self):
        return Not(self)

    def __call__(self):
        return self

    def __str__(self):
        return self.__repr__()


class Or(Composable):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def has_permission(self, request, view):
        return self.c1().has_permission(request, view) or \
            self.c2().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return self.c1().has_object_permission(request, view, obj) or \
            self.c2().has_object_permission(request, view, obj)

    def __repr__(self):
        return "({} or {})".format(
            self.c1(),
            self.c2()
        )


class And(Composable):
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def has_permission(self, request, view):
        return self.c1().has_permission(request, view) and \
            self.c2().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return self.c1().has_object_permission(request, view, obj) and \
            self.c2().has_object_permission(request, view, obj)

    def __repr__(self):
        return "({} and {})".format(
            self.c1(),
            self.c2()
        )


class Not(Composable):
    def __init__(self, c1):
        self.c1 = c1

    def has_permission(self, request, view):
        return not self.c1().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return not self.c1().has_object_permission(request, view, obj)

    def __repr__(self):
        return "!{}".format(
            self.c1()
        )


class P(Composable):
    def __init__(self, c1):
        self.c1 = c1

    def has_permission(self, request, view):
        return self.c1().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return self.c1().has_object_permission(request, view, obj)

    def __repr__(self):
        return type(self.c1()).__name__

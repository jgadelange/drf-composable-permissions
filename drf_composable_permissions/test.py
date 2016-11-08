from django.test import TestCase
from rest_framework.permissions import BasePermission

from drf_composable_permissions.p import P


class T(BasePermission):
    pass


class F(BasePermission):
    def has_permission(self, request, view):
        return False

    def has_object_permission(self, request, view, obj):
        return False


class PTest(TestCase):
    def test_identity(self):
        table = [
            (T, True),
            (F, False),
        ]

        for c1, outcome in table:
            combined = P(c1)
            self.assertEqual(combined.has_permission(None, None), outcome)
            self.assertEqual(combined.has_object_permission(None, None, None), outcome)

    def test_not(self):
        table = [
            (T, False),
            (F, True),
        ]

        for c1, outcome in table:
            combined = ~P(c1)
            self.assertEqual(combined.has_permission(None, None), outcome)
            self.assertEqual(combined.has_object_permission(None, None, None), outcome)

    def test_or(self):
        table = [
            (T, T, True),
            (T, F, True),
            (F, T, True),
            (F, F, False),
        ]

        for c1, c2, outcome in table:
            combined = P(c1) | P(c2)
            self.assertEqual(combined.has_permission(None, None), outcome)
            self.assertEqual(combined.has_object_permission(None, None, None), outcome)

    def test_and(self):
        table = [
            (T, T, True),
            (T, F, False),
            (F, T, False),
            (F, F, False),
        ]

        for c1, c2, outcome in table:
            combined = P(c1) & P(c2)
            self.assertEqual(combined.has_permission(None, None), outcome)
            self.assertEqual(combined.has_object_permission(None, None, None), outcome)

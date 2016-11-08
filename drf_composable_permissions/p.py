import inspect

from rest_framework.permissions import BasePermission


class P(BasePermission):
    OR = 'OR'
    AND = 'AND'
    NOT = 'NOT'
    IDENTITY = 'IDENTITY'

    def _run_operator(self, operator, f1, f2):
        if operator == self.IDENTITY:
            return f1()
        if operator == self.NOT:
            return not f1()
        if operator == self.OR:
            return f1() or f2()
        if operator == self.AND:
            return f1() and f2()

        raise NotImplementedError('Operator `{}` is not implemented.'.format(operator))

    def _build_function(self, name):
        # Encapsulate functions to have lazy evaluation
        def f(*args, **kwargs):
            def f1():
                return getattr(self.c1, name)(*args, **kwargs)

            def f2():
                return getattr(self.c2, name)(*args, **kwargs)
            return self._run_operator(self.operator, f1, f2)
        return f

    def __init__(self, c1, c2=None, operator=IDENTITY):
        self.c1 = c1() if inspect.isclass(c1) else c1
        self.c2 = c2() if inspect.isclass(c2) else c2
        self.operator = operator

        self.has_permission = self._build_function('has_permission')
        self.has_object_permission = self._build_function('has_object_permission')

    def __or__(self, other):
        return P(self, other, operator=self.OR)

    def __and__(self, other):
        return P(self, other, operator=self.AND)

    def __invert__(self):
        return P(self, operator=self.NOT)

    def __call__(self):
        return self

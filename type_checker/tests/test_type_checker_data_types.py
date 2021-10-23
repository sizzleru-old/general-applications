from __future__ import annotations

from unittest import TestCase, main
from constants import NoneType
from helper import type_error_message
from main import type_check

from numpy import random


class TestDataTypes(TestCase):
    def setUp(self: TestDataTypes) -> NoneType:
        self.debug = True
        self.START_RANGE = -1000
        self.END_RANGE = 1000
        self.RANGE = self.END_RANGE - self.START_RANGE
        self.SIZE = 100

    def test_numeric_type(self: TestDataTypes):
        @type_check(self.debug)
        def func_int(param_1: int) -> int:
            return param_1

        param_integer_list = [random.randint(self.START_RANGE, self.END_RANGE) for _ in range(self.SIZE)]

        for param_numeric in param_integer_list:
            try:
                func_int(param_numeric)
            except TypeError as context:
                self.fail("Unexpected TypeError with message: " + str(context))

        @type_check(self.debug)
        def func_float(param_1: float) -> float:
            return param_1

        param_float_list = [self.RANGE * random.rand() for _ in range(self.SIZE)]

        for param_float in param_float_list:
            try:
                func_float(param_float)
            except TypeError as context:
                self.fail("Unexpected TypeError with message: " + str(context))

        param_complex_list = [complex(self.RANGE * random.rand(), self.RANGE * random.rand()) for _ in range(self.SIZE)]

        @type_check(self.debug)
        def func_complex(param_1: complex) -> complex:
            return param_1

        for param_complex in param_complex_list:
            try:
                func_complex(param_complex)
            except TypeError as context:
                self.fail("Unexpected TypeError with message: " + str(context))


if __name__ == "__main__":
    main()

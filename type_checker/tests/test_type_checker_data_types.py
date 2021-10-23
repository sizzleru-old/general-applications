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
        self.SIZE = 100
        self.param_integer_list = random.randint(self.START_RANGE, self.END_RANGE, self.SIZE)
        self.param_float_list = (self.END_RANGE - self.START_RANGE) * random.random_sample(self.SIZE) + self.START_RANGE
        # self.param_complex_list =

    def test_numeric_type(self: TestDataTypes):
        @type_check(self.debug)
        def func_int(param_1: int) -> int:
            return param_1

        @type_check(self.debug)
        def func_float(param_1: float) -> float:
            return param_1

        for param_numeric in self.param_integer_list:
            try:
                func_int(int(param_numeric))
            except TypeError as context:
                self.fail("Unexpected TypeError with message: " + str(context))

        for param_float in self.param_float_list:
            try:
                func_float(float(param_float))
            except TypeError as context:
                self.fail("Unexpected TypeError with message: " + str(context))


if __name__ == "__main__":
    main()

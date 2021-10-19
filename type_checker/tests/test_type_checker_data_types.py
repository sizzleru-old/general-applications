from __future__ import annotations

from unittest import TestCase
import unittest

from constants import NoneType
from type_checker import type_check
from helper import type_error_message


class TestDataTypes(TestCase):
    def setUp(self: TestDataTypes) -> NoneType:
        self.debug = True
        self.param_int_1 = -17
        self.param_str_1 = "sizzle"

    def test_numeric_type(self: TestDataTypes):
        @type_check(self.debug)
        def func_int(param_1: int) -> int:
            return param_1

        try:
            func_int(self.param_int_1)
        except TypeError as context:
            self.fail("Unexpected TypeError with message: " + context.exception)

        """
        with self.assertRaises(TypeError) as context:
            func_int(self.param_str_1)
        self.assertEqual(type_error_message("param_1", self.param_str_1, int), str(context.exception))
        """


if __name__ == "__main__":
    unittest.main()

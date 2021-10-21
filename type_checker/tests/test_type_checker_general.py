from __future__ import annotations

from typing import Any
from unittest import TestCase
import unittest

from type_checker.constants import NoneType
from type_checker.main import type_check
from type_checker.validator import _validate_function, validator


class TestGeneral(TestCase):
    def setUp(self: TestGeneral) -> NoneType:
        self.debug = True

    def test_data_preservation(self: TestGeneral):
        @type_check(self.debug)
        def func_1(param_1):
            return param_1

        self.assertEqual(func_1(Any), Any)


if __name__ == "__main__":
    unittest.main()

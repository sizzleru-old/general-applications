from __future__ import annotations
from unittest import TestCase, main


class TestGeneral(TestCase):
    def setUp(self: TestGeneral):
        self.debug = True

    def test_data_preservation(self: TestGeneral):

        with self.assertRaises(TypeError):
            print("FUCK")
            raise TypeError()


if __name__ == "__main__":
    main()

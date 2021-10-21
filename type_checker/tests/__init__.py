from unittest import TestLoader, TextTestRunner

from type_checker.constants import NoneType


def run_all_tests() -> NoneType:
    """[searches all the tests of the form test*.py and runs it]

    Returns:
        NoneType: [None]
    """
    loader = TestLoader()
    suite = loader.discover(".")
    runner = TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    run_all_tests()

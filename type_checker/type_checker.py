from typing import Callable

from validator import _skip_validator, _validator


def type_check(run: bool = True) -> Callable[[Callable], Callable]:
    """[a decorator function for validating input and output parameters]

    Args:
        run (bool, optional): [can be set to false when the programing is not in debug mode]. Defaults to True.

    Returns:
        Callable[[Callable], Callable]: [a validator wrapper wrapper function]
    """
    return _validator if run else _skip_validator

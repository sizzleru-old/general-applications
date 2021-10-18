from typing import Any, Callable, Tuple, get_type_hints

from constants import RETURN_PARAMETER
from helper import _get_args


def _validator(func: Callable[..., Any]) -> Callable[..., Any]:
    """[validates the parameters using the wrapper function validator_wrapper]

    Args:
        func (Callable[..., Any]): [the subjected function]

    Returns:
        Callable[..., Any]: [returns a wrapper function that does the validation]
    """

    def validator_wrapper(*args: Tuple[Any], **kwargs: Tuple[Any]) -> Any:
        """[validates the values of the parameters of a function against the type hints provided]

        Returns:
            Any: [the original function return value]
        """
        parameter_values = _get_args(func, args, kwargs)
        parameter_type_hints = get_type_hints(func)
        return parameter_values[RETURN_PARAMETER]

    return validator_wrapper


def _skip_validator(func: Callable[..., Any]) -> Callable[[Any], Any]:
    """[returns the parameter value, acting as a function that skips the validation process]

    Args:
        func (Callable[..., Any]): [the subjected function]

    Returns:
        Callable[[Any], Any]: [the original function]
    """
    return func

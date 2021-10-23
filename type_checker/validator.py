from typing import Any, Callable, Dict, Tuple, get_type_hints

from constants import RETURN_PARAMETER
from helper import get_f_args, type_error_message
from valid_typing import valid_NormalType, valid_NewType


def _inspect_parameter(parameter_value: Any, parameter_type: Any) -> bool:
    params = parameter_value, parameter_type
    return valid_NormalType(*params) or valid_NewType(*params)


def _validate_function(parameter_values: Dict[str, Any], parameter_type_hints: Dict[str, Any]) -> Any:

    function_value = parameter_values[RETURN_PARAMETER]

    for parameter_name in parameter_type_hints:
        parameter_value = parameter_values[parameter_name]
        parameter_type_hint = parameter_type_hints[parameter_name]
        if not _inspect_parameter(parameter_value, parameter_type_hint):
            raise TypeError(type_error_message(parameter_name, parameter_value, parameter_type_hint))
    return function_value


def validator(func: Callable[..., Any]) -> Callable[..., Any]:
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
        parameter_values = get_f_args(func, args, kwargs)
        parameter_type_hints = get_type_hints(func)
        return _validate_function(parameter_values, parameter_type_hints)

    return validator_wrapper


def skip_validator(func: Callable[..., Any]) -> Callable[[Any], Any]:
    """[returns the parameter value, acting as a function that skips the validation process]

    Args:
        func (Callable[..., Any]): [the subjected function]

    Returns:
        Callable[[Any], Any]: [the original function]
    """
    return func

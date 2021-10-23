from typing import Any, Callable, Dict, List, Tuple, Type

from constants import RETURN_PARAMETER


def _get_input_args(func: Callable[..., Any], args: Tuple[Any], kwargs: Tuple[Any]) -> Dict[str, Any]:
    """[gets the input arguments of a given function]

    Args:
        func (Callable[..., Any]): [the subjected function]
        args (Tuple[Any]): [the positional argument values being extracted]
        kwargs (Tuple[Any]): [the keyword argument values being extracted]

    Returns:
        Dict[str, Any]: [a dictionary with the input parameter names as key, and their parameter values as the value]
    """
    args_names = func.__code__.co_varnames[: func.__code__.co_argcount]
    return {**dict(zip(args_names, args)), **kwargs}


def get_f_args(func: Callable[..., Any], args: Tuple[Any], kwargs: Tuple[Any]):
    """[gets both the input and output arguments of a given function]

    Args:
        func (Callable[..., Any]): [the subjected function]
        args (Tuple[Any]): [the positional argument values being extracted]
        kwargs (Tuple[Any]): [the keyword argument values being extracted]

    Returns:
        [type]: [a dictionary with the input and output parameter names as key, and their parameter values as the value]
    """
    args_value = _get_input_args(func, args, kwargs)
    args_value[RETURN_PARAMETER] = func(*args, **kwargs)
    return args_value


def _get_name(obj: Any):
    try:
        return obj.__name__
    except:
        return str(obj)


def type_error_message(parameter_name: str, parameter_value: Any, parameter_type_hint: Type):
    return (
        "Argument "
        + parameter_name
        + " is not of type "
        + _get_name(parameter_type_hint)
        + " (Got "
        + str(parameter_value)
        + " instead)"
    )


def switch(expression: Any, switch_cases: Dict[Any, Callable[[], Any]]) -> Any:
    return switch_cases[expression]


def type_hint_callable_to_list(type_hint: Tuple[List[Any], Any]) -> List[Any]:
    return type_hint.values()


def try_pass(func: Callable[..., Any], *args: Tuple[Any, ...], **kwargs: Tuple[Any, ...]) -> bool:
    try:
        func(*args, **kwargs)
        return True
    except:
        return False

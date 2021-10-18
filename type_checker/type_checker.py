from typing import Any, Callable, Dict, Tuple

RETURN_PARAMETER = "return"


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


def _get_args(func: Callable[..., Any], args: Tuple[Any], kwargs: Tuple[Any]):
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

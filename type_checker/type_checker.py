from typing import Any, Callable, Dict, Tuple, get_type_hints

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


def type_check(run: bool = True) -> Callable[[Callable], Callable]:
    """[a decorator function for validating input and output parameters]

    Args:
        run (bool, optional): [can be set to false when the programing is not in debug mode]. Defaults to True.

    Returns:
        Callable[[Callable], Callable]: [a validator wrapper wrapper function]
    """
    return _validator if run else _skip_validator

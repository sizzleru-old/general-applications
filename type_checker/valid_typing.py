from typing import Any, Callable, Type, get_args, get_type_hints
from constants import CALLABLE_INPUT_INDEX, CALLABLE_RETURN_INDEX, RETURN_PARAMETER
from helper import try_pass, type_hint_callable_to_list


def _try_is_instance(obj: Any, class_or_tuple: Type, type_extractor: Callable[[Any], Type] = type) -> bool:
    return (
        try_pass(isinstance, (obj, class_or_tuple))
        or try_pass(lambda obj: issubclass(type_extractor(obj), class_or_tuple), obj)
        or try_pass(lambda obj: type_extractor(obj) is class_or_tuple, obj)
    )


def valid_NormalType(parameter_value: Any, parameter_type: Any) -> bool:
    return _try_is_instance(parameter_value, parameter_type)


def valid_NewType(parameter_value: Any, parameter_type: Any) -> bool:
    return _try_is_instance(parameter_value, parameter_type, lambda new_type: new_type.__supertype__)


def valid_Callable(parameter_value: Any, parameter_type: Any) -> bool:
    callable_type_def = get_type_hints(parameter_value).values()
    callable_type_hint = get_args(parameter_type)

    return sum(
        [
            parameter_input_value is parameter_input_type_hint
            for parameter_input_value, parameter_input_type_hint in zip(
                callable_type_def[CALLABLE_INPUT_INDEX], callable_type_hint[CALLABLE_INPUT_INDEX]
            )
        ]
    )

from typing import Any, Type, Callable


def _try_is_instance(obj: Any, class_or_tuple: Type, type_extractor: Callable[[Any], Type] = type) -> bool:
    try:
        return isinstance(obj, class_or_tuple)
    except TypeError:
        pass
    try:
        return issubclass(type_extractor(obj), class_or_tuple)
    except TypeError:
        pass
    try:
        return type_extractor(obj) is class_or_tuple
    except TypeError:
        return False


def valid_NormalType(parameter_value: Any, parameter_type: Any) -> bool:
    return _try_is_instance(parameter_value, parameter_type)


def valid_NewType(parameter_value: Any, parameter_type: Any) -> bool:
    return _try_is_instance(parameter_value, parameter_type, lambda new_type: new_type.__supertype__)

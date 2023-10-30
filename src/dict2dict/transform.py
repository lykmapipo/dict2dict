"""Utilities to transform ``dict's``."""
from typing import Any, Dict, Type


__all__ = ["falsey_to_none"]


def _is_falsey(value: Type[Any]) -> Type[bool]:
    """Apply custom rule to check if value should not be considered as ``Falsey``.

    This implementation ignore:
        * ``False`` boolean value
        * ``0`` integer value
        * ``0.0`` float value
        * ``0j`` complex value
    """
    return (
        # boolean: False
        (isinstance(value, bool) and value is False)
        or
        # int: 0
        (isinstance(value, int) and value == 0)
        or
        # float: 0.0
        (isinstance(value, float) and value == 0.0)
        or
        # complex: 0j
        (isinstance(value, complex) and value == 0j)
    )


def _normalize_value(value: Type[Any]) -> Type[Any]:
    """Apply custom normalization to value before check if is ``Falsey``.

    This implementation handle:
        * ``"", " "`` string values
        * ``[], [None]`` list values
        * ``{}, {None}`` set values
        * ``(), (None, None)`` tuple values
    """
    # str: " "
    if isinstance(value, str):
        return value.strip()

    # list: [None]
    if isinstance(value, list):
        return [v for v in value if v]

    # set: {None}
    if isinstance(value, set):
        return {v for v in value if v}

    # TODO: more normalization rules

    # norule: return same value
    return value


def falsey_to_none(source: Dict[str, Any], **kwargs: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize ``Falsey`` items from a ``dict`` to ``None``.

    It takes a source ``dict``, if an item value contains a ``Falsey`` value,
    then, the item value is assigned to ``None``.

    This implementation ignore:
        * ``False`` boolean value
        * ``0`` integer value
        * ``0.0`` float value
        * ``0j`` complex value

    This implementation handle:
        * ``"", " "`` string values
        * ``[], [None]`` list values
        * ``{}, {None}`` set values
        * ``(), (None, None)`` tuple values

    Parameters
    ----------
    source (dict):
        Valid source dict.

    Returns
    -------
    result (dict):
        New normalized dict, else empty dict.

    Examples
    --------
    >>> from dict2dict import omit_falsey
    >>> a = { "a": 1, "b": [], }
    >>> b = falsey_to_none(a)
    >>> b == { "a": 1, "b": None, }
    True
    """
    result: Dict[str, Any] = {}  # normalized dict

    # limit dict only when normalizing
    if source and isinstance(source, dict):
        # transform each dict falsey value to ``None``
        for key, value in source.items():
            # if we should ignore value as falsey
            ignore = _is_falsey(value=value)

            # normalize value for falsey checks
            normalized_value = _normalize_value(value=value)

            # normalize dict falsey value to ``None``
            if not ignore and not normalized_value:
                result[key] = None

            # collect dict truey value
            else:
                result[key] = value

    # return dict with normalize falsey values
    return result

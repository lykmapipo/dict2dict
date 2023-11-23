"""Utilities to clean ``dict's``."""
from typing import Any, Dict

from .transform import falsey_to_none


__all__ = ["omit_falsey", "dict_to_dict"]


def omit_falsey(source: Dict[str, Any]) -> Dict[str, Any]:
    """Remove ``Falsey`` items from a ``dict``.

    It takes a source ``dict``, if an item contains a ``Falsey`` value,
    the item is removed from a ``dict``.

    Parameters
    ----------
    source (Dict[str, Any]):
        Valid source dict.

    Returns
    -------
    result (Dict[str, Any]):
        New dict with pythonic ``Truey`` values only, else empty dict.

    Examples
    --------
    >>> from dict2dict import omit_falsey
    >>> a = { "a": 1, "b": None, }
    >>> b = omit_falsey(a)
    >>> b == { "a": 1, }
    True
    """
    result: Dict[str, Any] = {}  # clean dict

    # collect truey items only from source dict
    if source and isinstance(source, dict):
        for key, value in source.items():
            if value:
                result[key] = value

    # return dict with truey values
    return result


def dict_to_dict(source: Dict[str, Any]) -> Dict[str, Any]:
    """Normalize and remove ``Falsey`` items from a ``dict``.

    It takes a ``dict``, normalize ``Falsey`` items to ``None``,
    and then, it remove ``Falsey`` items and retain only ``Truey`` items.

    Parameters
    ----------
    source (Dict[str, Any]):
        Variable ``dict's``.

    Returns
    -------
    dict (Dict[str, Any]):
        Valid dict

    Examples
    --------
    >>> from dict2dict import dict_to_dict
    >>> a = { "a": 1, "b": None, "c": [], }
    >>> b = dict_to_dict(a)
    >>> b == { "a": 1, }
    True
    """
    result: Dict[str, Any] = falsey_to_none(source=source)
    result = omit_falsey(source=result)
    return result

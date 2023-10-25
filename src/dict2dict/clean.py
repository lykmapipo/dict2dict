"""Utilities to clean ``dict's``."""
from typing import Any, Dict


__all__ = ["omit_falsey"]


def omit_falsey(source: Dict[str, Any]) -> Dict[str, Any]:
    """Remove ``Falsey`` items from a ``dict``.

    It takes a source ``dict``, if an item contains a ``Falsey`` value,
    the item is removed from a ``dict``.

    Parameters
    ----------
    source (dict):
        Valid source dict.

    Returns
    -------
    result (dict):
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

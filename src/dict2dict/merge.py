"""Utilities to merge multiple ``dict`` into single ``dict``."""
from typing import Any, Dict


__all__ = ["dicts2dict"]


def dicts2dict(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """Merge multiple ``dict`` into single ``dict``.

    It takes any number of ``dict``, merge them into a ``new dict``,
    precedence goes to key-value pairs in latter ``dict``.
    ``Falsey`` values have lower precedence over ``Truey`` values.

    Parameters
    ----------
    dicts (*dict):
        Variable ``dict's``.

    Returns
    -------
    dict (dict):
        Valid dict

    Examples
    --------
    >>> from dict2dict import dicts2dict
    >>> a = { "a": 1, "b": None, "c": None, }
    >>> b = { "b": 2, "c": None, }
    >>> c = dicts2dict(a, b)
    >>> print(c)
    { "a": 1, "b": 2, "c": None, }
    """
    falsey: Dict[str, Any] = {}  # falsey values
    truey: Dict[str, Any] = {}  # truey values
    result: Dict[str, Any] = {}  # merged values

    # collect truey and falsey values from source dicts
    for obj in dicts:
        # limit dict only when merging
        if obj and isinstance(obj, dict):
            # collect each dict falsey and truey items
            for k, v in obj.items():
                # collect truey valye
                if v:
                    truey[k] = v
                # collect falsey value
                else:
                    falsey[k] = v

    # merge falsey and truey values from sources dict
    result = {**falsey, **truey}

    # return merged values
    return result

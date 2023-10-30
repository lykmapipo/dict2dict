"""Utilities to merge multiple ``dict's`` into single ``dict``."""
from typing import Any, Dict


__all__ = ["dicts2dict"]


def dicts2dict(*sources: Dict[str, Any]) -> Dict[str, Any]:
    """Merge multiple ``dict`` into single ``dict``.

    It takes any number of ``dict``, merge them into a ``new dict``,
    precedence goes to key-value pairs in latter ``dict``.
    ``Falsey`` values have lower precedence over ``Truey`` values.

    Parameters
    ----------
    sources (*dict):
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
    >>> c == { "a": 1, "b": 2, "c": None, }
    True
    """
    falsey: Dict[str, Any] = {}  # falsey values
    truey: Dict[str, Any] = {}  # truey values
    result: Dict[str, Any] = {}  # merged values

    # collect truey and falsey values from source dicts
    for source in sources:
        # limit dict only when merging
        if source and isinstance(source, dict):
            # collect each dict falsey and truey values
            for k, v in source.items():
                # collect dict truey value
                if v:
                    truey[k] = v
                # collect dict falsey value
                else:
                    falsey[k] = v

    # merge falsey and truey values from source dicts
    result = {**falsey, **truey}

    # return merged dict values
    return result

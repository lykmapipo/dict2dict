"""Opinionated dictionary utilities for Python.

Examples
--------
- Merging multiple dictionaries to single dictionary
>>> from dict2dict import dicts2dict
>>> a = { "a": 1, "b": None, "c": None, }
>>> b = { "b": 2, "c": None, }
>>> c = dicts2dict(a, b)
>>> print(c)
{ "a": 1, "b": 2, "c": None, }
"""
from .merge import dicts2dict


__all__ = ["dicts2dict"]

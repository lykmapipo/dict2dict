"""Opinionated dictionary utilities for Python.

Examples
--------
- Normalize falsey items from a dictionary to ``None``
>>> from dict2dict import falsey_to_none
>>> a = { "a": 1, "b": [], }
>>> b = falsey_to_none(a)
>>> b == { "a": 1, "b": None, }
True


- Omit/Remove falsey items from a dictionary
>>> from dict2dict import omit_falsey
>>> a = { "a": 1, "b": None, }
>>> b = omit_falsey(a)
>>> b == { "a": 1, }
True


- Merging multiple dictionaries to single dictionary
>>> from dict2dict import dicts2dict
>>> a = { "a": 1, "b": None, "c": None, }
>>> b = { "b": 2, "c": None, }
>>> c = dicts2dict(a, b)
>>> c == { "a": 1, "b": 2, "c": None, }
True
"""
from .clean import omit_falsey
from .merge import dicts2dict
from .transform import falsey_to_none


__all__ = ["omit_falsey", "dicts2dict", "falsey_to_none"]

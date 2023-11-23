"""Opinionated dictionary utilities for Python.

Examples
--------
- Normalize ``Falsey`` items from a dictionary to ``None``
>>> from dict2dict import falsey_to_none
>>> a = { "a": 1, "b": [], }
>>> b = falsey_to_none(a)
>>> b == { "a": 1, "b": None, }
True


- Remove ``Falsey`` items from a dictionary
>>> from dict2dict import omit_falsey
>>> a = { "a": 1, "b": None, }
>>> b = omit_falsey(a)
>>> b == { "a": 1, }
True


- Normalize and remove ``Falsey`` items from a ``dict``
>>> from dict2dict import dict_to_dict
>>> a = { "a": 1, "b": None, "c": [], }
>>> b = dict_to_dict(a)
>>> b == { "a": 1, }
True


- Merging multiple dictionaries to single dictionary
>>> from dict2dict import dicts_to_dict
>>> a = { "a": 1, "b": None, "c": None, }
>>> b = { "b": 2, "c": None, }
>>> c = dicts_to_dict(a, b)
>>> c == { "a": 1, "b": 2, "c": None, }
True
"""
from .clean import dict_to_dict, omit_falsey
from .merge import dicts_to_dict
from .transform import falsey_to_none


__all__ = ["dict_to_dict", "dicts_to_dict", "falsey_to_none", "omit_falsey"]

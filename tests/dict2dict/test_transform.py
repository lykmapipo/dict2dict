"""Tests for transforming ``dict's``."""
from typing import Any, Dict, Tuple

import pytest

from dict2dict import falsey_to_none


@pytest.mark.parametrize(
    "source",
    [
        (None, {}),  # handled
        ({}, {}),  # handled
        ({"a": 1, "b": None}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": False}, {"a": 1, "b": False}),  # handled
        ({"a": 1, "b": 0}, {"a": 1, "b": 0}),  # handled
        ({"a": 1, "b": 0.0}, {"a": 1, "b": 0.0}),  # handled
        ({"a": 1, "b": 0j}, {"a": 1, "b": 0j}),  # handled
        ({"a": 1, "b": ""}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": " "}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": ()}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": (None)}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": ("c", None)}, {"a": 1, "b": ("c", None)}),  # ignored
        ({"a": 1, "b": []}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": [None]}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": {}}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": {None}}, {"a": 1, "b": None}),  # handled
        ({"a": 1, "b": {"c": None}}, {"a": 1, "b": {"c": None}}),  # handled
        (
            {"a": 1, "b": "b", "c": 2.0, "d": True, "e": 1j},
            {"a": 1, "b": "b", "c": 2.0, "d": True, "e": 1j},
        ),  # handled
        # # TODO: more falsey
    ],
)
def test_falsey_to_none(source: Tuple[Dict[str, Any], Dict[str, Any]]) -> None:
    """Test normalize dict falsey values to none."""
    dirty, expected = source

    clean = falsey_to_none(source=dirty)

    assert clean is not None
    assert isinstance(clean, dict)

    for key in expected.keys():
        assert clean[key] == expected[key]

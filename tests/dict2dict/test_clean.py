"""Tests for cleaning ``dict's``."""
from typing import Any, Dict, Tuple

import pytest

from dict2dict import omit_falsey


@pytest.mark.parametrize(
    "source",
    [
        (None, {}),  # handled
        ({}, {}),  # handled
        ({"a": 1, "b": None}, {"a": 1}),  # handled
        ({"a": 1, "b": False}, {"a": 1}),  # handled
        ({"a": 1, "b": 0}, {"a": 1}),  # handled
        ({"a": 1, "b": 0.0}, {"a": 1}),  # handled
        ({"a": 1, "b": 0j}, {"a": 1}),  # handled
        ({"a": 1, "b": ""}, {"a": 1}),  # handled
        ({"a": 1, "b": " "}, {"a": 1, "b": " "}),  # ignored
        ({"a": 1, "b": ()}, {"a": 1}),  # handled
        ({"a": 1, "b": (None)}, {"a": 1}),  # handled
        ({"a": 1, "b": ("c", None)}, {"a": 1, "b": ("c", None)}),  # ignored
        ({"a": 1, "b": []}, {"a": 1}),  # handled
        ({"a": 1, "b": [None]}, {"a": 1, "b": [None]}),  # ignored
        ({"a": 1, "b": {}}, {"a": 1}),  # handled
        ({"a": 1, "b": {None}}, {"a": 1, "b": {None}}),  # ignored
        ({"a": 1, "b": {"c": None}}, {"a": 1, "b": {"c": None}}),  # ignored
        (
            {"a": 1, "b": "b", "c": 2.0, "d": True, "e": 1j},
            {"a": 1, "b": "b", "c": 2.0, "d": True, "e": 1j},
        ),  # handled
        # TODO: more falsey
    ],
)
def test_omit_falsey(source: Tuple[Dict[str, Any], Dict[str, Any]]) -> None:
    """Test clean dict to remove falsey values."""
    dirty, expected = source

    clean = omit_falsey(source=dirty)

    assert clean is not None
    assert isinstance(clean, dict)

    for key in expected.keys():
        assert clean[key] == expected[key]

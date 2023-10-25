"""Tests for cleaning ``dict's``."""
from typing import Any, Dict, Tuple

import pytest

from dict2dict import omit_falsey


@pytest.mark.parametrize(
    "source",
    [
        (None, {}),
        ({}, {}),
        ({"a": 1, "b": None}, {"a": 1}),
        ({"a": 1, "b": False}, {"a": 1}),
        ({"a": 1, "b": 0}, {"a": 1}),
        ({"a": 1, "b": []}, {"a": 1}),
        ({"a": 1, "b": {}}, {"a": 1}),
        ({"a": 1, "b": ()}, {"a": 1}),
        (
            {"a": 1, "b": "b", "c": 2.0, "d": True},
            {"a": 1, "b": "b", "c": 2.0, "d": True},
        ),
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

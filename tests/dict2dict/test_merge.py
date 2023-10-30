"""Tests for merging multiple ``dict`` into single ``dict``."""
from typing import Any, Dict, List, Tuple

import pytest

from dict2dict import dicts_to_dict


@pytest.mark.parametrize(
    "sources",
    [
        ([None, None], {}),
        ([{}, {}], {}),
        (
            [
                {"a": 1, "b": None, "c": None},
                {"b": 2, "c": None},
            ],
            {"a": 1, "b": 2, "c": None},
        ),
    ],
)
def test_dicts_to_dict(sources: Tuple[List[Dict[str, Any]], Dict[str, Any]]) -> None:
    """Test merging dicts to dict."""
    raw_dicts, expected_dict = sources

    result_dict = dicts_to_dict(*raw_dicts)
    assert result_dict is not None
    assert isinstance(result_dict, dict)

    for k in expected_dict.keys():
        assert result_dict[k] == expected_dict[k]

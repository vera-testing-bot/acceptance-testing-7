"""Seed test, so a shard repo's CI has something to run."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app import add


def test_add() -> None:
    assert add(2, 3) == 5


@pytest.mark.parametrize("left,right", [(-1, 0), (0, -1), (1001, 0), (0, 1001)])
def test_add_rejects_out_of_range_values(left: int, right: int) -> None:
    with pytest.raises(ValueError):
        add(left, right)

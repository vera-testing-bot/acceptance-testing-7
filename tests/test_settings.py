"""Verify that an oversized settings file is rejected.

Mirrors Vera's documented behavior: a `.vera/settings.yaml` that exceeds the
10 KB limit is rejected and Vera falls back to defaults. These tests pin that
boundary so a regression (silently accepting an oversized file) is caught.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from shard_app.settings import (
    MAX_SETTINGS_BYTES,
    SettingsSizeError,
    validate_settings_size,
)


def test_settings_under_limit_is_accepted(tmp_path: Path) -> None:
    settings = tmp_path / "settings.yaml"
    settings.write_bytes(b"k: v\n")

    assert validate_settings_size(settings) is None


def test_settings_exactly_at_limit_is_accepted(tmp_path: Path) -> None:
    settings = tmp_path / "settings.yaml"
    settings.write_bytes(b"x" * MAX_SETTINGS_BYTES)

    assert validate_settings_size(settings) is None


def test_oversized_settings_file_is_rejected(tmp_path: Path) -> None:
    settings = tmp_path / "settings.yaml"
    settings.write_bytes(b"x" * (MAX_SETTINGS_BYTES + 1))

    with pytest.raises(SettingsSizeError):
        validate_settings_size(settings)


def test_rejection_reports_actual_and_limit_sizes(tmp_path: Path) -> None:
    settings = tmp_path / "settings.yaml"
    settings.write_bytes(b"x" * (MAX_SETTINGS_BYTES + 5))

    with pytest.raises(SettingsSizeError) as exc_info:
        validate_settings_size(settings)

    message = str(exc_info.value)
    assert str(MAX_SETTINGS_BYTES) in message
    assert str(MAX_SETTINGS_BYTES + 5) in message

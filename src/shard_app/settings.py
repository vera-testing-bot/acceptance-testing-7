"""Settings file size validation.

Vera rejects a `.vera/settings.yaml` that exceeds its size limit and falls
back to documented defaults. This module pins that boundary so a regression
(silently accepting an oversized file) is caught by tests.
"""

from __future__ import annotations

from pathlib import Path

MAX_SETTINGS_BYTES = 10 * 1024


class SettingsSizeError(ValueError):
    """Raised when a settings file exceeds the maximum allowed size."""


def validate_settings_size(path: Path, limit: int = MAX_SETTINGS_BYTES) -> None:
    """Reject a settings file whose byte size exceeds ``limit``.

    Returns ``None`` when the file is within the limit; raises
    :class:`SettingsSizeError` when it is too large.
    """
    size = Path(path).stat().st_size
    if size > limit:
        raise SettingsSizeError(
            f"settings file is {size} bytes which exceeds the {limit} byte limit"
        )

"""Trivial module so an acceptance shard repo has code to change."""

MIN_INPUT = 0
MAX_INPUT = 1000


def add(left: int, right: int) -> int:
    """Return the sum of two integers.

    Each argument must fall within the inclusive ``[MIN_INPUT, MAX_INPUT]``
    bounds; out-of-range values are rejected with ``ValueError``.
    """
    for name, value in (("left", left), ("right", right)):
        if not MIN_INPUT <= value <= MAX_INPUT:
            raise ValueError(
                f"{name}={value} is out of range [{MIN_INPUT}, {MAX_INPUT}]"
            )
    return left + right

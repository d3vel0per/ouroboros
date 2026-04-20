from __future__ import annotations

import pytest

from ouroboros.router import extract_first_argument


@pytest.mark.parametrize(
    ("remainder", "expected"),
    [
        pytest.param(None, None, id="none"),
        pytest.param("", None, id="empty"),
        pytest.param("   \t  ", None, id="whitespace"),
        pytest.param("seed.yaml --max-iterations 2", "seed.yaml", id="plain-token"),
        pytest.param('"seed file.yaml" --strict', "seed file.yaml", id="double-quoted"),
        pytest.param("'seed file.yaml' --strict", "seed file.yaml", id="single-quoted"),
        pytest.param(r"seed\ file.yaml --strict", "seed file.yaml", id="escaped-space"),
    ],
)
def test_extract_first_argument_returns_first_shell_style_argument(
    remainder: str | None,
    expected: str | None,
) -> None:
    assert extract_first_argument(remainder) == expected


def test_extract_first_argument_falls_back_to_whitespace_split_for_invalid_shell_syntax() -> None:
    assert extract_first_argument('"unterminated seed path.yaml --strict') == '"unterminated'

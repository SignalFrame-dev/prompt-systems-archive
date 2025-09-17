def to_verbatim(text: str) -> str:
    """Return text normalized for verbatim comparisons (no paraphrase tolerance)."""
    raise NotImplementedError

def enforce_label_order(items: list[tuple[str, str]], expected: list[str]) -> list[tuple[str, str]]:
    """Return items reordered to match expected labels; error if label missing/extra."""
    raise NotImplementedError

def to_decimal(x):
    """
    Accepts int/float/str and returns a float in [0.0, 1.0].

    Rules (you will implement):
    - If x > 1 or looks like "15" or "15%": interpret as percent (15 -> 0.15).
    - If 0 <= x <= 1: pass through (0.15 -> 0.15).
    - Reject negatives, booleans, and non-parsable strings by raising ValueError.
    """
    def to_decimal(x):
    # Reject booleans (bool is a subclass of int in Python)
    if isinstance(x, bool):
        raise ValueError("Booleans not allowed")

    # Handle numeric inputs
    if isinstance(x, (int, float)):
        if x < 0:
            raise ValueError("Negative values not allowed")
        if 0 <= x <= 1:
            return float(x)
        # placeholder: percent handling not yet implemented
        raise NotImplementedError("Percent handling to be added")

    # placeholder: string handling not yet implemented
    raise NotImplementedError("String handling to be added")


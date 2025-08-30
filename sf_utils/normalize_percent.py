def to_decimal(x):
    """
    Accepts int/float/str and returns a float in [0.0, 1.0].

    Rules (you will implement):
    - If x > 1 or looks like "15" or "15%": interpret as percent (15 -> 0.15).
    - If 0 <= x <= 1: pass through (0.15 -> 0.15).
    - Reject negatives, booleans, and non-parsable strings by raising ValueError.
    """
    raise NotImplementedError("Implement after tests are written.")

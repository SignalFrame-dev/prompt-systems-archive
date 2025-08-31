def to_decimal(x):
    """
    Convert input into a decimal between 0.0 and 1.0.

    Rules:
    - If x is a bool: reject with ValueError
    - If x is a number:
        * < 0 → ValueError
        * 0 <= x <= 1 → return float(x)
        * > 1 → interpret as percent (divide by 100)
    - If x is a string:
        * Strip spaces
        * If ends with %, remove the %
        * Try to convert to float
        * < 0 → ValueError
        * 0 <= v <= 1 → return v
        * > 1 → divide by 100
    - Otherwise: ValueError
    """

    # 1. Reject booleans
    if isinstance(x, bool):
        raise ValueError("Booleans not allowed")

    # 2. Numbers
    if isinstance(x, (int, float)):
        if x < 0:
            raise ValueError("Negative values not allowed")
        if 0 <= x <= 1:
            return float(x)
        return x / 100.0

    # 3. Strings
    if isinstance(x, str):
        s = x.strip()
        if not s:
            raise ValueError("Empty string not allowed")

        if s.endswith("%"):
            s = s[:-1].strip()

        try:
            v = float(s)
        except ValueError:
            raise ValueError("Non-numeric string")

        if v < 0:
            raise ValueError("Negative values not allowed")
        if v <= 1:
            return v
        return v / 100.0

    # 4. Unsupported types
    raise ValueError("Unsupported type")

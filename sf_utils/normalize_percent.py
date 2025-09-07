def to_decimal(x):
   """
Normalize an input into a decimal in [0.0, 1.0].

Accepted:
- int/float:
  * x < 0            → ValueError
  * 0 ≤ x ≤ 1        → float(x)
  * x > 1            → x / 100.0   (percent)
- str:
  * Trims spaces; optional trailing '%' allowed
  * Parses numeric content with float()
  * v < 0            → ValueError
  * 0 ≤ v ≤ 1        → v
  * v > 1            → v / 100.0   (percent)

Rejected:
- bool (explicitly) → ValueError
- Any other type    → ValueError
- Empty/non-numeric strings → ValueError
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
    raise ValueError(f"Unsupported type: {type(x).__name__}")


from sf_utils.normalize_percent import to_decimal

def test_pass_through_range():
    assert to_decimal(0.15) == 0.15
    assert to_decimal(1) == 1.0
    assert to_decimal(0) == 0.0

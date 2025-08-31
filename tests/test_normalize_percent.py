from sf_utils.normalize_percent import to_decimal

def test_pass_through_range():
    assert to_decimal(0.15) == 0.15
    assert to_decimal(1) == 1.0
    assert to_decimal(0) == 0.0

def test_percent_inputs():
    assert to_decimal(15) == 0.15
    assert to_decimal("15") == 0.15
    assert to_decimal("15%") == 0.15
    assert to_decimal("0.15") == 0.15

def test_rejections():
    try:
        to_decimal(True)
        assert False, "Expected ValueError for True"
    except ValueError:
        pass

    try:
        to_decimal(-1)
        assert False, "Expected ValueError for -1"
    except ValueError:
        pass

    try:
        to_decimal("abc")
        assert False, "Expected ValueError for 'abc'"
    except ValueError:
        pass

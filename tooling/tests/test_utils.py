import pytest
from signalframe.utils import to_verbatim, enforce_label_order

def test_to_verbatim_normalizes_quotes_and_spaces():
    raw = '  The Landlord must provide HVAC maintenance  twice  annually. '
    want = "The Landlord must provide HVAC maintenance twice annually."
    assert to_verbatim(raw) == want

def test_enforce_label_order_happy_path():
    items = [("Restrictions", "…"), ("Obligations", "…"), ("Renewal terms", "…")]
    expected = ["Obligations", "Restrictions", "Renewal terms"]
    out = enforce_label_order(items, expected)
    assert [k for k, _ in out] == expected

def test_enforce_label_order_missing_label_raises():
    items = [("Obligations", "x"), ("Restrictions", "y")]
    expected = ["Obligations", "Restrictions", "Renewal terms"]
    with pytest.raises(KeyError):
        enforce_label_order(items, expected)

def test_enforce_label_order_extra_label_raises():
    items = [("Obligations", "x"), ("Restrictions", "y"), ("Renewal terms", "z"), ("Other", "oops")]
    expected = ["Obligations", "Restrictions", "Renewal terms"]
    with pytest.raises(KeyError):
        enforce_label_order(items, expected)

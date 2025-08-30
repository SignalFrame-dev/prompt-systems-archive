# Test plan for to_decimal(x)
# Expected acceptances:
# - "15"    -> 0.15
# - "15%"   -> 0.15
# - 15      -> 0.15
# - 0.15    -> 0.15
# - "0.15"  -> 0.15
# - 1       -> 1.0
# - 0       -> 0.0
#
# Expected rejections (raise ValueError):
# - -1
# - "abc"
# - True / False

def test_placeholder_only():
    assert True

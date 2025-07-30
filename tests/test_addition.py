def addition(a, b):
    return a + b
print(addition(5, 3))  # Output: 8
def test_addition():
    assert addition(2, 3) == 5
    assert addition(-1, 1) == 0
    assert addition(0, 0) == 0
    assert addition(100, 200) == 300
    assert addition(-5, -5) == -10
from solutions.CHK import checkout_solution

def test_sum_a():
    assert 180 == checkout_solution.cost_a(4)
    assert 130 == checkout_solution.cost_a(3)
    assert 0 == checkout_solution.cost_a(0)

def test_sum_b():
    assert 45 == checkout_solution.cost_b(2)
    assert 75 == checkout_solution.cost_b(3)
    assert 0 == checkout_solution.cost_b(0)

def test_checkout():
    result = checkout_solution.checkout("B,A,A,A,A,B,B,C,D")
    expected = 290
    assert result == expected

from solutions.CHK import checkout_solution

def test_sum_a():
    assert 450 == checkout_solution.cost_a(11)
    assert 500 == checkout_solution.cost_a(12)
    assert 380 == checkout_solution.cost_a(9)
    assert 0 == checkout_solution.cost_a(0)

def test_sum_b():
    assert 45 == checkout_solution.cost_b(2, 0)
    assert 75 == checkout_solution.cost_b(3, 0)
    assert 75 == checkout_solution.cost_b(3, 1)
    assert 45 == checkout_solution.cost_b(3, 2)
    assert 45 == checkout_solution.cost_b(3, 3)
    assert 0 == checkout_solution.cost_b(0, 0)

def test_checkout():
    result = checkout_solution.checkout("BAAAABBCDEE")
    expected = 340
    assert result == expected
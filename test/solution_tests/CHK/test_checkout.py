from solutions.CHK import checkout_solution


def test_checkout():
    result = checkout_solution.checkout("B,A,A,A,A,B,B,C,D")
    expected = 290
    assert result == expected
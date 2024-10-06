from solutions.CHK import checkout_solution

def test_checkout():
    skus = ""
    skus += 9 * "A"  # 380
    skus += 2 * "B"  # 45
    skus += 3 * "E"  # 120 - 15 (1B)
    skus += 4 * "F"  # 30
    skus += 2 * "X"
    skus += 2 * "Z"  # 62

    cost = checkout_solution.checkout(skus)

    assert cost == 622

def test_checkout_invalid():
    skus = "ABC~"

    cost = checkout_solution.checkout(skus)

    assert cost == -1


from solutions.CHK import checkout_solution

import lib.solutions.CHK.offer


# def test_sum_a():
#     assert 450 == checkout_solution.cost_a(11)
#     assert 500 == checkout_solution.cost_a(12)
#     assert 380 == checkout_solution.cost_a(9)
#     assert 0 == checkout_solution.cost_a(0)
#
# def test_sum_b():
#     assert 45 == checkout_solution.cost_b(2, 0)
#     assert 75 == checkout_solution.cost_b(3, 0)
#     assert 75 == checkout_solution.cost_b(3, 1)
#     assert 45 == checkout_solution.cost_b(3, 2)
#     assert 45 == checkout_solution.cost_b(3, 3)
#     assert 0 == checkout_solution.cost_b(0, 2)
#     assert 0 == checkout_solution.cost_b(0, 0)
#
# def test_sum_f():
#     assert 10 == checkout_solution.cost_f(1)
#     assert 20 == checkout_solution.cost_f(2)
#     assert 20 == checkout_solution.cost_f(3)
#     assert 30 == checkout_solution.cost_f(4)
#     assert 80 == checkout_solution.cost_f(11)
#     assert 0 == checkout_solution.cost_f(0)
#
# def test_checkout():
#     result = checkout_solution.checkout("BAAAABBCDEEFFF")
#     expected = 360
#     assert result == expected
#
#

def test_checkout():
    skus = ""
    skus += 9 * "A"  # 380
    skus += 2 * "B"  # 45
    skus += 3 * "E"  # 120 - 15 (1B)
    skus += 4 * "F"  # 30
    skus += 2 * "Z"  # 100

    cost = checkout_solution.checkout(skus)

    assert cost == 690

def test_checkout_invalid():
    skus = "ABC~"

    cost = checkout_solution.checkout(skus)

    assert cost == -1

from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    sku_list = skus.split(",")

    total_skus = defaultdict(int)

    for sku in sku_list:
        if sku not in "ABCD":
            return -1
        total_skus[sku] += 1

    total_cost = 0

    # A cost
    total_cost += 130 * total_skus["A"] // 3
    total_cost += 50 * (total_skus["A"] - total_skus["A"] % 3)

    # B cost
    total_cost += 45 * total_skus["B"] // 2
    total_cost += 30 * (total_skus["B"] - total_skus["B"] % 2)

    # C cost
    total_cost += 20 * total_skus["C"]

    # D cost
    total_cost += 15 * total_skus["D"]

    return total_cost





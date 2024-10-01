from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

def cost_a(count: int) -> int:
    total_cost = 200 * (count // 5)
    total_cost += 130 * ((count % 5) // 3)
    total_cost += 50 * ((count % 5) % 3)
    return total_cost

def cost_b(count: int, count_e: int) -> int:
    # remove 1 count per 2 E
    count -= count_e // 2
    if count < 0:
        return 0
    total_cost = 45 * (count // 2)
    total_cost += 30 * ( count % 2)
    return total_cost

def checkout(skus: str) -> int:

    total_skus = defaultdict(int)

    for sku in skus:
        if sku not in "ABCDE":
            return -1
        total_skus[sku] += 1

    total_cost = 0

    # A cost
    total_cost += cost_a(total_skus["A"])

    # B cost
    total_cost += cost_b(total_skus["B"], total_skus["E"])

    # C cost
    total_cost += 20 * total_skus["C"]

    # D cost
    total_cost += 15 * total_skus["D"]

    # E cost
    total_cost += 40 * total_skus["E"]

    return total_cost



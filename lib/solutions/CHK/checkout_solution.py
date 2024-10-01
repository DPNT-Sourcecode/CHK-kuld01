from collections import defaultdict

# noinspection PyUnusedLocal
# skus = unicode string

def cost_a(count: int) -> int:
    total_cost = 130 * (count // 3)
    total_cost += 50 * (count % 3)
    return total_cost

def cost_b(count: int) -> int:
    total_cost = 45 * (count // 2)
    total_cost += 30 * ( count % 2)
    return total_cost

def checkout(skus: str) -> int:

    total_skus = defaultdict(int)

    for sku in skus:
        if sku not in "ABCD":
            return -1
        total_skus[sku] += 1

    total_cost = 0

    # A cost
    total_cost += cost_a(total_skus["A"])

    # B cost
    total_cost += cost_b(total_skus["B"])

    # C cost
    total_cost += 20 * total_skus["C"]

    # D cost
    total_cost += 15 * total_skus["D"]

    return total_cost

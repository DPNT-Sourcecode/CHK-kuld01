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

    total_skus[]




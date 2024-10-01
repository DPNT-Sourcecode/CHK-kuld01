

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    sku_list = skus.split(",")

    for sku in sku_list:
        if sku not in "ABCD":
            return -1



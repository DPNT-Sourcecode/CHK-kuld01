from collections import defaultdict
import attrs
from typing import Protocol, List, Dict
from lib.solutions.CHK import offer

# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus: str) -> int:

    for sku in skus:
        if sku not in "ABCDEF":
            return -1
        total_skus[sku] += 1

    offer_registry = offer.OfferRegistry(
    )

    offer_registry.calculate()

    return total_cost



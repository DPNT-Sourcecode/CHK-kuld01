from collections import defaultdict
import attrs
from typing import Protocol, List, Dict
from lib.solutions.CHK import offer

# noinspection PyUnusedLocal
# skus = unicode string

VALID_SKUS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def checkout(skus: str) -> int:

    for sku in skus:
        if sku not in VALID_SKUS:
            return -1

    offer_registry = offer.OfferRegistry(
        [
        offer.MultiBuyOffer(product_code="A", prices=[offer.Price(1, 50), offer.Price(3, 130), offer.Price(5, 200)]),
        ]
    )

    offer_registry.calculate()

    return total_cost

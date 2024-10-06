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
        [
        offer.MultiBuyOffer(product_code="A", prices=[offer.Price(1, 50), offer.Price(3, 130), offer.Price(5, 200)]),
        offer.MultiBuyOffer(product_code="A", prices=[offer.Price(1, 50), offer.Price(3, 130), offer.Price(5, 200)]),
        ]
    )

    offer_registry.calculate_cost()

    return total_cost


from collections import defaultdict
import attrs
from typing import Protocol, List, Dict
from . import offer
from .basket import Basket

# noinspection PyUnusedLocal
# skus = unicode string

VALID_SKUS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def checkout(skus: str) -> int:

    for sku in skus:
        if sku not in VALID_SKUS:
            return -1

    basket = Basket.from_string(skus)

    offer_registry = offer.OfferRegistry(
        [
        # chat gpt used to generate the offers list based on the table provided
        offer.MultiBuyOffer(product_code="A", prices=[offer.Price(1, 50), offer.Price(3, 130), offer.Price(5, 200)]),
        offer.MultiBuyOffer(product_code="B", prices=[offer.Price(1, 30), offer.Price(2, 45)]),
        offer.MultiBuyOffer(product_code="C", prices=[offer.Price(1, 20)]),
        offer.MultiBuyOffer(product_code="D", prices=[offer.Price(1, 15)]),
        offer.FreeCrossBuyOffer(product_code="E", price=40, free_product_code="B", trigger_quantity=2),
        offer.FreeBuyOffer(product_code="F", price=10, trigger_quantity=2),
        offer.MultiBuyOffer(product_code="G", prices=[offer.Price(1, 20)]),
        offer.MultiBuyOffer(product_code="H", prices=[offer.Price(1, 10), offer.Price(5, 45), offer.Price(10, 80)]),
        offer.MultiBuyOffer(product_code="I", prices=[offer.Price(1, 35)]),
        offer.MultiBuyOffer(product_code="J", prices=[offer.Price(1, 60)]),
        offer.MultiBuyOffer(product_code="K", prices=[offer.Price(1, 80), offer.Price(2, 150)]),
        offer.MultiBuyOffer(product_code="L", prices=[offer.Price(1, 90)]),
        offer.MultiBuyOffer(product_code="M", prices=[offer.Price(1, 15)]),
        offer.FreeCrossBuyOffer(product_code="N", price=40, free_product_code="M", trigger_quantity=3),
        offer.MultiBuyOffer(product_code="O", prices=[offer.Price(1, 10)]),
        offer.MultiBuyOffer(product_code="P", prices=[offer.Price(1, 50), offer.Price(5, 200)]),
        offer.MultiBuyOffer(product_code="Q", prices=[offer.Price(1, 30), offer.Price(3, 80)]),
        offer.FreeCrossBuyOffer(product_code="R", price=50, free_product_code="Q", trigger_quantity=3),
        offer.MultiBuyOffer(product_code="S", prices=[offer.Price(1, 30)]),
        offer.MultiBuyOffer(product_code="T", prices=[offer.Price(1, 20)]),
        offer.FreeBuyOffer(product_code="U", price=40, trigger_quantity=3),
        offer.MultiBuyOffer(product_code="V", prices=[offer.Price(1, 50), offer.Price(2, 90), offer.Price(3, 130)]),
        offer.MultiBuyOffer(product_code="W", prices=[offer.Price(1, 20)]),
        offer.MultiBuyOffer(product_code="X", prices=[offer.Price(1, 90)]),
        offer.MultiBuyOffer(product_code="Y", prices=[offer.Price(1, 10)]),
        offer.MultiBuyOffer(product_code="Z", prices=[offer.Price(1, 50)]),
        ]
    )

    return offer_registry.calculate(basket)

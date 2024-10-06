from collections import defaultdict
import attrs
from typing import Protocol, List, Dict
from collections import UserDict
# noinspection PyUnusedLocal
# skus = unicode string

class Basket(UserDict):
    def __setitem__(self, key, value):
        if value < 0:
            value = 0
        super().__setitem__(key, 0)



@attrs.define()
class Price:
    quantity: int
    price: int


class BuyOffer(Protocol):
    
    def calculate_cost(self, quantity: int) -> int:
        pass


@attrs.define()
class MultiBuyOffer:
    prices: List[Price]

    def calculate_cost(self, quantity: int) -> int:
        cost = 0
        self.prices.sort(key=lambda x: x.quantity, reverse=True)
        for price in self.prices:
            quantity_at_price = quantity // price.quantity
            cost += quantity_at_price * price.price
            quantity -= quantity_at_price * price.quantity
        return cost


@attrs.define()
class FreeBuyOffer:
    price: Price

    def calculate_cost(self, quantity: int) -> int:
        cost = price.price * (quantity - (quantity // price.quantity))
        return cost


@attrs.define()
class OfferRegistry:
    offers = Dict[str, BuyOffer]

    def calculate_cost(self, skus: dict) -> int:
        cost = 0
        for sku, quantity in skus.items():
            cost += self.offers[sku].calculate_cost(quantity)
        return cost


# def cost_a(quantity: int) -> int:
#     total_cost = 200 * (count // 5)
#     total_cost += 130 * ((count % 5) // 3)
#     total_cost += 50 * ((count % 5) % 3)
#     return total_cost
#
# def cost_b(quantity: int, count_e: int) -> int:
#     # remove 1 count per 2 E
#     count -= count_e // 2
#     if count < 0:
#         return 0
#     total_cost = 45 * (count // 2)
#     total_cost += 30 * ( count % 2)
#     return total_cost
#
# def cost_f(quantity: int) -> int:
#     total_cost = 10 * (count - (count // 3))
#     return total_cost

def checkout(skus: str) -> int:

    total_skus = defaultdict(int)

    for sku in skus:
        if sku not in "ABCDEF":
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

    # F cost
    total_cost += cost_f(total_skus["F"])

    return total_cost


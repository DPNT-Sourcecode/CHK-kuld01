from collections import defaultdict
import attrs
from typing import Protocol, List
# noinspection PyUnusedLocal
# skus = unicode string

@attrs.define()
class Price:
    quantity: int
    price: int


class BuyOffer(Protocol):
    
    def calculate_cost(self, quantity: int) -> int:
        pass

@attrs.define()
class SingleBuyOffer:
    single_price: int
    
    def calculate_cost(self, quantity: int) -> int:
        return self.single_price * quantity

@attrs.define()
class DoubleBuyOffer:
    single_price: int
    double_price: int
    
    def calculate_cost(self, quantity: int) -> int:
        cost = self.double_price * (count // 2)
        cost += self.single_price * ( count % 2)
        return cost


@attrs.define()
class TripleBuyOffer:
    single_price: int
    double_price: int
    triple_price: int
    

    def calculate_cost(self, quantity: int) -> int:
        cost = self.triple_price * (quantity // 5)
        cost += self.double_price * ((quantity % 5) // 3)
        cost += self.single_price * ((quantity % 5) % 3)
        return cost

@attrs.define()
class MultiBuyOffer:
    prices: List[Price]

    def calculate_cost(self, quantity: int) -> int:
        cost = 0
        prices_sorted = self.prices.sort(key=lambda x: x.quantity, reverse=True)
        print(self.prices[0].quantity)
        for price in prices_sorted:
            quantity_at_price = quantity // price.quantity
            cost += quantity_at_price * price.price
            quantity -= quantity_at_price
        return cost

class OfferRegistry:
    pass

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


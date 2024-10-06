from lib.solutions.CHK.basket import Basket
import attrs

from typing import List

@attrs.define()
class Price:
    quantity: int
    price: int

@attrs.define
class BuyOffer():
    product_code: str

    def _get_quantity(self, basket: Basket):
        return basket[self.product_code]

    def calculate_cost(self, basket: Basket) -> int:
        pass


@attrs.define()
class MultiBuyOffer(BuyOffer):
    prices: List[Price]

    def calculate_cost(self, basket: Basket) -> int:
        quantity = self._get_quantity(basket)
        cost = 0
        self.prices.sort(key=lambda x: x.quantity, reverse=True)
        for price in self.prices:
            quantity_at_price = quantity // price.quantity
            cost += quantity_at_price * price.price
            quantity -= quantity_at_price * price.quantity
        return cost


@attrs.define()
class FreeBuyOffer(BuyOffer):
    price: Price

    def calculate_cost(self, basket: Basket) -> int:
        quantity = basket[self.product_code]
        cost = self.price.price * (quantity - (quantity // self.price.quantity))
        return cost


@attrs.define()
class CrossBuyOffer(BuyOffer):
    price: Price
    free_product_code: str
    free_product_quantity_required: int

    def remove_free(self, basket: Basket) -> Basket:
        quantity = basket[self.product_code]
        basket[self.free_product_code] -= quantity // self.free_product_quantity_required
        return basket

    def calculate_cost(self, basket: Basket) -> int:
        quantity = basket[self.product_code]
        cost = self.price.price * (quantity - (quantity // self.price.quantity))
        return cost


@attrs.define()
class OfferRegistry:
    offers: List[BuyOffer]

    def calculate(self, basket: Basket) -> int:
        cost = 0

        for offer in self.offers:
            if isinstance(offer, CrossBuyOffer):
                basket = offer.remove_free(basket)

        for offer in self.offers:
            cost += offer.calculate_cost(basket)

        return cost




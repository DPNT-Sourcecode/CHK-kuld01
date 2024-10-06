from .basket import Basket
import attrs

from typing import List, Dict

@attrs.define()
class Price:
    quantity: int
    price: int

class Offer:

    def calculate_cost(self, basket: Basket) -> int:
        pass


@attrs.define
class BuyOffer(Offer):
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
    price: int
    trigger_quantity: int

    def calculate_cost(self, basket: Basket) -> int:
        quantity = basket[self.product_code]
        # divide into sets
        cost = self.trigger_quantity * self.price * (quantity // (self.trigger_quantity + 1))
        # calculate remainder
        cost += self.price * (quantity % (self.trigger_quantity + 1))
        return cost


@attrs.define()
class FreeCrossBuyOffer(BuyOffer):
    price: int
    free_product_code: str
    trigger_quantity: int

    def remove_free(self, basket: Basket) -> Basket:
        quantity = basket[self.product_code]
        basket[self.free_product_code] -= quantity // self.trigger_quantity
        return basket

    def calculate_cost(self, basket: Basket) -> int:
        quantity = basket[self.product_code]
        cost = self.price * quantity
        return cost



@attrs.define()
class CrossBuyOffer(Offer):
    products: Dict[str, int]
    trigger_quantity: int
    offer_price: int

    def calculate_cost(self, basket: Basket) -> int:

        total_quantity = 0
        for product_code in self.products:
            total_quantity += basket[product_code]
        cost = self.offer_price * (total_quantity // self.trigger_quantity)

        remaining_quantity = total_quantity % self.trigger_quantity

        # caclulate remaining quantity prices, favouring the customer
        prices = list(self.products.values())
        prices.sort()
        for price in prices:
            if remaining_quantity == 0:
                break
            cost += price
            remaining_quantity -= 1
        return cost


@attrs.define()
class OfferRegistry:
    offers: List[Offer]

    def calculate(self, basket: Basket) -> int:
        cost = 0

        for offer in self.offers:
            if isinstance(offer, FreeCrossBuyOffer):
                basket = offer.remove_free(basket)

        for offer in self.offers:
            cost += offer.calculate_cost(basket)

        return cost


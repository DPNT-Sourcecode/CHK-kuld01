from solutions.CHK import offer
from solutions.CHK.basket import Basket

import pytest

@pytest.fixture
def basket():
    instance = Basket()
    instance["A"] = 5
    instance["B"] = 3
    return instance

class TestBuyOffer:

    def test_get_quantity(self, basket):
        assert 5 == offer.BuyOffer("A")._get_quantity(basket)


class TestMultiBuyOffer:

    def test_calculate_cost(self, basket):
        basket["C"] = 11
        cost = offer.MultiBuyOffer(
            product_code="C",
            prices=[
                offer.Price(1, 50),
                offer.Price(3, 130),
                offer.Price(5, 200),
            ]
        ).calculate_cost(basket)
        assert cost == 450



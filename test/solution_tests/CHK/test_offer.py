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

    def test_calculate_cost_zero(self, basket):
        basket["C"] = 0
        cost = offer.MultiBuyOffer(
            product_code="C",
            prices=[
                offer.Price(1, 50),
                offer.Price(3, 130),
                offer.Price(5, 200),
            ]
        ).calculate_cost(basket)
        assert cost == 0

class TestFreeBuyOffer:

    def test_calculate_cost(self, basket):
        basket["C"] = 4
        cost = offer.FreeBuyOffer(
            product_code="C",
            price=50,
            trigger_quantity=2
        ).calculate_cost(basket)
        assert cost == 150

    def test_calculate_cost_zero(self, basket):
        basket["C"] = 0
        cost = offer.FreeBuyOffer(
            product_code="C",
            price=50,
            trigger_quantity=2
        ).calculate_cost(basket)
        assert cost == 0


class TestFreeCrossBuyOffer:

    def test_remove_free(self, basket):
        basket["C"] = 4
        basket["D"] = 3
        basket = offer.FreeCrossBuyOffer(
            product_code="C",
            price=50,
            free_product_code="D",
            trigger_quantity=2
        ).remove_free(basket)
        assert 1 == basket["D"]

    def test_calculate_cost(self, basket):
        basket["C"] = 4
        cost = offer.FreeCrossBuyOffer(
            product_code="C",
            price=50,
            free_product_code="D",
            trigger_quantity=2
        ).calculate_cost(basket)
        assert cost == 200

    def test_calculate_cost_zero(self, basket):
        basket["C"] = 0
        cost = offer.FreeCrossBuyOffer(
            product_code="C",
            price=50,
            free_product_code="D",
            trigger_quantity=2
        ).calculate_cost(basket)
        assert cost == 0



class TestCrossBuyOffer:

    def test_calculate_cost(self, basket):
        basket["C"] = 1
        basket["D"] = 2
        cost = offer.CrossBuyOffer(
            products={
                "C": 15,
                "D": 20
            },
            offer_price=25,
            trigger_quantity=2
        ).calculate_cost(basket)
        assert 40 == cost


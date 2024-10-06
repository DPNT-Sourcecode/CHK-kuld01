from solutions.CHK import offer, basket
import pytest

@pytest.fixture
def basket():
    instance = basket.Basket()
    instance["A"] = 5
    instance["B"] = 3

class TestBuyOffer:

    def test_get_quantity(self, basket):
        assert 5 == offer.BuyOffer("A")._get_quantity(basket)


class TestMultiBuyOffer:

    def test_get_quantity(self, basket):
        assert 5 == offer.BuyOffer("A")._get_quantity(basket)

from solutions.CHK import basket

class TestBasket:

    def test_default_value(self):
        instance = basket.Basket()
        assert instance['xyz123'] == 0

    def test_minimum_value(self):
        instance = basket.Basket()
        instance['key'] = -5
        assert instance['key'] == 0

    def test_changes(self):
        instance = basket.Basket()
        instance['key'] += 1
        instance['key'] -= 2
        instance['key'] += 1
        assert instance['key'] == 1

    def test_from_string(self):
        instance = basket.Basket.from_string("AAB")
        assert instance['A'] == 2
        assert instance['B'] == 1



from collections import UserDict

class Basket(UserDict):
    """Dict-like class where min value is 0 and default value is 0"""

    def __getitem__(self, key):
        if key not in self.data:
            return 0
        return super().__getitem__(key)

    def __setitem__(self, key, value):
        if value < 0:
            value = 0
        super().__setitem__(key, value)


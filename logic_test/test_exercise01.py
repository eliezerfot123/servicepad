import unittest
from exercise01 import Multiples 

class TestMultiples(unittest.TestCase):
    def test_fizz(self):
        for i in [3, 6, 9, 18]:
            assert Multiples(i) == 'fizz'

    def test_buzz(self):
        for i in [5, 10, 50]:
            assert Multiples(i) == 'buzz'

    def test_fizzbuzz(self):
        for i in [15, 30, 75]:

            assert Multiples(i) == 'fizzbuzz'
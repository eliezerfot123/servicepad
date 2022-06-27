import unittest
from exercise02 import fibonacci 

class TestFibonacci(unittest.TestCase):
    def testFibonacci1(self):
        self.assertEqual(6765, fibonacci(20), "Case1 unit test")
    
    def testFibonacci2(self):
        self.assertEqual(610, fibonacci(15), "Case2 unit test")

if __name__ == '__main__':
    unittest.main()
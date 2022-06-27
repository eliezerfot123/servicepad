import unittest
from exercise03 import repeatWord 

class RepeatWordTest(unittest.TestCase):
    def testCase1(self):
        phrase = "Hello Carmen, hello Marcos, hello pedro"
        self.assertEqual(
            {
                'hello':3,
                'carmen':1,
                'marcos': 1,
                'pedro': 1
            }, repeatWord(phrase),
            "Boila!, This fun"
        )

if __name__ == '__main__':
    unittest.main()
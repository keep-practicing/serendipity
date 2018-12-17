import unittest
from serendipity import sample2


class TestSample(unittest.TestCase):
    def test_sample(self):
        print("hello, world")
        self.assertEqual(sample2.sample2(), 1)


if __name__ == "__main__":
    unittest.main()

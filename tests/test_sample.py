import unittest
from serendipity import sample


class TestSample(unittest.TestCase):
    def test_sample(self):
        print("hello, world")
        self.assertEqual(sample.sample(), 10)


if __name__ == "__main__":
    unittest.main()

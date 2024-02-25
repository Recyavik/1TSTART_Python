import unittest
from module_example import add, multi

class TestMyModule(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(3, 5), 8)
        self.assertEqual(add(-3, 5), 2)

    def test_multi(self):
        self.assertEqual(multi(3, 5), 15)
        self.assertEqual((multi(-3, 5)), -15)

if __name__ == "__main__":
    unittest.main()
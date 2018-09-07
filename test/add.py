import unittest
from add import Add

class TestAdd(unittest.TestCase):
    def test_add(self):
        add = Add()
        self.assertEqual(add.add(1, 2), 3)
        self.assertEqual(add.add(2, -5), -3)
        self.assertEqual(add.add(2, 0), 2)

if __name__ == '__main__':
    unittest.main()

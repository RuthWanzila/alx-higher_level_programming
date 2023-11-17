import unittest
from base import Base

class TestBase(unittest.TestCase):

    def test_auto_increment_id(self):
        # Create multiple instances of Base
        base1 = Base()
        base2 = Base()
        base3 = Base()

        # Ensure that the IDs are unique
        self.assertNotEqual(base1.id, base2.id)
        self.assertNotEqual(base1.id, base3.id)
        self.assertNotEqual(base2.id, base3.id)

if __name__ == '__main__':
    unittest.main()

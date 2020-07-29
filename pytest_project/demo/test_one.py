import unittest


class Demo(unittest.TestCase):
    def test_addition(self):
      print("addition")
      assert 1 + 1 == 2


    def test_sub(self):
      print("substraction ")
      assert 5 - 3 == 2

    def test_mul(self):
        print("multiplication")
        assert 5 * 3 == 15

    def test_div(self):
        print("Division")
        assert 4 / 2 == 2
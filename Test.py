import unittest

from Prog1 import summation

class TestSum(unittest.TestCase) :
  def test_list_int(self) :
    """
    Test Case To Add Two Numbers
    """
    data = [32, 23]
    result = summation(data)
    self.assertEqual(result, 55)
    
if __name__ == '__main__' :
  unittest.main()

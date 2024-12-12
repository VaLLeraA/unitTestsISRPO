import unittest


def subtraction(a, b):
   return a-b

def multiplication(a,b):
   return a*b

class MathTestCase(unittest.TestCase):

   def test_subtraction(self):
      self.assertEqual(subtraction(1,2), -1)
      self.assertEqual(subtraction(2,-3), 5)
      self.assertEqual(subtraction(-5,-5), 0)
      self.assertEqual(subtraction(-5,2), -7)
      self.assertEqual(subtraction(3,0), 3)

   def test_multiplication(self):
      self.assertEqual(multiplication(1,2), 2)
      self.assertEqual(multiplication(2,-3), -6)
      self.assertEqual(multiplication(-5,-5), 25)
      self.assertEqual(multiplication(3,0), 0)


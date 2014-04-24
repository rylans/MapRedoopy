import unittest
import os
import sys

lib_path = os.path.abspath('../src')
sys.path.append(lib_path)

from mapredoopy import mappy

def square(x):
  return x*x

class TestSumOfSquares(unittest.TestCase):
  def test_wordcount_p1(self):
    seq = range(518)
    m = reduce(lambda x,y: x+y, mappy(square, seq, 1))
    r = reduce(lambda x,y: x+y, map(square, seq))
    assert m == r

  def test_wordcount_p4(self):
    seq = range(4232)
    m = reduce(lambda x,y: x+y, mappy(square, seq, 4))
    r = reduce(lambda x,y: x+y, map(square, seq))
    assert m == r

  def test_wordcount_p32(self):
    seq = range(7932)
    m = reduce(lambda x,y: x+y, mappy(square, seq, 32))
    r = reduce(lambda x,y: x+y, map(square, seq))
    assert m == r
    
if __name__ == '__main__':
  unittest.main()

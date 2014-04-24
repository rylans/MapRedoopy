import unittest
import os
import sys

lib_path = os.path.abspath('../src')
sys.path.append(lib_path)

from mapredoopy import mappy

def word_count(string):
  return len(string.split(' '))

class TestWordCount(unittest.TestCase):
  def setUp(self):
    self.lorem_text = ["lorem ipsum dolar sit amet, consectetur",
		  "adipiscing elit, sed do eiusmod tempor",
		  "incididunt ut labore et dolare magna aliqua."]
    self.lorem_result = reduce(lambda x,y: x+y, map(word_count, self.lorem_text))

  def test_wordcount_p1(self):
    m = reduce(lambda x,y: x+y, mappy(word_count, self.lorem_text, 1))
    assert m == self.lorem_result

  def test_wordcount_p4(self):
    m = reduce(lambda x,y: x+y, mappy(word_count, self.lorem_text, 4))
    assert m == self.lorem_result

  def test_wordcount_p32(self):
    m = reduce(lambda x,y: x+y, mappy(word_count, self.lorem_text, 32))
    assert m == self.lorem_result
    
if __name__ == '__main__':
  unittest.main()

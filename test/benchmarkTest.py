import datetime
import unittest
import os
import sys

lib_path = os.path.abspath('../src')
sys.path.append(lib_path)

from mapredoopy import mappy

def countTom(string):
  '''Return the number of occurences of the word 'Tom' in the string'''
  return sum([1 for i in string.split(' ') if "Tom" in i])

def add(x,y):
  return x+y

def benchmarkTest():
  '''Test whether asynchronous map or synchronous map is faster'''
  lines = open("book.txt").readlines()
  mappy_c = 0
  map_c = 0
  
  #Compute async map time on average
  before_mappy_t = datetime.datetime.now()
  for i in range(20):
    mappy_c += reduce(add, mappy(countTom, lines, 4))
  after_mappy_t = datetime.datetime.now()


  #Compute sync map time on average
  before_map_t = datetime.datetime.now()
  for i in range(20):
    map_c += reduce(add, map(countTom, lines))
  after_map_t = datetime.datetime.now()

  mappy_t = after_mappy_t - before_mappy_t
  map_t = after_map_t - before_map_t
  print "Async time: " + str(mappy_t)
  print "Sync time: " + str(map_t)

if __name__ == '__main__':
  benchmarkTest()

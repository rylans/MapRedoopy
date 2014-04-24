from multiprocessing import Pool
import itertools

def chunks(l, n):
  """ Return n lists of approximately equal size from l.
  """
  c = []
  m = int(len(l) / n)
  for i in range(0, n - 1):
    c.append(l[i*m:i*m + m])
  c.append(l[n*m - m:])
  return c

def mappy(f, lst, p):
  """ Split lst into p chunks and then do an async map with p processes.
  """
  pool = Pool(processes = p)
  partitions = chunks(lst, p)

  results = []
  for partition in partitions:
    rlist = []
    pool.map_async(f, partition, callback=rlist.append)
    results.append(rlist)
  pool.close()
  pool.join()

  return sum(sum(results, []),[])

def fun(x):
  return x*x

def word_count(string):
  return len(string.split(' '))

if __name__ == '__main__':
  print "'from mapredoopy import mappy' and then 'mappy(f, list, processes)'"

from multiprocessing import Pool
import itertools

def chunks(l, n):
  c = []
  for i in range(0, len(l), n):
    c.append(l[i:i+n])
  return c

def mappy(f, lst, p):
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

print mappy(fun, range(20), 4)

import multiprocessing
import os
def square(n):
  print("Worker process id for {0}: {1}".format(n, os.getpid()))
  return (n*n)
if __name__ == "__main__":
  mylist = [1,2,3,4]
  p = multiprocessing.Pool()
# map square function and the list of elements to work on to the process pool
  result = p.map(square, mylist)
  print(result)

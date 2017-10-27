import multiprocessing
def remove(balance, lock):
  lock.acquire()
  balance.value = balance.value - 1
  lock.release()
def add(balance, lock):
  lock.acquire()
  balance.value = balance.value + 1
  lock.release()
if __name__ == "__main__":
  # initial balance (a shared ressource exists in the shared memory)
  balance = multiprocessing.Value('i', 100)
  lock = multiprocessing.Lock()
  p1 = multiprocessing.Process(target=remove, args=(balance,lock))
  p2 = multiprocessing.Process(target=add, args=(balance,lock))
  p1.start()
  p2.start()
  print ("Final balance = {}".format(balance.value))

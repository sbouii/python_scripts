import multiprocessing 
def square_list(mylist, q):
 for num in mylist:
   q.put(num * num)

def print_queue(q):
   print ("Queue elements:")
   while not q.empty():
     print(q.get())
   print("Queue is now empty!")

if __name__ == "__main__":
    mylist = [1,2,3,4]
    # creating multiprocessing Queue
    q = multiprocessing.Queue()
    # creating new processes
    p1 = multiprocessing.Process(target=square_list, args=(mylist, q))
    p2 = multiprocessing.Process(target=print_queue, args=(q,))
    # running process p1
    p1.start()
    p1.join()
    # running process p2 
    p2.start()
    p2.join()

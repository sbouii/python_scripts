import multiprocessing
def sender(connection, msgs):
    """
    function to send messages to other end of pipe
    """
    for msg in msgs:
        connection.send(msg)
        print("Sent the message: {}".format(msg))
    connection.close()
def receiver(connection):
    """
    function to recieve messages from the other end of pipe
    """
    while 1:
        msg = connection.recv()
        if msg == "END":
            break
        print("Received the message: {}".format(msg))
if __name__ == "__main__":
    # messages to be sent 
    msgs = ["Hi", "process", "keep", "working!"]
    #creating a pipe 
    parent_connection, child_connection = multiprocessing.Pipe()
    
    # creating new processes
    p1 = multiprocessing.Process(target=sender, args=(parent_connection,msgs))
    p2 = multiprocessing.Process(target=receiver, args=(child_connection,)) 
    # running processes
    p1.start()
    p2.start()
    # wait until process finish
    p1.join()
    p2.join() 

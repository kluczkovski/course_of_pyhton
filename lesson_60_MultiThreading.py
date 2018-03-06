import time
from threading import Thread
def myFunction(i):
    print("Sleeping 5 second %d " %i)
    time.sleep(5)
    print("Finished sleeping %d \n" %i)



for i in range(4):
    mythread = Thread(target=myFunction, args=(i,))
    mythread.start()


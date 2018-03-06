from threading import Thread

def myFactorial(n):

    if n < 1:
        return 1
    else:
        myReturnNumber = n * myFactorial(n - 1)
        print(str(n) + "! = " + str(myReturnNumber) + "\n")
        return myReturnNumber


myThread_01 = Thread(target=myFactorial, args=(20,))
myThread_02 = Thread(target=myFactorial, args=(19,))
myThread_01.start()
myThread_02.start()
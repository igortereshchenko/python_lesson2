from threading import  Thread
import random
import time

class MyThread(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name


    def run(self):
        amount = random.randint(1,5)
        time.sleep(amount)
        print(self.name, amount)

if __name__=="__main__":
    for i in range(10):
        thread = MyThread("Thread "+ str(i))
        thread.start()
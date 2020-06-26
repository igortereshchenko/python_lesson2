from threading import Thread
import random
import time


def thread_delay(name, delay, smth):
    count = 0
    while count<4:
        time.sleep(delay)
        count+=1
        print(name, count)


class MyThread(Thread):

    def __init__(self, name, smth):
        Thread.__init__(self)
        self.name = name
        self.__smth=smth


    def run(self):
        thread_delay(self.name, random.randint(1,3), self.__smth)

if __name__=="__main__":
    for i in range(3):
        thread = MyThread("Thread "+ str(i),None)
        thread.start()
        if i%2==0:
            thread.join()
        print("End")
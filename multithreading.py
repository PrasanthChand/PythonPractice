# multithreading

from threading import *
from time import sleep


class A(Thread):
    def run(self):
        for i in range(5):
            print('A')
            sleep(1)


class B(Thread):
    def run(self):
        for i in range(5):
            print('B')
            sleep(1)


thread1 = A()
thread2 = B()
thread1.start()
sleep(0.1)
thread2.start()
sleep(0.1)
thread1.join()
thread2.join()

print('end of program')

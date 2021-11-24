#!/bin/python

import threading
import random
from time import sleep


def random_numbers():
    global a
    while True:
        sleep(1)
        a = random.randint(1,100)
        print("random number = {}".format(a))

def print_cube():
    while True:
        sleep(1)
        print("Cube: {}".format(a*a*a))

def print_square():
    while True:
        sleep(1)
        print("Square: {}".format(a*a))


if __name__ == "__main__":
    a = 0
    t1 = threading.Thread(target=random_numbers)
    t2 = threading.Thread(target=print_cube)
    t3 = threading.Thread(target=print_square)

    t1.start()
    t2.start()
    t3.start()


    t1.join()
    t2.join()
    t3.join()


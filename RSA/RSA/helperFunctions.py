from methoden import *
import random

def euclid(a,b):
    c = a
    d = b
    while(c != 0 and d != 0):
        if(c > d):
            c = c - d
        else:
            d = d - c
    if(c != 0):
        return c
    else:
        return d
    
def check_prime(number):
    return

def rand_prime():
    while True:
        p = random.randrange(10001, 100000, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p
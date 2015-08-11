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

#take positive integers a, b, and return a triple (g, x, y),
#such that ax + by = g = gcd(a, b).
def extended_euclid(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y

def check_prime(number):
    
    return

def rand_prime():
    while True:
        p = random.randrange(10001, 100000, 2)
        if all(p % n != 0 for n in range(3, int((p ** 0.5) + 1), 2)):
            return p

def generateKeys():
    p = rand_prime()
    q = rand_prime()
    while p==q:
        q=rand_prime()

    N = p*q
    phiN = (p-1)*(q-1)

    e=0

    for el in range(10000,20000):
        if euclid(el, phiN) == 1:
            e=el
            break
    if e==0:
        print("!!! e==0")

    temp = extended_euclid(e, phiN)#1 = e*d + phiN * t
    d = temp[1]
    while d<=0:
        d = d+phiN

    publicKey = e
    privateKey = N

    return publicKey, privateKey
#! /usr/bin/env python
from __future__ import division
from math import floor
from random import choice

def get_birth():
    return choice(range(365))

def is_success(xs):
    for x in range(23):
        for y in range(x+1, 23):
            if(xs[x]== xs[y]):
                return True
    return False

def result(times=10000):
    count=0
    for i in range(times):
        #get 23 birth days
        births = list()
        for j in range(23):
            births.append(get_birth())
        if(is_success(births)):
            count+=1
    print count/times

result()

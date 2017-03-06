#!/usr/bin/env python
from math import factorial

def solution(total):
    for i in range(total/1):
        for j in range(total/2):
            for k in range(total/3):
                if i+2*j+3*k == total:
                  yield (i,j,k)

def final(total):
    results=0
    for xs in solution(total):
       result= factorial(sum(xs))
       for x in xs:
           result/= factorial(x)
       results+=result
    return results

if __name__=='__main__':
    print final(15)

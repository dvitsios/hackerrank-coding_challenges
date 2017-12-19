#!/bin/python3

import sys

def lonely_integer(a):
    
    d = {}
    
    for i in a:
        d[i] = d.get(i, 0) + 1
        
    for k,v in d.items():
        if v == 1:
            return k

n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))

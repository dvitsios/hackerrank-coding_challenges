#!/bin/python3

import sys

def lonely_integer(a):
    
    lonely = 0
    for i in a:
        lonely ^= i
    
    return lonely
        
n = int(input().strip())
a = [int(a_temp) for a_temp in input().strip().split(' ')]
print(lonely_integer(a))
 
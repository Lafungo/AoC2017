# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:03:11 2017

@author: Lafungo
"""

def maze(a):
    p = 0
    s = 0
    
    while p >= 0 and p < len(a):
        j = a[p]
        if j >= 3:
            a[p] -= 1
        else:
            a[p] += 1
        p += j
        s += 1
    
    return s

if __name__ == '__main__':
    with open('d5_input.txt') as f:
        a = []
        
        for line in f:
            a.append(int(line))
            
        print(maze(a))

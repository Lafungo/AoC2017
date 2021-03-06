# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:25:10 2017

@author: Lafungo
"""

def blocks(a):
    s = []
    
    while a not in s:
        s.append(list(a))
        
        m = max(a)
        l = len(a)
        
        for i in range(l):
            if a[i] == m:
                a[i] = 0
                break
            
        j = (i + 1) % l
        while m > 0:
            a[j] += 1
            j = (j + 1) % l
            m -= 1
    
    for k in range(len(s)):
        if a == s[k]:
            return len(s) - k

if __name__ == '__main__':
    with open('d6_input.txt') as f:
        a = []
        
        for line in f:
            for n in line.split('\t'):
                a.append(int(n))
                
        print(blocks(a))
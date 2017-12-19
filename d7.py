# -*- coding: utf-8 -*-
"""
Created on Tue Dec 19 10:15:05 2017

@author: Lafungo
"""

w = dict()
s = dict()

with open('d7_input.txt') as f:
    for line in f:
        l = line.strip().split(' ')
        t = []
        t.append(l[0])
        t.append(int(l[1][1:-1]))
        
        if len(l) > 2:
            for i in range(3, len(l)):
                t.append(l[i].rstrip(','))
                
        w[t[0]] = t[1]
        s[t[0]] = t[2:]
        
b = t[0]
found = False

while not found:
    found = True
    
    for k, v in s.items():
        if b in v:
            b = k
            found = False
            
print(b)
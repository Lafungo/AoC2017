# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 08:45:00 2017

@author: Lafungo
"""

def validate(p):
    t = p.strip().split(' ')
    s = set()
    
    for w in t:
        s.add(tuple(sorted(list(w))))
    
    if len(t) < 2:
        return False
    
    if len(s) == len(t):
        return True
    else:
        return False
    
if __name__ == '__main__':
    with open('d4_input.txt') as f:
        s = 0
        
        for line in f:
            if validate(line):
                s += 1
                
        print(s)

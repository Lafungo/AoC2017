# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 15:58:55 2017

@author: Lafungo
"""

import csv

with open('d2_input.txt', newline='') as f:
    r = csv.reader(f, delimiter='\t')
    s = 0
    
    for row in r:
        a = []
        done = False
        
        for e in row:
            n = int(e)
            
            for m in a:
                if n <= m and m % n == 0:
                    s += m // n
                    done = True
                    break
                elif m <= n and n % m == 0:
                    s += n // m
                    done = True
                    break
            
            if not done:
                a.append(n)
                    
            if done:
                break

print(s)
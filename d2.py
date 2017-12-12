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
        m = -1
        M = -1
        
        for e in row:
            n = int(e)
            if m < 0 or n < m:
                m = n
            if M < n:
                M = n
            
        s += M - m

print(s)
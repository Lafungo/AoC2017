# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 08:40:34 2017

@author: Lafungo
"""

def dist(n):
    if n == 1:
        return 0
    
    i = 1
    
    while (i + 2)**2 < n:
        i += 2
        
    d = i // 2 # minimum distance
    m = n - i**2
    
    # switch per quadrant (based on diagonal axes)
    if m <= i + 1:
        d += abs(m - d)
    elif m <= 2 * (i + 1):
        m -= i + 1
        d += abs(m - d)
    elif m <= 3 * (i + 1):
        m -= 2 * (i + 1)
        d += abs(m - d)
    else:
        m -= 3 * (i + 1)
        d += abs(m - d)
        
    return d

if __name__ == '__main__':
    while True:
        try:
            n = int(input('Enter a positive integer: '))
            
            if n > 0:
                d = dist(n)
                print(d)
                break
            else:
                print('Invalid input. Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a positive integer.')
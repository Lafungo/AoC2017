# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 08:40:34 2017

@author: Lafungo
"""

def position(n):
    if n == 1:
        return (0, 0)
    
    i = 1
    
    while (i + 2)**2 < n:
        i += 2
    
    d = i // 2 # square on diagonal at (d, -d)
    m = n - i**2
    
    # switch per quadrant (based on diagonal axes)
    if m <= i + 1:
        x = d + 1
        y = (m - 1) - d
    elif m <= 2 * (i + 1):
        m -= i + 1
        x = d + 1 - m
        y = d + 1
    elif m <= 3 * (i + 1):
        m -= 2 * (i + 1)
        x = -(d + 1)
        y = d + 1 - m
    else:
        m -= 3 * (i + 1)
        x = -(d + 1) + m
        y = -(d + 1)
        
    return (x, y)
        

def sum_alloc(n):
    a = dict()
    a[(0, 0)] = 1
    
    for k in range(2, n + 1):
        s = 0
        x, y = position(k)
        neighbors = [(i, j) for i in [x + m for m in range(-1, 2)]
                            for j in [y + m for m in range(-1, 2)]]
        
        for neighbor in neighbors:
            if neighbor in a:
                s += a[neighbor]
        
        a[(x, y)] = s
    
    return a[position(n)]

if __name__ == '__main__':
    while True:
        try:
            n = int(input('Enter a positive integer: '))
            
            if n > 0:
                d = sum_alloc(n)
                print(d)
                break
            else:
                print('Invalid input. Please enter a positive integer.')
        except ValueError:
            print('Invalid input. Please enter a positive integer.')
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 16:44:04 2017

@author: Lafungo
"""

from math import floor, log

def digit(n, d): # 0-indexed
    return (n // 10**d) % 10

def captcha(n):
    try:
        n = int(n)
        s = 0
        e = floor(log(n, 10) + 1)
        
        for k in range(e, 0, -1):
            if digit(n, k - 1) == digit(n, (k - 2) % e):
                s += digit(n, k - 1)
                
        return s
    except ValueError:
        print('Please enter a sequence of digits.')

if __name__ == '__main__':
    while True:
        try:
            n = int(input('Enter a sequence of digits: '))
            if n > 0:
                s = captcha(n)
                print(s)
                break
            else:
                print('Invalid input. Please enter a sequence of digits.')
        except ValueError:
            print('Invalid input. Please enter a sequence of digits.')

#!/usr/bin/env python3

number = int(input('insert a number: '))

try:
    if number % 2 == 0:
        print('this number is even!')
    else:
        print('this number is odd!')
except:
    print(':(')

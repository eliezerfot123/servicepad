#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eliezer Romero
# @Date:   2022/6/23 17:49
# output:_ 5 function calls in 0.000 seconds

'''
For this exercice number two:
The sequence begins with the numbers 0 and 1; 
from these, "each term is the sum of the two previous ones", 
this is the recurrence relation that defines it. (Wikipedia)

if  you want show range number for this  fibonacci sequence
you should exec the next funtion: 
fibonacci(number) for number in range(18) and this show you the number serie

This code will resolve mentioned series 
for each number entered in its variable "number" 
or in a given range.

'''

def fibonacci(number):
    values = {0: 0, 1: 1}
    if number in values:  
        return values[number]
    # Compute and cache the Fibonacci number
    values[number] = fibonacci(number - 1) + fibonacci(number - 2)  # Recursive case
    return values[number]


print(fibonacci(15))
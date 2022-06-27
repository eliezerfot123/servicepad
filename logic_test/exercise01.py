#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Eliezer Romero
# @Date:   2022/6/23 15:27
# output:_ 104 function calls in 0.001 seconds

def Multiples(number):
    for i in range(1, number+1):
        map = "fizz"*(i%3<1)+(i%5<1)*"buzz" or i
        print(map)
    return map


if __name__ == '__main__':
    Multiples(100)
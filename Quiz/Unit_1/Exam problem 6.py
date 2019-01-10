#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 23:06:21 2018

@author: smrikva
"""
import numpy as np

def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    result = []
    falseRes = []
    for choice in range(2**len(choices)):
        binChoice = bin(choice)[2:]
        binChoice = '0'*(len(choices)-len(binChoice)) + binChoice
        binChoice = np.array([int(i) for i in binChoice])
        sumBin = sum(binChoice*choices)
        if sumBin == total:
             result.append(binChoice)
        elif sumBin < total:
            falseRes.append((binChoice, sumBin-total))
            
    if len(result)==0:
        falseRes.sort(key=lambda x: x[1], reverse=True)
        return falseRes[0][0]
    
    if len(result)==1:
        return result[0]
    sums = [sum(r) for r in result]
    return result[sums.index(min(sums))]        

        

choices = [1,2,2,3]
total = 4
find_combination(choices, total)

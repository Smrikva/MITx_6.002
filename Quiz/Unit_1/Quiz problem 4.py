#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 19:17:47 2018

@author: smrikva
"""
'''
def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    nums = L.copy()
    maxSum = 0
    
    for i in range(len(nums)):
        if maxSum < sum(nums[i:]):
            maxSum = sum(nums[i:]) 
    
    nums.reverse()
    for i in range(len(nums)):
       if maxSum < sum(nums[i:]):
           maxSum = sum(nums[i:])     
    
    return maxSum
'''    



def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    
    sums = []
    nums = L.copy()

    while True:
        if nums[0]<=0:
            nums.pop(0)
        else:
            break
        
    while True:
        if nums[-1]<=0:
            nums.pop(-1)
        else:
            break

    lenNums = len(nums)
    for i in range(0, lenNums+1):
        for j in range(i+1, lenNums+1):
            sums.append(sum(nums[i:j]))
    
    return max(sums)



a =[1,-2,3,-4]

print(max_contig_sum(a))
















#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 16 04:22:03 2018

@author: smrikva
"""
import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    balls = [1,1,1,0,0,0]    
    random.shuffle(balls)
    success = 0
    for i in range(numTrials):
        pick3 = [balls[i] for i in random.sample(range(0,5), 3)]
        if pick3.count(pick3[0]) == 3: success += 1
    return success/float(numTrials)

# ONE LINER

#def noReplacementSimulation(n): 
#return sum(sum(random.sample((0,0,0,-3,-6,9),3))==0 for n in range(n)) / n
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 20:42:54 2018

@author: smrikva
"""
import random 
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    sameColors = 0
    for i in range(numTrials):
        balls = [1,1,1,1,0,0,0,0]
        random.shuffle(balls)
    
        picks = set()
        for j in range(3):
            picks.add(balls.pop(random.randint(0,len(balls)-1)))
        if len(picks)==1:
            sameColors += 1
    return sameColors/float(numTrials)
drawing_without_replacement_sim(10)
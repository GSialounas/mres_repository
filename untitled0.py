#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 11:27:20 2018

@author: gs1511
"""
import numpy as np

x = [i for i in range(2,8)]
s = np.zeros(len(x))

for i in x:
    for j in range(1,10**i+1):
        s[i-2]+=1/j
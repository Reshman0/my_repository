# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:24:53 2022

@author: Bekir Berk YILDIRIM
"""
def removNb(n):
    result = []
    sequence_sum = n * (n + 1) // 2
    for x in range(1, n + 1):
        y = (sequence_sum - x) // (x + 1)
        if y <= n and x * y == (sequence_sum - x - y):
            result.append((x, y))
    return result
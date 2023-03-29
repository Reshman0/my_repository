 # -*- coding: utf-8 -*-
"""
Created on Sun Nov  6 19:45:56 2022

@author: Bekir Berk YILDIRIM
"""

def find_needle(haystack):
    # your code here
    needle='needle'
    counter=0
    for x in haystack:
        counter=counter+1
        if x==needle:
            break
    output='found the needle at position '+str(counter)
    return output


s = find_needle(['jjfgkd','dfhksıfu','needle'])
print(s)

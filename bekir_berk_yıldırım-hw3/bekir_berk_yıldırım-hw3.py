# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 12:38:22 2023

@author: Bekir Berk YILDIRIM
"""
from sys import exit
search_string=input("Please enter file name:")

with open("FileStructure.txt", 'r') as file:
    file_contents = file.read()

lines = file_contents.split('\n')
lines = lines[::-1]
path=[]
for line in lines:
   if search_string in line:
       start=lines.index(line)
try:
    start
except NameError:
    print("File Not Found")
    exit()
path.append(lines[start][1:])
for i in range(start+1,len(lines)):
    if '/' in lines[i] :
        continue
    path.append(lines[i][1:])
    if '*' in lines[i] :
        break
path.reverse()
l=('\\'.join(path)).split('.')
print(l[0])
     
    
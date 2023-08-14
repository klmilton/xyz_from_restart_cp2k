# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 17:37:20 2022

@author: kmilton
"""
import sys
import numpy as np



infile= sys.argv[1]
input_data = open(infile)

xyz_1=[]

for lines in input_data:
    line_words=lines.split()
    if len(line_words) == 4:
        if line_words[0] =='Si':
            xyz_1.append(line_words[:])
        if line_words[0] =='H':
            xyz_1.append(line_words[:])
        if line_words[0] == 'O':
            xyz_1.append(line_words[:])
        if line_words[0] =='Ot':
            xyz_1.append(line_words[:])
        if line_words[0] == 'Ob':
            xyz_1.append(line_words[:])
        if line_words[0] =='Ow':
            xyz_1.append(line_words[:])
        if line_words[0] =='Ht':
            xyz_1.append(line_words[:])
        if line_words[0] == 'Hb':
            xyz_1.append(line_words[:])
        if line_words[0] =='Hw':
            xyz_1.append(line_words[:])
        if line_words[0] == 'W':
            xyz_1.append(line_words[:])
        if line_words[0] =='S':
            xyz_1.append(line_words[:])
            

    
size=len(xyz_1)
a=open('xyz.xyz','w')
out_string = str(len(xyz_1)) + '\n' + 'string' + '\n'
a.write(out_string)
for i in range(size):
    out_string = str(xyz_1[i][0]) + '    ' +str(xyz_1[i][1]) + '    ' + str(xyz_1[i][2]) + '    ' + str(xyz_1[i][3]) + '\n'
    a.write(out_string)

    

    

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 17 00:37:43 2021

@author: Raza_Jutt
"""

import time
import csv
import numpy as np
import pandas as pd
#import os
from blockchain import blockexplorer

data = pd.read_csv('3.csv')
data = data.dropna()
a = data['215857']

b = []
d = []

for i in a:
    d.append(int(i))

for i in range(215857,219514):
    if i not in d:
        b.append(i)
    
print(b)
print(len(b))
 
"""
with open('miss.csv', 'w') as g:
    writer = csv.writer(g)
    pre_block = ""
    #new_row = 0, 0, 0 ,0 ,0
    #writer.writerow(new_row)
    for i in b:
        a=1
        while a:
            try :
                print(i)
                block = blockexplorer.get_block(str(i-1))
                pre_block = str(block.hash)
                block = blockexplorer.get_block(str(i))
                writer.writerow([i, block.hash, str(block.transactions), pre_block ,block.nonce])
                f = open(str(i)+".txt","w")
                f.write(str(block.transactions))
                f.close()
                pre_block = str(block.hash)
                a=0
            except:
                print("Stuck >>>>>>>  waiting")
                time.sleep(20)           
"""
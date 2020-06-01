# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 15:09:41 2020

@author: Charlie
"""

import pandas as pd
import numpy as np

# create an 4x20 empty dataframe
df = pd.DataFrame(columns=["A","B","C","D","WIP"],index=range(20))

# each "machine" starts with 3 WIP
df.iloc[0]=[3,3,3,3,12]


for i in range(1,20):
 
    A = min(np.random.randint(low=1,high=6), df.loc[i-1,"A"])
    B = min(np.random.randint(low=1,high=6), df.loc[i-1,"B"])
    C = min(np.random.randint(low=1,high=6), df.loc[i-1,"C"])
    D = min(np.random.randint(low=1,high=6), df.loc[i-1,"D"])
    
    Input = np.random.randint(low=1,high=6)
    
    df.loc[i,"A"] = df.loc[i-1,"A"] - A + Input
    df.loc[i,"B"] = df.loc[i-1,"B"] - B + A
    df.loc[i,"C"] = df.loc[i-1,"C"] - C + B
    df.loc[i,"D"] = df.loc[i-1,"D"] - D + C
    
    df.loc[i,"WIP"] = df.loc[i-1,"WIP"] + Input - D
    
print(df.mean())

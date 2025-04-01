import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from warnings import filterwarnings

dataframe1 = pd.read_csv('evdata Table V2.8.csv')
dataframe2 = dataframe1
res = list(dataframe2.columns)

mths =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
for z in res:
    if z == 'Quantity' or z == 'Unnamed: 10' :
        continue

    col = dataframe2[z].unique()
    dfgraph0 = pd.DataFrame({'MTH': mths})
    for i in col:
        dfgraph0[i] =0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        for n in dfgraph0['MTH']:
            totsum = dataframe2.loc[(dataframe2['Month']== n) & (dataframe2[z] == i ), 'Quantity'].sum()
            dfgraph0.loc[dfgraph0['MTH'] == n, i] = totsum
    
    dfgraph0.to_csv(z + "MonthEVdf.csv")

counties = dataframe2['County'].unique()
for z in res:
    if z == 'Quantity' or z == 'Unnamed: 10' :
        continue
    col = dataframe2[z].unique()
    #engines = dataframe2['Engine'].unique()
    dfgraph1 = pd.DataFrame({'County':counties})
    for x in col:
        dfgraph1[x] = 0
        for n in dfgraph1['County']:
            sumToT = dataframe2.loc[(dataframe2['County']== n) & (dataframe2[z] == x), 'Quantity'].sum()
            dfgraph1.loc[dfgraph1['County'] == n, x] = sumToT

    dfgraph1.to_csv(z + "CountyEVdf.csv")


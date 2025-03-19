import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from warnings import filterwarnings


# dataframe1 = pd.read_csv('evdata Table V2.7.csv')
# dataframe2 = dataframe1
# res = list(dataframe2.columns)

# mths =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# for z in res:
#     if z == 'Quantity' or z == 'Unnamed: 10' :
#         continue

#     col = dataframe2[z].unique()
#     dfgraph0 = pd.DataFrame({'MTH': mths})
#     for i in col:
#         dfgraph0[i] =0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
#         for n in dfgraph0['MTH']:
#             totsum = dataframe2.loc[(dataframe2['Month']== n) & (dataframe2[z] == i ), 'Quantity'].sum()
#             dfgraph0.loc[dfgraph0['MTH'] == n, i] = totsum
    
#     dfgraph0.to_csv(z + "MonthEVdf.csv")

# counties = dataframe2['County'].unique()
# for z in res:
#     if z == 'Quantity' or z == 'Unnamed: 10' :
#         continue
#     col = dataframe2[z].unique()
#     #engines = dataframe2['Engine'].unique()
#     dfgraph1 = pd.DataFrame({'County':counties})
#     for x in col:
#         dfgraph1[x] = 0
#         for n in dfgraph1['County']:
#             sumToT = dataframe2.loc[(dataframe2['County']== n) & (dataframe2[z] == x), 'Quantity'].sum()
#             dfgraph1.loc[dfgraph1['County'] == n, x] = sumToT

#     dfgraph1.to_csv(z + "CountyEVdf.csv")

# dfgraph2 = pd.read_csv("SegmentCountyEVdf.csv")
# colms = list(dfgraph2.columns)
# print(colms)

# x = dfgraph2['County']
# for n in range(2, len(colms)-1):
#     y = dfgraph2[colms[n]]
#     if n <= 11:
#         plt.plot(x,y)
#     elif n <= 21:
#         plt.plot(x,y, linestyle = 'dashed')
#     elif n <=34:
#         plt.plot(x,y,linestyle = 'dotted')

# #naming the x axis
# plt.xlabel('Month')
# # naming the y axis
# plt.ylabel('No. of cars')
# # giving a title to my graph
# plt.title('EV segment types by month')
# # show a legend on the plot
# plt.legend(colms[2:28])
# # function to show the plot
# plt.show()
# plt.savefig('EV segment types by month.png')

dfgraph3 = pd.read_csv('EngineCountyEVdf.csv')
dfgraph3 = dfgraph3.drop('Unnamed: 0', axis = 1)
# dfgraph3.plot.bar()
# plt.xticks(np.arange(len(dfgraph3['County'])),dfgraph3['County'] )
# #naming the x axis
# plt.xlabel('County')
# # naming the y axis
# plt.ylabel('No. of cars')
# # giving a title to my graph
# plt.title('EV Engine types by County')
# # show a legend on the plot
# plt.legend()
# # function to show the plot
# plt.show()


dfgraph5 = dfgraph3.drop(['petrol electric (hybrid)','diesel electric (hybrid)','electric', 'diesel/plug-in electric hybrid'],axis=1)
dfgraph5.plot.bar()
plt.xticks(np.arange(len(dfgraph5['County'])),dfgraph5['County'] )
dfgraph4 = pd.read_csv('PriceEngineCounty.csv')
dfgraph4.plot.line()

#naming the x axis
plt.xlabel('County')
# naming the y axis
plt.ylabel('Price in Euro')
# giving a title to my graph
plt.title('EV Price by Engine & County')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()


print('DONE')

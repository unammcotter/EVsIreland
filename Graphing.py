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

# dfgraph3 = pd.read_csv('MakeCountyEVdf.csv')
# dfgraph3 = dfgraph3.drop(['Unnamed: 0','Unnamed: 42'], axis = 1)
# #dfgraph3 = dfgraph3.drop(['Unnamed: 0'], axis = 1)
# dfgraph4 = pd.read_excel('CensusPopData2022.xlsx')
# for n in dfgraph3['County']:    
#     for x in list(dfgraph3.columns):
#         if x == 'County':
#             continue

#         diff = dfgraph4.loc[(dfgraph4['County']== n), 'Pop10'].sum()
#         deno = dfgraph3.loc[(dfgraph3['County']==n),x].sum()
#         ans = deno/diff
#         dfgraph3.loc[(dfgraph3['County']==n),x] = ans

# dfgraph3.plot.bar()
# plt.xticks(np.arange(len(dfgraph3['County'])),dfgraph3['County'] )
# #naming the x axis
# plt.xlabel('County')
# # naming the y axis
# plt.ylabel('No. of cars per 10,000 pop.')
# # giving a title to my graph
# plt.title('EV Car Makes by County 2024')
# # show a legend on the plot
# plt.legend()
# # function to show the plot
# plt.show()


# dfgraph5 = dfgraph3.drop(['petrol electric (hybrid)','diesel electric (hybrid)','electric', 'diesel/plug-in electric hybrid'],axis=1)
# dfgraph5.plot.bar()
# plt.xticks(np.arange(len(dfgraph5['County'])),dfgraph5['County'] )
# dfgraph4 = pd.read_csv('PriceEngineCounty.csv')
# dfgraph4.plot.line()

# #naming the x axis
# plt.xlabel('County')
# # naming the y axis
# plt.ylabel('Price in Euro')
# # giving a title to my graph
# plt.title('EV Price by Engine & County')
# # show a legend on the plot
# plt.legend()
# # function to show the plot
# plt.show()

#------------------------------------------------------------------------------------
#------------------Graph of top 5 Makes----------------------------------------------
dfgraph3 = pd.read_csv('MakeCountyEVdf.csv')
dfgraph3 = dfgraph3.drop(['Unnamed: 0','Unnamed: 42'], axis = 1)
#dfgraph3 = dfgraph3.drop(['Unnamed: 0'], axis = 1)
dfgraph4 = pd.read_excel('CensusPopData2022.xlsx')
for n in dfgraph3['County']:    
    for x in list(dfgraph3.columns):
        if x == 'County':
            continue

        diff = dfgraph4.loc[(dfgraph4['County']== n), 'Pop10'].sum()
        deno = dfgraph3.loc[(dfgraph3['County']==n),x].sum()
        ans = deno/diff
        dfgraph3.loc[(dfgraph3['County']==n),x] = ans

df = pd.read_csv('MakeCountyEVdf.csv')
df = df.drop(['Unnamed: 0','Unnamed: 42'], axis = 1)
for col in df.columns:
    if col == 'County':
            continue
    df[col].values[:] = 0

for z in list(dfgraph3.columns):
    if z == 'County':
            continue
    d = dfgraph3.nlargest(5, z)[['County',z]]
    df = pd.merge(df,d,on="County", how = "inner")

dfgraph3.plot.bar()
plt.xticks(np.arange(len(dfgraph3['County'])),dfgraph3['County'] )
#naming the x axis
plt.xlabel('County')
# naming the y axis
plt.ylabel('No. of cars per 10,000 pop.')
# giving a title to my graph
plt.title('EV Car Makes by County 2024')
# show a legend on the plot
plt.legend()
# function to show the plot
plt.show()

#---------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#----------------------------Car ownership vs Reg cars
df1 = pd.read_csv('AdminCounty2022.csv')
cl = list(df1.columns)
print(cl)
df1 = df1[['County','T15_1_1C','T15_1_2C','T15_1_3C','T15_1_GE4C']]
df2 = pd.read_csv('CountyCountyEVdf.csv')

df1.drop(df1.tail(1).index,
        inplace = True)
df2.drop(df2.tail(1).index,
        inplace = True)

df1.insert(1,'Quantity', df2['Quantity'])

x1 = df1['Quantity']
x2 = df1['Quantity']
x3 = df1['Quantity']
x4 = df1['Quantity']
y1 = df1['T15_1_1C']
y2 = df1['T15_1_2C']
y3 = df1['T15_1_3C']
y4 = df1['T15_1_GE4C']

plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)
plt.scatter(x4,y4)
#naming the x axis
plt.xlabel('Number of Registered cars')
# naming the y axis
plt.ylabel('Number of Housholds')
# giving a title to my graph
plt.title('Car Ownership vs number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['1 Car','2 Car', '3 Car', '4+ Cars'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T15_1_1C']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/housholds')
# giving a title to my graph
plt.title('Households with 1 Car & Resigtered EV & Plug-in')
#show a legend on the plot
plt.legend(['Registered Cars','Households'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T15_1_2C']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/housholds')
# giving a title to my graph
plt.title('Households with 2 Cars & Resigtered EV & Plug-in')
#show a legend on the plot
plt.legend(['Registered Cars','Households'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T15_1_3C']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/housholds')
# giving a title to my graph
plt.title('Households with 3 Cars & Resigtered EV & Plug-in')
#show a legend on the plot
plt.legend(['Registered Cars','Households'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T15_1_GE4C']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/housholds')
# giving a title to my graph
plt.title('Households with 4+ Cars & Resigtered EV & Plug-in')
#show a legend on the plot
plt.legend(['Registered Cars','Households'])
#function to show the plot
plt.show()
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#----------------------------House Type vs Reg cars
df1 = pd.read_csv('AdminCounty2022.csv')
cl = list(df1.columns)
print(cl)
df1 = df1[['County','T6_1_HB_H','T6_1_FA_H','T6_1_BS_H','T6_1_CM_H']]
df2 = pd.read_csv('CountyCountyEVdf.csv')

df1.drop(df1.tail(1).index,
        inplace = True)
df2.drop(df2.tail(1).index,
        inplace = True)

df1.insert(1,'Quantity', df2['Quantity'])

x1 = df1['Quantity']
x2 = df1['Quantity']
x3 = df1['Quantity']
x4 = df1['Quantity']
y1 = df1['T6_1_HB_H']
y2 = df1['T6_1_FA_H']
y3 = df1['T6_1_BS_H']
y4 = df1['T6_1_CM_H']

plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)
plt.scatter(x4,y4)
#naming the x axis
plt.xlabel('Number of Registered cars')
# naming the y axis
plt.ylabel('Number of Housholds')
# giving a title to my graph
plt.title('Home Type vs number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['House/Bungalow','Flat/Apartment', 'Bed-Sit', 'Caravan/Mobile home'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T6_1_HB_H']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/households')
# giving a title to my graph
plt.title('House Type & Resigtered EV & Plug-in')
#show a legend on the plot
plt.legend(['Registered Cars','House/Bungalow'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T6_1_FA_H']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/houeholds')
# giving a title to my graph
plt.title('House Type & Resigtered EV & Plug-in')
#show a legend on the plot
plt.legend(['Registered Cars','Flat/Apartment'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T6_1_BS_H']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/households')
# giving a title to my graph
plt.title('House Type & Resigtered EV & Plug-in')
#show a legend on the plot
plt.legend(['Registered Cars','Bed-Sit'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T6_1_CM_H']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/housholds')
# giving a title to my graph
plt.title('House Type & Resigtered EV & Plug-in')
#show a legend on the plot
plt.legend(['Registered Cars','Caravan/Mobile home'])
#function to show the plot
plt.show()
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#----------------------------Renewable vs Reg cars
df1 = pd.read_csv('AdminCounty2022.csv')
cl = list(df1.columns)
print(cl)
df1 = df1[['County','T6_10_RE']]
df2 = pd.read_csv('CountyCountyEVdf.csv')

df1.drop(df1.tail(1).index,
        inplace = True)
df2.drop(df2.tail(1).index,
        inplace = True)

df1.insert(1,'Quantity', df2['Quantity'])

x1 = df1['Quantity']
y1 = df1['T6_10_RE']

plt.scatter(x1,y1)

#naming the x axis
plt.xlabel('Number of Registered cars')
# naming the y axis
plt.ylabel('Number of Housholds')
# giving a title to my graph
plt.title('Households with Renewable Energy vs number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend()
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T6_10_RE']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Number of registered cars/households')
# giving a title to my graph
plt.title('Households with Renewable Energy vs number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['Registered Cars','Household'])
#function to show the plot
plt.show()

#--------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------
#----------------------------Higher Profes by people vs Reg cars
df1 = pd.read_csv('AdminCounty2022.csv')
df1 = df1[['County','T9_2_PB']]
df2 = pd.read_csv('CountyCountyEVdf.csv')

df1.drop(df1.tail(1).index,
        inplace = True)
df2.drop(df2.tail(1).index,
        inplace = True)

df1.insert(1,'Quantity', df2['Quantity'])

x1 = df1['Quantity']
y1 = df1['T9_2_PB']

plt.scatter(x1,y1)

#naming the x axis
plt.xlabel('Number of Registered cars')
# naming the y axis
plt.ylabel('Number of Higher Professionals')
# giving a title to my graph
plt.title('Higher Professionals vs number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend()
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T9_2_PB']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Quantity')
# giving a title to my graph
plt.title('Higher Professionals vs number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['Registered Cars','Higher Professional'])
#function to show the plot
plt.show()

print('yay')
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#----------------------------Commuter Type vs Reg cars
df1 = pd.read_csv('AdminCounty2022.csv')
df1 = df1[['County','T11_1_BUT','T11_1_TDLT','T11_1_CDT']]
df2 = pd.read_csv('CountyCountyEVdf.csv')

df1.drop(df1.tail(1).index,
        inplace = True)
df2.drop(df2.tail(1).index,
        inplace = True)

df1.insert(1,'Quantity', df2['Quantity'])

x1 = df1['Quantity']
x2 = df1['Quantity']
x3 = df1['Quantity']
y1 = df1['T11_1_BUT']
y2 = df1['T11_1_TDLT']
y3 = df1['T11_1_CDT']

plt.scatter(x1,y1)
plt.scatter(x2,y2)
plt.scatter(x3,y3)

#naming the x axis
plt.xlabel('Number of Registered cars')
# naming the y axis
plt.ylabel('Number of Housholds')
# giving a title to my graph
plt.title('Commuter Type vs number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['Bus','Rail','Car'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T11_1_BUT']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Quantity')
# giving a title to my graph
plt.title('Bus users and number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['Registered Cars','Bus user'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T11_1_TDLT']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Quantity')
# giving a title to my graph
plt.title('Rail users and number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['Registered Cars','Rail users'])
#function to show the plot
plt.show()

df3 = df1[['County','Quantity','T11_1_CDT']]
df3.plot.bar()
plt.xticks(np.arange(len(df3['County'])),df3['County'] )
plt.xlabel('County')
# naming the y axis
plt.ylabel('Quantity')
# giving a title to my graph
plt.title('Car drivers and number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['Registered Cars','Car drivers'])
#function to show the plot
plt.show()

print('yay')
#--------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------
#----------------------------Degrees Type vs Reg cars
df1 = pd.read_csv('AdminCounty2022.csv')
df1 = df1[['County','T10_4_HDPQT','T10_4_PDT','T10_4_DT']]
df1['3rd level degree'] = df1[['T10_4_HDPQT','T10_4_PDT','T10_4_DT']].sum(axis =1)
df2 = pd.read_csv('CountyCountyEVdf.csv')

df1.drop(df1.tail(1).index,
        inplace = True)
df2.drop(df2.tail(1).index,
        inplace = True)

df1.insert(1,'Quantity', df2['Quantity'])

x1 = df1['Quantity']
#x2 = df1['Quantity']
#x3 = df1['Quantity']
y1 = df1['3rd level degree']
#y2 = df1['T11_1_TDLT']
#y3 = df1['T11_1_CDT']

plt.scatter(x1,y1)
#plt.scatter(x2,y2)
#plt.scatter(x3,y3)

#naming the x axis
plt.xlabel('Number of Registered cars')
# naming the y axis
plt.ylabel('Number of Degrees')
# giving a title to my graph
plt.title('Bacholer Degree vs number of registered EVs & Plugins car')
#show a legend on the plot
plt.legend(['Bachelor'])#,'Rail','Car'])
#function to show the plot
plt.show()

print('yay')
#--------------------------------------------------------------------------------------------

# dfgraph6 = pd.read_csv('AdminCounty2022.csv')
# #cl = list(dfgraph6.columns)
# #print(cl)
# dfgraph6 = dfgraph6[['County','T15_1_NC','T15_1_1C','T15_1_2C','T15_1_3C','T15_1_GE4C','T15_1_NSC','T15_1_TC']]
# #dfgraph6 = dfgraph6.drop(['Unnamed: 0','Unnamed: 42'], axis = 1)
# #dfgraph6 = dfgraph6.drop(['Unnamed: 0'], axis = 1)
# dfgraph7 = pd.read_csv('CountyCountyEVdf.csv')

# dfgraph6.drop(dfgraph6.tail(1).index,
#         inplace = True)
# dfgraph7.drop(dfgraph7.tail(1).index,
#         inplace = True)

# x1 = dfgraph6['T15_1_1C']
# x2 = dfgraph6['T15_1_2C']
# x3 = dfgraph6['T15_1_3C']
# x4 = dfgraph6['T15_1_GE4C']
# y = dfgraph7['Quantity']

# plt.scatter(x1,y)
# #naming the x axis
# plt.xlabel('Number of households')
# # naming the y axis
# plt.ylabel('Number of registered cars')
# # giving a title to my graph
# plt.title('Cars owned vs number of registered evs car')
# # show a legend on the plot
# # plt.legend()
# # function to show the plot
# plt.show()
# plt.scatter(x2,y)
# plt.legend()
# plt.show()
# plt.scatter(x3,y)
# plt.show()
# plt.scatter(x4,y)
# plt.show()

# dfgraph6 = pd.read_csv('AdminCounty2022.csv')
# #cl = list(dfgraph6.columns)
# #print(cl)
# dfgraph6 = dfgraph6[['County','T15_1_1C','T15_1_2C','T15_1_3C','T15_1_GE4C']]
# #dfgraph6 = dfgraph6.drop(['Unnamed: 0','Unnamed: 42'], axis = 1)
# #dfgraph6 = dfgraph6.drop(['Unnamed: 0'], axis = 1)
# dfgraph7 = pd.read_csv('CountyCountyEVdf.csv')

# dfgraph6.drop(dfgraph6.tail(1).index,
#         inplace = True)
# dfgraph7.drop(dfgraph7.tail(1).index,
#         inplace = True)

# x = dfgraph6['County']
# y2 = dfgraph6['T15_1_2C']
# y3 = dfgraph6['T15_1_3C']
# y4 = dfgraph6['T15_1_GE4C']
# dfgraph6.insert(1,'Quantity', dfgraph7['Quantity'])

# dfgraph6 = dfgraph6[['County','Quantity','T15_1_2C']]

# dfgraph6.plot.bar()
# plt.xticks(np.arange(len(dfgraph6['County'])),dfgraph6['County'] )
# #naming the x axis
# plt.xlabel('County')
# # naming the y axis
# plt.ylabel('Number of registered cars/housholds')
# # giving a title to my graph
# plt.title('Households with 1 car vs number of registered evs car')
# # show a legend on the plot
# # plt.legend()
# # function to show the plot
# plt.show()

# dfgraph8 = pd.read_csv('AdminCounty2022.csv')
# #cl = list(dfgraph6.columns)
# #print(cl)
# dfgraph8 = dfgraph8[['County','T6_1_HB_P','T6_1_FA_P','T6_1_BS_P','T6_1_CM_P']]
# #dfgraph6 = dfgraph6.drop(['Unnamed: 0','Unnamed: 42'], axis = 1)
# #dfgraph6 = dfgraph6.drop(['Unnamed: 0'], axis = 1)
# dfgraph9 = pd.read_csv('CountyCountyEVdf.csv')

# dfgraph8.drop(dfgraph8.tail(1).index,
#         inplace = True)
# dfgraph9.drop(dfgraph9.tail(1).index,
#         inplace = True)

# dfgraph8.insert(1,'Quantity', dfgraph9['Quantity'])

# dfgraph4 = pd.read_excel('CensusPopData2022.xlsx')

# datatypes1 = dfgraph8.dtypes
# datatypes2 = dfgraph4
# print(datatypes1)
# print(datatypes2)
# for n in dfgraph8['County']:    
#     for x in list(dfgraph8.columns):
#         if x == 'County':
#             continue

#         diff = dfgraph4.loc[(dfgraph4['County']== n), 'Pop10'].sum()
#         deno = dfgraph8.loc[(dfgraph8['County']==n),x].sum()
#         ans = deno/diff
#         dfgraph8.loc[(dfgraph8['County']==n),x] = ans
# dfgraph8.round(0)

# #dfgraph6 = dfgraph6[['County','Quantity','T6_1_HB_P','T6_1_FA_P']]
# x1 = dfgraph8['Quantity']
# x2 = dfgraph8['Quantity']
# x3 = dfgraph8['Quantity']
# x4 = dfgraph8['Quantity']
# y1 = dfgraph8['T6_1_HB_P']
# y2 = dfgraph8['T6_1_FA_P']
# y3 = dfgraph8['T6_1_BS_P']
# y4 = dfgraph8['T6_1_CM_P']

# plt.scatter(x1,y1)
# plt.scatter(x2,y2)
# plt.scatter(x3,y3)
# plt.scatter(x4,y4)
# #dfgraph6.plot.bar()
# #plt.xticks(np.arange(len(dfgraph6['County'])),dfgraph6['County'] )
# #naming the x axis
# plt.xlabel('County')
# # naming the y axis
# plt.ylabel('Number of registered cars/housholds')
# # giving a title to my graph
# plt.title('Households with 1 car vs number of registered evs car')
# # show a legend on the plot
# #plt.legend()
# # function to show the plot
# plt.show()

# dfgraph6 = dfgraph8
# #dfgraph6.insert(1,'Quantity', dfgraph7['Quantity'])
# #dfgraph6 = dfgraph6[['County','Quantity','T6_1_FA_P']]

# dfgraph6.plot.bar()
# plt.xticks(np.arange(len(dfgraph6['County'])),dfgraph6['County'] )
# #naming the x axis
# plt.xlabel('County')
# # naming the y axis
# plt.ylabel('Number of registered cars/housholds')
# # giving a title to my graph
# plt.title('Households with 1 car vs number of registered evs car')
# # show a legend on the plot
# # plt.legend()
# # function to show the plot
# plt.show()

print('DONE')

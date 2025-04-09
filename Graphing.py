import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from warnings import filterwarnings


#SIMPLE STATS NOT NORMALISED
dfCensus = pd.read_csv("Census2022V2.0.csv")
dfCensus = dfCensus[['County',
 #Table 1: Population aged 18+ by sex
                     'Total_Males_18plus', 'Total_Females_18plus',

 #Table 1: Population aged 18 - 19 by sex and year of age, persons aged 20 years and over by sex and age group
                     'T1_1AGE18T','T1_1AGE19T','T1_1AGE20_24T','T1_1AGE25_29T',
                     'T1_1AGE30_34T','T1_1AGE35_39T','T1_1AGE40_44T','T1_1AGE45_49T',
                     'T1_1AGE50_54T','T1_1AGE55_59T','T1_1AGE60_64T','T1_1AGE65_69T',
                     'T1_1AGE70_74T','T1_1AGE75_79T','T1_1AGE80_84T','T1_1AGEGE_85T',
 
 #Table 1: Private households by type of accommodation                     
                     'T6_1_HB_H','T6_1_FA_H','T6_1_BS_H','T6_1_CM_H',

 #Table 3: Permanent private households by type of occupancy                     
                     'T6_3_RPLH','T6_3_RLAH','T6_3_RVCHBH','T6_3_OFRH',

 #Table 10: Permanent private households by number of renewables                    
                     'T6_10_RE',
 
 #Table 4: Population aged 15 years and over by sex and highest level of education completed        
                     'T10_4_TVT','T10_4_ACCAT','T10_4_HCT','T10_4_ODNDT','T10_4_HDPQT',
                     'T10_4_PDT','T10_4_DT',

 #Table 2: Persons in private households by socio-economic group of reference person
                     'T9_2_HA','T9_2_HB','T9_2_HC','T9_2_HD','T9_2_HE','T9_2_HF',
                     'T9_2_HG','T9_2_HH','T9_2_HI','T9_2_HJ','T9_2_HZ',

 #Table 1: Population aged 5 years and over by means of travel to work, school or college
                     'T11_1_FW','T11_1_BIW','T11_1_BUW','T11_1_TDLW','T11_1_MW',
                     'T11_1_CDW','T11_1_CPW','T11_1_VW','T11_1_OTHW','T11_1_WMFHW',
                     'T11_1_NSW','T11_1_FT','T11_1_BIT','T11_1_BUT','T11_1_TDLT',
                     'T11_1_CDT',
                
 #Table 1: Number of households with cars
                     'T15_1_NC','T15_1_1C','T15_1_2C','T15_1_3C','T15_1_GE4C']]

plus2_car_cols = ['T15_1_2C','T15_1_3C','T15_1_GE4C']
activeT = ['T11_1_FT','T11_1_BIT']
pT = ['T11_1_BUT','T11_1_TDLT']

dfCensus['T15_1_2C+'] = dfCensus[plus2_car_cols].sum(axis=1)
dfCensus['T11_1_ACT'] = dfCensus[activeT].sum(axis=1)
dfCensus['T11_1_PUT'] = dfCensus[pT].sum(axis=1)

dfCensus2 = dfCensus.drop(columns=plus2_car_cols)
dfCensus2 = dfCensus2.drop(columns=activeT)
dfCensus2 = dfCensus2.drop(columns=pT)
dfCensus2 = dfCensus2.drop(columns='County')

dfBEVs = pd.read_csv("Combined_CountyEVdf.csv")
dfCensus2['Total BEVs'] =  dfBEVs[['2024']]
dfCensus2.drop(dfCensus.tail(1).index,
        inplace = True)

# Summary statistics
summary = dfCensus2.describe().T[['mean', '50%', 'std']]  # 50% = median
summary.rename(columns={'50%': 'median'}, inplace=True)
print(summary)

# Select only numeric columns
all_columns = dfCensus2.columns

# Compute correlations
correlation_matrix = dfCensus2[all_columns].corr()

# Show correlation of age groups with 'No. Cars'
print(correlation_matrix['Total BEVs'].sort_values(ascending=False))

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Matrix of Census Data Groups and BEV Registration")
plt.show()

# Create scatterplots for each age group
import matplotlib.pyplot as plt
import seaborn as sns

for col in all_columns:
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=dfCensus2[col], y=dfCensus2['Total BEVs'])
    sns.regplot(x=dfCensus2[col], y=dfCensus2['Total BEVs'], scatter=False, color='red')
    plt.title(f"Total BEVs Reg. vs {col}")
    plt.xlabel(col)
    plt.ylabel("Total BEVs Re.")
    plt.tight_layout()
    plt.show()

#-----------------------------------------------------------------------------------------------



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

# version %%%
df1 = pd.read_csv('AdminCounty2022.csv')
df1 = df1[['County','T6_10_RE','T6_10_NORE','T6_10_NS','T6_10_T']]
df2 = pd.read_csv('CountyCountyEVdf.csv')

ire_val = df1['T6_10_RE'].iloc[-1]
df1['Renewables%'] = (df1['T6_10_RE']/df1['T6_10_T'])*100
df1['NoRenewables%'] = (df1['T6_10_NORE']/df1['T6_10_T'])*100

df1.drop(df1.tail(1).index,
        inplace = True)
#df2.drop(df2.tail(1).index,
#        inplace = True)

print(df1['County'])
df1.insert(1,'Quantity', df2['Quantity'])

# x1 = df1['Quantity']
# y1 = df1['Renewables%']
# plt.scatter(x1,y1)

# #naming the x axis
# plt.xlabel('Number of Registered cars')
# # naming the y axis
# plt.ylabel('Number of Housholds')
# # giving a title to my graph
# plt.title('Households with Renewable Energy vs number of registered EVs & Plugins car')
# #show a legend on the plot
# plt.legend()
# #function to show the plot
# plt.show()

value_remove = ['Dublin']
df4 = df1[~df1['County'].isin(value_remove)]
y2 = df4['Quantity']
x2 = df4['Renewables%']

plt.scatter(x2,y2)

#naming the x axis
plt.xlabel('% Share of Households')
# naming the y axis
plt.ylabel('Number of Registered cars')
# giving a title to my graph
plt.title('Households with Renewable Energy vs number of registered BEVs')
#show a legend on the plot
plt.legend()
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

#% version
df1 = pd.read_csv('AdminCounty2022.csv')
df1 = df1[['County','T9_2_PB','T9_2_PT']]
df2 = pd.read_csv('CountyCountyEVdf.csv')

ire_val = df1['T9_2_PB'].iloc[-1]
df1['HigherProfs%'] = (df1['T9_2_PB']/df1['T9_2_PT'])*100

df1.drop(df1.tail(1).index,
        inplace = True)
#df2.drop(df2.tail(1).index,
#        inplace = True)



print(df1['County'])
df1.insert(1,'Quantity', df2['Quantity'])

df5 = pd.read_excel('passenger-cars-by-county.xlsx')
df1['Quantity%'] = (df1['Quantity']/df5['2024 Units'])*100

y1 = df1['Quantity%']
x1 = df1['HigherProfs%']
plt.scatter(x1,y1)

#naming the x axis
plt.xlabel('% Share of Population')
# naming the y axis
plt.ylabel('% Share of Registered cars')
# giving a title to my graph
plt.title('Higher Professionals vs number of registered BEVs')
#show a legend on the plot
plt.legend()
#function to show the plot
plt.show()


# value_remove = ['Dublin']
# df4 = df1[~df1['County'].isin(value_remove)]
# y2 = df4['Quantity']
# x2 = df4['HigherProfs%']

# plt.scatter(x2,y2)

# #naming the x axis
# plt.xlabel('% Share of Households')
# # naming the y axis
# plt.ylabel('Number of Registered cars')
# # giving a title to my graph
# plt.title('Higher Professionals vs vs number of registered BEVs')
# #show a legend on the plot
# plt.legend()
# #function to show the plot
# plt.show()

print('done')
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

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings

dataframe1 = pd.read_csv('evdata Table V2.6.csv')
dataframe2 = dataframe1.dropna()

#x = dataframe2['Month']
#y = dataframe2['Quantity']
mths =  ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
print (mths)
dfgraph1 = pd.DataFrame({'MTH': mths})
dfgraph1['Total'] = 0
for n in dfgraph1['MTH']:
    totsum = dataframe2.loc[dataframe2['Month']== n, 'Quantity'].sum()
    dfgraph1.loc[dfgraph1['MTH'] == n, 'Total'] = totsum

print(dfgraph1)

engines = dataframe2['Engine'].unique()
print (engines)
dfgraph2 = pd.DataFrame({'MTH': mths})
for i in engines:
    dfgraph2[i] = 0
   
    for n in dfgraph2['MTH']:
        totsum = dataframe2.loc[(dataframe2['Month']== n) & (dataframe2['Engine'] == i ), 'Quantity'].sum()
        dfgraph2.loc[dfgraph1['MTH'] == n, i] = totsum

print(dfgraph2)

# plt.plot(x,y)
# plt.xlabel('Month')
# plt.ylabel('Number of regisetered cars')
# plt.title('New Restrations of Eletric and Hybrid Cars')
# plt.draw()
# plt.show()

#mths = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# plt.bar(x,y, width = 0.5)

# plt.xlabel('Month')
# plt.ylabel('Number of regisetered cars')
# plt.title('New Restrations of Eletric and Hybrid Cars')
# #plt.draw()
# plt.show()

#dataframe3 = dataframe2[['Month','Quantity']]
#dataframe3.plot(kind='bar')
#dataframe3['Month'].value_counts().plot(kind ='bar',xlabel='Month',ylabel='Count', rot=0)
print('DONE')
#dataframe3 = sns.load_dataset('evdata Table V2.6.csv')
#dataframe3.head()

#print(x,y)
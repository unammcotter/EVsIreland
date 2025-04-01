import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from warnings import filterwarnings

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
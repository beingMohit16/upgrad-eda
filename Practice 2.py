# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 15:28:48 2021

@author: mohit
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df= pd.read_csv(r'E:\UPgrade\Practice+Questions+-+Session+2\Practice Questions - Session 2\Footwear_v2.csv')

print(df.loc[:,['Delhi','Mumbai','Mumbai','Jaipur','Hyderabad']].apply(lambda x : float(x[:-1]) if x[-1] == '%' else float(x)))

df['Hyderabad'] = df['Hyderabad'].apply(lambda x : float(x[:-1]) if x[-1] == '%' else float(x))
print(np.abs())

def clean(string):
    clean="".join(filter(lambda x: x!='%', string))
    return float(clean)

df['Mumbai']=df['Mumbai'].apply(clean)
df['Delhi']=df['Delhi'].apply(clean)
df['Jaipur']=df['Jaipur'].apply(clean)
df['Hyderabad']=df['Hyderabad'].apply(clean)

df.describe()

sub_df=df[['Delhi', 'Mumbai', 'Jaipur', 'Hyderabad']]
sub_df.boxplot()


cryp= pd.read_csv(r'E:\UPgrade\Practice+Questions+-+Session+2\Practice Questions - Session 2\crypto.csv')

sns.pairplot(cryp)

crpy2 = cryp.corr()

sns.heatmap(crpy2, cmap = 'Greens', annot = True)

marks = pd.read_csv(r'E:\UPgrade\Data+Visualisation+-+Practice+Questions\Data Visualisation - Graded Questions\Marks.csv')
marks.info()

plt.hist(marks['Score A'],bins = 6)
plt.boxplot(marks['Score C'])
marks['Score C'].describe()

df3 = df2[(df2.Profit < 0) & (df2.Sales < 15000)]
sns.jointplot('Sales', 'Profit', df3)
plt.show()


df2 = pd.read_csv(r'E:\UPgrade\Data+Visualisation+-+Practice+Questions\Data Visualisation - Graded Questions\superstore.csv')

df3 = df2[(df2.Profit < 0) | (df2.Sales < 15000)]
sns.jointplot('Sales', 'Profit', df3)
plt.show()

sns.barplot(data = df2, x = 'Segment', y = 'Sales', estimator = np.mean)
sns.barplot(data = df2, x = 'Segment', y = 'Sales', estimator = np.avg)

pie_data = df2.groupby('Ship Mode')['Quantity'].sum()

df2['Discount'] = df2['Discount'].apply(lambda x : float(x[:-1]) if x[-1] == '%' else float(x))

bar_data = df2.groupby('Region')['Discount'].mean()

sns.barplot(x = df2['Region'], y = df2['Discount'].mean())

census = pd.read_excel(r'E:\UPgrade\census+data.xlsx')


import pandas as pd
marks = pd.read_csv('https://query.data.world/s/HqjNNadqEnwSq1qnoV_JqyRJkc7o6O')
df = df[df.isnull().sum(axis=1) != 5]
print(df.isnull().sum())

import pandas as pd
customer = pd.read_csv('https://query.data.world/s/y9rxL9mGdP6AXPiDaIL4yYm6DsfTV2')

customer['Cust_id'] = customer['Cust_id'].apply(lambda x : x[5:] )
print(customer.head(10))

from py_dataset import data
sleepstudy =data('sleepstudy')

sleepstudy['Reaction'] = #Type your code here

print(sleepstudy.head(10))




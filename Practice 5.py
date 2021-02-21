import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime 


gold_silver = pd.read_csv(r'E:\UPgrade\EDA_Gold_Silver_prices.csv')

gold_silver['Year'] = gold_silver['Month'].apply(lambda x : x[-2:])
gold_silver['Year'] = gold_silver['Year'].astype('int32')
gold_silver['Year'].describe()
gold_silver['Year'] = gold_silver['Year'].apply(lambda x :'19'+ str(x) if x > 17 else ( '200'+ str(x) if x <10 else '20'+ str(x) ))

gold_silver.apply(lambda x : x if x[-1] == 2008 else 'sorry')

gold_silver = gold_silver['Year' == 2008]

currencies = pd.read_csv(r'E:\UPgrade\currencies.csv')
currencies_corr = currencies.corr()

nas = pd.read_csv(r'E:\UPgrade\nas.csv')
nas.info()
nas.isnull().sum()
nas['Mother.edu '== 'Illiterate'].value_counts()


pd.pivot_table(nas[(nas['Mother.edu'] == 'Illiterate')],values = nas['Mother.edu'], index = nas['Siblings'],aggfunc = 'count' )



pd.pivot_table(nas[(nas, 
                           index = nas['Siblings'],values = nas['Mother.edu'] ,aggfunc = 'count' )


nas.groupby(['Mother.edu','Siblings'])['Siblings'].count()

#You also want to understand how the average science marks vary with the father’s education level and age. 
#Neglect the age group of 11 years since there are very few children in that segment. Mark the correct statement:

nas['Science..'].describe()
nas.groupby(['Father.edu'])['Science..'].mean()

nas[nas['Age'] != '11- years'].groupby(['Father.edu'])['Science..'].mean()
nas[nas['Age'] != '11- years'].groupby(['Age','Father.edu'])['Science..'].mean()














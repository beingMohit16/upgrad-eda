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
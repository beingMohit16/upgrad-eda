# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 18:26:29 2021

@author: mohit
"""
import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns


popularity = pd.read_csv(r'E:\UPgrade\popularity.csv')
popularity[' shares'].describe()
np.percentile(popularity[' shares'],80)

sns.boxplot(pop_shr[' shares'])

Q1 = np.percentile(popularity[' shares'], 25, interpolation = 'midpoint')  
Q2 = np.percentile(popularity[' shares'], 50, interpolation = 'midpoint')  
Q3 = np.percentile(popularity[' shares'], 75, interpolation = 'midpoint')

IQR = Q3 - Q1  
low_lim = Q1 - 1.5 * IQR 
up_lim = Q3 + 1.5 * IQR 
pop_shr =popularity[popularity[' shares']<10800]
pop_shr[' shares'].describe()
st.stdev(pop_shr[' shares'])
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:39:39 2021

@author: mohit
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime 

companies = pd.read_csv(r'E:\UPgrade\InvestmentAnalysis\companies.csv', encoding= 'unicode_escape')
rounds2 = pd.read_csv(r'E:\UPgrade\InvestmentAnalysis\rounds2.csv',encoding = 'unicode_escape')

#creating company and companytype column in round2
rounds2['company'] = rounds2['company_permalink'].apply(lambda x : x.split(r'/')[-1]).str.lower()
rounds2['companytype'] = rounds2['company_permalink'].apply(lambda x : x.split(r'/')[-2]).str.lower()

#rounds3 = rounds2.company_permalink.str.split(n=1, expand=True)
#rounds3.columns = ['STATUS_ID{}'.format(x+1) for x in rounds3.columns]

print('No of the Unique companies in round1 : ',len(pd.unique(rounds2['company'])))

#creating company and companytype column in companies
rounds2['company'] = rounds2['company_permalink'].apply(lambda x : x.split(r'/')[-1]).str.lower()
rounds2['companytype'] = rounds2['company_permalink'].apply(lambda x : x.split(r'/')[-2]).str.lower()

companies.info()
companies.name.describe()
rounds2.company_permalink.value_counts()

companies.permalink = companies.permalink.str.lower()
rounds2.equals(companies)
master_frame = pd.concat([rounds2,companies], axis = 1)

test['null'] = rounds2[rounds2['raised_amount_usd'].isnull() == True].groupby('funding_round_type')['raised_amount_usd'].count()
test['null'] = rounds2['raised_amount_usd'].isnull().sum()



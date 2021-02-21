# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:31:06 2021

@author: mohit
"""

import pandas as pd
cust_rating = pd.read_csv('https://query.data.world/s/ILc-P4llUraMaYN6N6Bdw7p6kUvHnj')

cust_rating['avg_rating'] = round(cust_rating.iloc[:,2:].mean(axis = 1))

print(cust_rating.head(10))

odi_batting = pd.read_csv(r'E:\UPgrade\odi-batting.csv')

odi_batting['century'] = odi_batting['Runs'].apply(lambda x : 1 if x  >99 else 0)
name = odi_batting.groupby('Player')['century'].sum()
odi_batting['strike_rate'] = (odi_batting['Runs']*100)/odi_batting['Balls']
test = odi_batting[odi_batting['century'] == 1]
odi_batting['Year'] = odi_batting['MatchDate'].apply(lambda x: x[6:])

odi_batting[odi_batting['Country'] == 'India'].groupby('Year')['century'].sum()

order = pd.read_csv('https://query.data.world/s/3hIAtsCE7vYkPEL-O5DyWJAeS5Af-7')
order['Order_Date'] = pd.to_datetime(order['Order_Date'])

order['day'] = order['Order_Date'].dt.day_name()

order['day'] = order['Order_Date'].apply(lambda x: int(x[7:9]))


print(order.head(10))

grades = pd.read_csv(r'E:\UPgrade\grades.csv')

grades['format'] = grades['submission'].apply(lambda x : x[-3:])
grades['format'] = grades['format'].apply(lambda x : x[1:] if x == '.7z' else (x[-1] if x[-1] == 'R' else x))
grades['format'].value_counts()
grades['percent'] = grades['format'].value_counts()/grades['format'].count()
grades['submit_time'] = pd.to_datetime(grades['submit_time'])
grades['submission'].value_counts()
grades['day'] = grades['submit_time'].dt.day
grades['month'] = grades['submit_time'].dt.month
grades['year'] = grades['submit_time'].dt.year
grades['date'] = grades['submit_time'].dt.date
grades['hour'] = grades['submit_time'].dt.hour

grades[(grades['day'] > 3) & (grades['month'] >= 1) & (grades['year'] > 2016)].describe()
grades['date'].value_counts()
grades['hour'].value_counts()

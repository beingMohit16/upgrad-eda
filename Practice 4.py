import pandas as pd
import numpy as np
import statistics as st
import matplotlib.pyplot as plt
import seaborn as sns

nas = pd.read_csv(r'E:\UPgrade\EDA_nas.csv')

nas.info()
nas['State'].value_counts()
pd.pivot_table(nas,index =  'Watch.TV', values = 'Science..', aggfunc = 'mean', fill_value = 0 )
pd.pivot_table(nas,index =  'Father.edu', values = 'Maths..', aggfunc = 'mean', fill_value = 0 )
pd.pivot_table(nas,index =  'Play.games', values = 'Reading..', aggfunc = 'mean', fill_value = 0 )

nas_8 = pd.read_csv(r'E:\UPgrade\EDA_nas (2).csv')
nas_8.info()
nas['Solve.Maths'].describe()
pd.pivot_table(nas_8,index = 'Solve.Maths', values = 'Maths..', aggfunc = 'mean')

grad_census = pd.read_excel(r'E:\UPgrade\EDA_census.xlsx')
grad_census.reset_index(inplace = True)
#grad_census['level_0'].columns = grad_census['level_0'].iloc[0]

grad_census = grad_census.iloc[:,:15]
grad_census.info()
grad_census.rename(columns = {'level_0':'Table_name','level_1':'State_code','level_2':'Distt_code','level_3':'Area_name',
                              'level_4':'Total/Rural/Urban','Unnamed: 1':'Person','Unnamed: 2':'Male','Unnamed: 3':'Female','Unnamed: 4':'Illit_person',
                              'Unnamed: 5':'Illit_male','Unnamed: 6':'Illit_female','Unnamed: 7':'Liit_person',
                              'Unnamed: 8':'Liit_male','Unnamed: 9':'Liit_female',
                              'C-8  EDUCATIONAL LEVEL BY AGE AND SEX FOR POPULATION AGE 7 AND ABOVE - 2011': 'Age-Group'}, inplace = True)

grad_census = grad_census.iloc[6:,]
grad_census.isnull().sum()

grad_census['State_code'] = grad_census['State_code'].apply(lambda x : 0 if x == '00' else int(x))

#What percentage of females in the age group 20-24 are illiterate in India, 
#i.e. out of all the females in the age group 20-24, what fraction is illiterate?
#littrate female where age-group == '20-24'

all_fem = grad_census.loc[(grad_census['Age-Group'] == '20-24') & (grad_census['State_code'] == 0) & (grad_census['Total/Rural/Urban'] == 'Total') ,'Female']
illit_fem = grad_census.loc[(grad_census['Age-Group'] == '20-24') & (grad_census['State_code'] == 0) & (grad_census['Total/Rural/Urban'] == 'Total') ,'Illit_female']
lit_per = (all_fem - illit_fem)/illit_fem

#Compare the literacy rates (i.e. the number of literates / total number of population) in each 
#age group and choose the correct option.

pd.pivot_table(grad_census[(grad_census['State_code'] != 0) & (grad_census['Total/Rural/Urban'] == 'Total') & (grad_census['Age-Group'] == 'All ages')], 
                           index = 'Age-Group',values = 'Liit_female' ,aggfunc = 'mean' )

a4_dims = (16.7, 8.27)
plt.subplots(figsize=a4_dims)
sns.barplot(x = grad_census['Age-Group'], y=grad_census['Liit_person'] )

litracy_rate['Female'].describe()
litracy_rate['Person'] = litracy_rate['Person'].astype('int32')

litracy_rate = grad_census.iloc[6,[14:]]

litracy_rate = grad_census.loc[:,['State_code','Area_name','Age-Group','Liit_person','Person','Total/Rural/Urban']]
litracy_rate = litracy_rate.loc[34:]

test = pd.pivot_table(litracy_rate,index = litracy_rate['Age-Group'],values = 'Liit_person',aggfunc = 'mean')

test = pd.pivot_table(litracy_rate[(litracy_rate['State_code'] != 0) & (litracy_rate['Total/Rural/Urban'] == 'Total') & (litracy_rate['Age-Group'] == 'All ages')], 
                           index = 'Area_name',values = ['Liit_person','Person'] ,aggfunc = 'mean' )

test['Lit_rate'] = (test['Liit_person']/test['Person'])*100




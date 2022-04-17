# -*- coding: utf-8 -*-
"""
Created on Fri Apr 15 19:36:54 2022

@author: hp
"""

import pandas as pd

#file_name=pd.read_csv('file.csv')---------format of read_csv

data=pd.read_csv('transaction.csv')

data=pd.read_csv('transaction.csv',sep=';')

# suumary of the data

data.info()

#CostPerTransaction = CostPerItem * NumberOfItemsPurchased
#variable= dataframe['column name']

CostPerItem = data['CostPerItem']
NumberOfItemsPurchased = data['NumberOfItemsPurchased']
CostPerTransaction = CostPerItem * NumberOfItemsPurchased

# Adding a new column to dataframe

data['CostPerTransaction']= CostPerTransaction
# Or

data['CostPerTransaction']= data['CostPerItem']* data['NumberOfItemsPurchased']

# Sales per Transaction

data['SalesPerTransaction']= data['SellingPricePerItem']* data['NumberOfItemsPurchased']

# Profit Calculation= Sales -  cost

data['ProfitPerTransaction'] = data['SalesPerTransaction']- data['CostPerTransaction']


#Markup= Profit/cost

data['MarkupPerTransaction']=data['ProfitPerTransaction']/data['CostPerTransaction']


# Rounding Markup

roundmarkup= round(data['MarkupPerTransaction'],2)

# Combining data fields

my_date='Day'+'-'+'Month'+'-'+'Year'

# Checking columns datatype

print(data['Day'].dtype)

# Change coulmn types

day=data['Day'].astype(str)
year=data['Year'].astype(str)

data['date']=day+'-'+data['Month']+'-'+year


# using iloc-(splits data into subset of data that we can view) to view specific column/rows

data.iloc[0]    # views the rows with index=0
data.iloc[0:3]  #first 3 rows
data.iloc[-5:]  #last 5 rows

data.head(5)     #first 5 rows
data.iloc[:,2]    #all rows and 2 column
data.iloc[4,2]    # 4th rows and 2nd column


# Using split to split the client keyword field
#new_var=column.str.split('sep',expand=True)

split_col=data['ClientKeywords'].str.split(',' , expand=True)

# Creating new columns for the split column in client keyword

data['ClientAge']=split_col[0]
data['clientType']=split_col[1]
data['LengthofContract']= split_col[2]

# Using the replace function

data['ClientAge']=data['ClientAge'].str.replace('[','')
data['LengthofContract']=data['LengthofContract'].str.replace(']','')
data['ItemDescription']=data['ItemDescription'].str.lower()

# How to merge files

# Bringing in new dataset

seasons=pd.read_csv('value_inc_seasons.csv',sep=';')

#merging files:merge_df=pd.merge(df_old,df_new,on='key')


data=pd.merge(data,seasons,on='Month')


# Dropping  columns

#df=df.drop('columname',axis = 1)

data=data.drop(['ClientKeywords','Year','Month','Day'],axis=1)


# Export into csv

data.to_csv('ValueInc_Cleaned.csv',index=False)  #index=False to remove index column

















































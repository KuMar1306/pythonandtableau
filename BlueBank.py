# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 11:13:03 2022

@author: hp
"""

import json
import pandas as pd

import numpy as np

import matplotlib.pyplot as plt # we will use only py plot

# Method 1 to read json data

json_file=open('loan_data_json.json')
data=json.load(json_file)

# Method 2 to read json data

with open('loan_data_json.json') as json_file:
    data=json.load(json_file)



# Transform to Data frame

loandata= pd.DataFrame(data)

# Finding unique values for the Purpose column

loandata['purpose'].unique() # shows values in purpose column

# Describing the data

loandata.describe()
loandata['int.rate'].describe()
loandata['fico'].describe()
loandata['dti'].describe()



# Using exp() to get the annual income

loandata['income']= np.exp(loandata['log.annual.inc'])


# Working with Arrays

arr=np.array([1,2,3,4])

# 0D array

arr=np.array(43)

# 2D array

arr=np.array([[1,2,3],[4,5,6]])

# Working with if statements
# Fico score

fico=700

# fico >= 300 and < 400:'Very Poor'
# fico >= 400 and ficoscore < 600:'Poor'
# fico >= 601 and ficoscore < 660:'Fair'
# fico >= 660 and ficoscore < 780:'Good'
# fico >=780:'Excellent'

if fico>=300 and fico<400:
    ficocat='Ver Poor'
elif fico>=400 and fico<600:
    ficocat='Poor'
elif fico>=601 and fico<660:
    ficocat='Fair'
elif fico>=660 and fico<780:
    ficocat='Good'
elif fico>=780:
    ficocat='Excellent'
else:
    ficocat='Unknown'
print(ficocat)


# For loop


fruits=['apple','cherry','banana','pear']

for x in fruits:
    print(x)
    y=x+' fruit'
    print(y)
    
for x in range(0,4):
    y=fruits[x]+ ' for sale'
    print(y)
    
    
# Applying for loop to load data

length=len(loandata)
fcat=[]
for x in range(0,length):
    category=loandata['fico'][x]
    if category>=300 and category<400:
        cat='Very Poor'
    elif category>=400 and category<600:
        cat='Poor'
    elif category>=601 and category<660:
        cat='Fair'
    elif category>=660 and category<780:
        cat='Good'
    elif category>=780:
        cat='Excellent'
    else:
        cat='Unknown'
    fcat.append(cat)  #to place new item from cat in the availbale space of fcat
fcat=pd.Series(fcat)
loandata['fico.category']=fcat

# While loop

i=1
while i<10:
    print(i)
    i=i+1
    

# df.loc as conditional statements
# df.loc[df[coulumnname] condition, newcolumnname]='value if condition is set'

# for interest rate, a new column is wanted, rate>0.12 then high, else low

loandata.loc[loandata['int.rate']>0.12,'int.rate.type']='High'
loandata.loc[loandata['int.rate']<=0.12,'int.rate.type']='Low'
    

# Number of loans/rows by fico.category

catplot=loandata.groupby(['fico.category']).size()  # size()-count the number of rows
catplot.plot.bar(color='green',width=0.1)
plt.show()


purposecount=loandata.groupby(['purpose']).size()
purposecount.plot.bar(color='red',width=0.3)
plt.show()


# Scatter plots

ypoint=loandata['income']
xpoint=loandata['dti']
plt.scatter(xpoint,ypoint, color='#4caf50')
plt.show()


# Writing to csv
loandata.to_csv('loan_cleaned.csv',index=True)
















    
    
















































    
    
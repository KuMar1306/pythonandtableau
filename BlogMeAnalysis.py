# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 20:07:15 2022

@author: hp
"""

import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Reading excel or xlsx files
data=pd.read_excel('articles.xlsx')

# summary of the data

data.describe()
data.info()

#counting the number of articles per source
#format of groupby: df.groupby(['column_to_group'])['column to count].count()

data.groupby(['source_id'])['article_id'].count()

#number of reaction by publisher

data.groupby(['source_id'])['engagement_reaction_count'].sum()

#dropping a column

data=data.drop('engagement_comment_plugin_count',axis=1) # axis=1 means we are referring to dropping a column

# Function in python

def thisfunction():
    print('This is my first function')
thisfunction()

#This is a function with variables

def aboutme(name):
    print('This is'+name)
    return name   # return whatever variable we have created
a=aboutme('Yashvi')

def aboutme(name,surname,location):
    print('This is'+name,'My surname is '+surname+ 'I am from' +location)
    return name,surname,location   # return whatever variable we have created
a=aboutme('Yashvi', 'Kumar', 'India')


# Using for loops in function

def favfood(food):
    for x in food:
        print('Top food is '+x)
        
fastfood=['burger','pizza','pie']

favfood(fastfood)

# Creating a keyword flag

# keyword='crash'
# length=len(data)
# key_flag=[]
# for x in range(0,length):
#     heading=data['title'][x]
#     if keyword in heading:
#         flag=1
#     else:
#         flag=0
#     key_flag.append(flag)

#Creating a function

def keywordflag(keyword):
    length=len(data)
    keyword_flag=[]
    for x in range(0,length):
        heading=data['title'][x]
        try:
            if keyword in heading:
                flag=1
            else:
                flag=0
        except:
            flag=0
        keyword_flag.append(flag)
    return keyword_flag

keywordflag=keywordflag('murder')

# Creating a new column in data dataframe

data['keywordflag']=pd.Series(keywordflag)

    
#SentimentIntensityAnalyzer

sent_int=SentimentIntensityAnalyzer() #initializes the class

text=data['title'][16]
sent=sent_int.polarity_scores(text)  # determine the sentiment

neg=sent['neg']
pos=sent['pos']
neu=sent['neu']

#adding a for loop to extract sentiment per title

title_neg_sentiment=[]
title_pos_sentiment=[]
title_neu_sentiment=[]

length=len(data)

for x in range(0,length):
    try:
        text=data['title'][x]
        sent_int=SentimentIntensityAnalyzer()
        sent=sent_int.polarity_scores(text)
        neg=sent['neg']
        pos=sent['pos']
        neu=sent['neu']
    except:
        neg=0
        pos=0
        neu=0
    title_neg_sentiment.append(neg)
    title_pos_sentiment.append(pos)
    title_neu_sentiment.append(neu)

title_neg_sentiment=pd.Series(title_neg_sentiment)
title_pos_sentiment=pd.Series(title_pos_sentiment)
title_neu_sentiment=pd.Series(title_neu_sentiment)
    
data['title_neg_sentiment']=title_neg_sentiment
data['title_pos_sentiment']=title_pos_sentiment
data['title_neu_sentiment']=title_neu_sentiment



#Writing the data

data.to_excel('blogme_clean.xlsx',sheet_name='blogmedata',index=False)

    
    
    
































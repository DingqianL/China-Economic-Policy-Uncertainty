# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 08:48:50 2021

@author: dingq
"""
import os
import pandas as pd

path = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete\2007_2016'
os.chdir(path)
files = os.listdir(path)
files = [f for f in files if f.endswith('.xlsx')]


counts_dup = []
counts_clean = []
dates = []

for i in files:
    date0 = i[6:14]
    dates.append(date0)
    df = pd.read_excel(i)
    df = df[['title']]
    counts_dup.append(len(df))
    df = df.drop_duplicates()
    counts_clean.append(len(df))
    
counts_2007_2016 = pd.DataFrame(data = {'date':dates, 'dup_count':counts_dup, 'count': counts_clean})
counts_2007_2016['date'] = pd.to_datetime(counts_2007_2016['date'])

counts_2007_2016['year'] = counts_2007_2016['date'].dt.year
counts_2007_2016['month'] = counts_2007_2016['date'].dt.month
counts_2007_2016['day'] = counts_2007_2016['date'].dt.day

'''
## to check if I downloaded all the counts for each day
check = counts_2007_2016.groupby(['year', 'month']).count()
check.to_csv(r'check counts.csv')
'''

counts_2007_2016.to_csv(r'counts_2007_2016.csv', index = False)





# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 19:47:42 2020

@author: dingq
"""

import os
import pandas as pd
import numpy as np
#import jieba
import re
import jieba.posseg as pseg


os.chdir(r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete')
rmrb49_06 = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete\rmrb1946_2006_full.txt'

with open(rmrb49_06, 'r+') as f:
    rmrb = f.read()

rmrb = rmrb.replace(' ', '')
rmrb = rmrb.replace('\n','')

datepattern=re.compile(r'\d{4}\.\d{2}\.\d{2}')
dates = re.findall(datepattern, rmrb)

artis = re.split(datepattern, rmrb)
artis = artis[1:]

for i in dates:
    if not i[0] in ['1','2']:
        print(i)
        del artis[dates.index(i)]
        del dates[dates.index(i)]



rmrb_frame = pd.DataFrame({'date':dates, 'article': artis})
rmrb_frame['date'] = pd.to_datetime(rmrb_frame['date'])

rmrb_frame['year'] = rmrb_frame['date'].dt.year

counts = rmrb_frame.groupby('year').count()
counts.to_excel(r'count the number of articles 1949_2006.xlsx')

rmrb07_16 = pd.read_excel(r'count2007_2016.xlsx')

rmrb07_16['date'] = pd.to_datetime(rmrb07_16['date'])
rmrb07_16['year'] = rmrb07_16['date'].dt.year

rmrb07_16_count = rmrb07_16.groupby('year').sum()

rmrb07_16_count.to_excel(r'count the number of articles 2007_2016.xlsx')



path1 = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\gmrb\2020'

folders = os.listdir(path1)
folders = [f for f in folders if not f.endswith('ini')]


for i in folders:
    date=folders #the folder of each date, there are 365 folders named after date
    counts=[]
    
    for i in folders:
        path11=os.path.join(path1,i) #path of each date
        artic=os.listdir(path11) #count the number of articles for each date
       # os.chdir(path1)
        count=len(artic)
        counts.append(count)


sum(counts)

### gmrb

os.chdir(r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\gmrb')

file = r'number of articles.csv'

gmrb_49_07 = pd.read_csv(file)

gmrb_49_07['date'] = pd.to_datetime(gmrb_49_07['date'])

gmrb_49_07['year'] = gmrb_49_07['date'].dt.year

gmrb_49_07_count = gmrb_49_07.groupby('year').sum()

gmrb_49_07_count.to_excel(r'gmrb count the number of ariticles per year.xlsx')


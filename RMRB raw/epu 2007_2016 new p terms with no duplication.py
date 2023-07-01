# -*- coding: utf-8 -*-
"""
Created on Thu Sept  9 6:25 2022

@author: dingq
"""

import re
import os
import pandas as pd
import sys
sys.path.append(r'C:\Users\dingq\AppData\Roaming\Python\Python39\site-packages')
import rexepu
#import datetime
#from datetime import timedelta

path = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\rmrb_E'
os.chdir(path)

file1 = 'econtxt.txt'
file2 = 'bustxt.txt'

with open(file1,'r+', encoding = 'utf8', errors='ignore') as f:
    text1=f.read()
text1 = text1.replace(' ', '') #delete space
text1 = text1.replace('\n','') #delete lines

with open(file2,'r+', encoding = 'utf8', errors='ignore') as f:
    text2=f.read()
text2 = text2.replace(' ', '') #delete space
text2 = text2.replace('\n','') #delete lines

text = text1+ '\n' + text2
#identify dates and split annual text into single article with date label
datepattern=re.compile(r'\d{4}\-\d{2}\-\d{2}')
match = re.split(datepattern, text) #split into single article

del match[-1]
"""del match[60356]
del match[165936]
del match[227002]"""

dateextract=re.findall(datepattern,text) #identify dates

"""del date[60356]
del date[165936]
del date[227002]"""

##to make sure the #of text matches that of date
if len(match)!=len(dateextract):
    print('Split Error!')
else:
    print('Congrats, no error in splitting!')

date = dateextract
##step2: generate epu index for each article with DataFrame
# put article and date into dataframe
articlelist=pd.DataFrame(data=match, index=date)
articlelist['date']=date

# save count of keywords into DataFrame
u1=rexepu.keywords(match,rexepu.pu1)
articlelist['u1']=u1
u2=rexepu.keywords(match,rexepu.pu2)
articlelist['u2']=u2
u3=rexepu.keywords(match,rexepu.pu3)
articlelist['u3']=u3
u4=rexepu.keywords(match,rexepu.pu4)
articlelist['u4']=u4
u5=rexepu.keywords(match,rexepu.pu5)
articlelist['u5']=u5
u6=rexepu.keywords(match,rexepu.pu6)
articlelist['u6']=u6
u7=rexepu.keywords(match,rexepu.pu7)
articlelist['u7']=u7
u8=rexepu.keywords(match,rexepu.pu8)
articlelist['u8']=u8
u9=rexepu.keywords(match,rexepu.pu9)
articlelist['u9']=u9
u10=rexepu.keywords(match,rexepu.pu10)
articlelist['u10']=u10

e1=rexepu.keywords(match,rexepu.pe1)
articlelist['e1']=e1
e2=rexepu.keywords(match,rexepu.pe2)
articlelist['e2']=e2

n3p1 = rexepu.keywords(match,rexepu.n3p1)
articlelist['n3p1'] = n3p1
n3p2 = rexepu.keywords(match,rexepu.n3p2)
articlelist['n3p2'] = n3p2
n3p3 = rexepu.keywords(match,rexepu.n3p3)
articlelist['n3p3'] = n3p3
n3p4 = rexepu.keywords(match,rexepu.n3p4)
articlelist['n3p4'] = n3p4
n3p5 = rexepu.keywords(match,rexepu.n3p5)
articlelist['n3p5'] = n3p5
n3p6 = rexepu.keywords(match,rexepu.n3p6)
articlelist['n3p6'] = n3p6
n3p7 = rexepu.keywords(match,rexepu.n3p7)
articlelist['n3p7'] = n3p7
n3p8 = rexepu.keywords(match,rexepu.n3p8)
articlelist['n3p8'] = n3p8

n2p1 = rexepu.keywords(match,rexepu.n2p1)
articlelist['n2p1'] = n2p1
n2p2 = rexepu.keywords(match,rexepu.n2p2)
articlelist['n2p2'] = n2p2
n2p3 = rexepu.keywords(match,rexepu.n2p3)
articlelist['n2p3'] = n2p3
n2p4 = rexepu.keywords(match,rexepu.n2p4)
articlelist['n2p4'] = n2p4
n2p5 = rexepu.keywords(match,rexepu.n2p5)
articlelist['n2p5'] = n2p5
n2p6 = rexepu.keywords(match,rexepu.n2p6)
articlelist['n2p6'] = n2p6
n2p7 = rexepu.keywords(match,rexepu.n2p7)
articlelist['n2p7'] = n2p7

n1p1 = rexepu.keywords(match,rexepu.n1p1)
articlelist['n1p1'] = n1p1
n1p2 = rexepu.keywords(match,rexepu.n1p2)
articlelist['n1p2'] = n1p2
n1p3 = rexepu.keywords(match,rexepu.n1p3)
articlelist['n1p3'] = n1p3
n1p4 = rexepu.keywords(match,rexepu.n1p4)
articlelist['n1p4'] = n1p4
n1p5 = rexepu.keywords(match,rexepu.n1p5)
articlelist['n1p5'] = n1p5

t1 =rexepu.keywords(match,rexepu.tp1)
articlelist['t1']=t1
t2 =rexepu.keywords(match,rexepu.tp2)
articlelist['t2']=t2
t3 =rexepu.keywords(match,rexepu.tp3)
articlelist['t3']=t3
t4 =rexepu.keywords(match,rexepu.tp4)
articlelist['t4']=t4
t5 =rexepu.keywords(match,rexepu.tp5)
articlelist['t5']=t5
t6 =rexepu.keywords(match,rexepu.tp6)
articlelist['t6']=t6
t7 =rexepu.keywords(match,rexepu.tp7)
articlelist['t7']=t7
t8 =rexepu.keywords(match,rexepu.tp8)
articlelist['t8']=t8
t9 =rexepu.keywords(match,rexepu.tp9)
articlelist['t9']=t9
t10 =rexepu.keywords(match,rexepu.tp10)
articlelist['t10']=t10
t11 =rexepu.keywords(match,rexepu.tp11)
articlelist['t11']=t11
t12 =rexepu.keywords(match,rexepu.tp12)
articlelist['t12']=t12
t13 =rexepu.keywords(match,rexepu.tp13)
articlelist['t13']=t13
t14 =rexepu.keywords(match,rexepu.tp14)
articlelist['t14']=t14
t15 =rexepu.keywords(match,rexepu.tp15)
articlelist['t15']=t15
t16 =rexepu.keywords(match,rexepu.tp16)
articlelist['t16']=t16
t17 =rexepu.keywords(match,rexepu.tp17)
articlelist['t17']=t17
t18 =rexepu.keywords(match,rexepu.tp18)
articlelist['t18']=t18    

###generate index epu
u = []
e = []
p1 = []
p2 = []
p3 = []
t = []
for i in range(len(match)):        
    if u1[i]>0 or \
       u2[i]>0 or \
       u3[i]>0 or \
       u4[i]>0 or \
       u5[i]>0 or \
       u6[i]>0 or \
       u7[i]>0 or \
       u8[i]>0 or \
       u9[i]>0 or \
       u10[i]>0:
           u0=1
           u.append(u0)
    else:
        u0=0
        u.append(u0)

for i in range(len(match)):
    if (e1[i]>0 or e2[i]>0):
        e0=1
        e.append(e0)
    else:
        e0=0
        e.append(e0)
    
for i in range(len(match)):        
    if n1p1[i]>0 or n1p2[i]>0 or n1p3[i]>0 or n1p4[i]>0 or n1p5[i]>0:
           p01=1
           p1.append(p01)
    else:
        p01=0
        p1.append(p01)

for i in range(len(match)):        
    if n2p1[i]>0 or n2p2[i]>0 or n2p3[i]>0 or n2p4[i]>0 or n2p5[i]>0 or n2p6[i]>0 or n2p7[i]>0:
           p02=1
           p2.append(p02)
    else:
        p02 = 0
        p2.append(p02)

for i in range(len(match)):        
    if n3p1[i]>0 or n3p2[i]>0 or n3p3[i]>0 or n3p4[i]>0 or n3p5[i]>0 or n3p6[i]>0 or n3p7[i]>0 or n3p8[i]>0:
           p03 = 1
           p3.append(p03)
    else:
        p03 = 0
        p3.append(p03)

for i in range(len(match)):        
    if t1[i]>0 or \
       t2[i]>0 or \
       t3[i]>0 or \
       t4[i]>0 or \
       t5[i]>0 or \
       t6[i]>0 or \
       t7[i]>0 or \
       t8[i]>0 or \
       t9[i]>0 or \
       t10[i]>0 or \
       t11[i]>0 or \
       t12[i]>0 or \
       t13[i]>0 or \
       t14[i]>0 or \
       t15[i]>0 or \
       t16[i]>0 or \
       t17[i]>0 or \
       t18[i]>0: 
           t0=1
           t.append(t0)
    else:
        t0=0
        t.append(t0)

epu1=[]
for i in range(len(match)):  
    if u[i]>0 and e[i]>0 and p1[i]>0:
        epu0=1
        epu1.append(epu0)
    else:
        epu0=0
        epu1.append(epu0)

epu2=[]
for i in range(len(match)):  
    if u[i]>0 and e[i]>0 and p2[i]>0:
        epu0=1
        epu2.append(epu0)
    else:
        epu0=0
        epu2.append(epu0)

epu3=[]
for i in range(len(match)):  
    if u[i]>0 and e[i]>0 and p3[i]>0:
        epu0=1
        epu3.append(epu0)
    else:
        epu0=0
        epu3.append(epu0)
 
if len(e)==len(p1)==len(p2)==len(p3)==len(u)==len(epu1)==len(epu2)==len(epu3)==len(match)==len(date):
    print('Pass')
else:
    print('Alert')
    
tpu=[]
for i in range(len(match)):  
    if u[i]>0 and e[i]>0 and t[i]>0:
        tpu0=1
        tpu.append(tpu0)
    else:
        tpu0=0
        tpu.append(tpu0)

#put epu index into DataFrame
articlelist['e']=e
articlelist['p1']=p1
articlelist['p2']=p2
articlelist['p3']=p3
articlelist['u']=u
articlelist['epu1']=epu1
articlelist['epu2']=epu2
articlelist['epu3']=epu3
articlelist['tpu'] = tpu

articlelist = articlelist.rename(columns={0:'match'})

articlelist['date'] = pd.to_datetime(articlelist['date'] )
articlelist = articlelist.sort_values(by='date')
articlelist['year'] = articlelist['date'].dt.year
articlelist['month'] = articlelist['date'].dt.month

articlelist = articlelist[['year', 'month','date','epu1','epu2','epu3','tpu']]

articlelist_count = pd.read_csv(r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete\count2007_2016.csv')
articlelist_count['date'] = pd.to_datetime(articlelist_count['date'])
articlelist_count = articlelist_count.sort_values(by='date')
articlelist_count['year'] = articlelist_count['date'].dt.year
articlelist_count['month'] = articlelist_count['date'].dt.month
articlelist_count = articlelist_count.groupby(['year','month']).sum()
articlelist_count.reset_index(inplace = True)


articlelist_sum = articlelist.groupby(['year','month']).sum()
articlelist_sum.reset_index(inplace = True)

articlelist_merge = pd.merge(articlelist_count, articlelist_sum, on = ['year', 'month'])

articlelist_merge['epu1_count'] = articlelist_merge['epu1']/articlelist_merge['count']
articlelist_merge['epu2_count'] = articlelist_merge['epu2']/articlelist_merge['count']
articlelist_merge['epu3_count'] = articlelist_merge['epu3']/articlelist_merge['count']
articlelist_merge['tpu_count'] = articlelist_merge['tpu']/articlelist_merge['count']

articlelist_merge.head(10)


# for era3

std1_e = articlelist_merge.epu1_count.std()
std2_e = articlelist_merge.epu2_count.std()
std3_e = articlelist_merge.epu3_count.std()
std3_t = articlelist_merge.tpu_count.std()

articlelist_merge['epu1_index'] = articlelist_merge.epu1_count/std1_e
articlelist_merge['epu2_index'] = articlelist_merge.epu2_count/std2_e
articlelist_merge['epu3_index'] = articlelist_merge.epu3_count/std3_e

articlelist_merge['tpu_index'] = articlelist_merge.tpu_count/std3_t

articlelist_merge['epu1_index'] = articlelist_merge['epu1_index']/articlelist_merge['epu1_index'].mean()*100
articlelist_merge['epu2_index'] = articlelist_merge['epu2_index']/articlelist_merge['epu2_index'].mean()*100
articlelist_merge['epu3_index'] = articlelist_merge['epu3_index']/articlelist_merge['epu3_index'].mean()*100

articlelist_merge['tpu_index'] = articlelist_merge['tpu_index']/articlelist_merge['tpu_index'].mean()*100


articlelist_merge.to_excel(r'epu tpu 2007_2016 new P term no_duplication_09092022.xlsx')



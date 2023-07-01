# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 16:34:44 2021

@author: dingq
"""

import os
import pandas as pd
import re
import rexepu

path = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete'
os.chdir(path)

folders = ['2017', '2018', '2019', '2020', '2021']

# to calculate articles per day
counts = []
for i in folders:
    path1 = os.path.join(path, i)
    days = os.listdir(path1)
    count = []
    for j in days:
        path2 = os.path.join(path1,j)
        count0 = len(os.listdir(path2))
        count.append(count0)
    counts.append(count)        
    
sums = [sum(f) for f in counts]


# to count articles that contain E 

# for RMRB
path = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete'
folders = ['2017', '2018', '2019', '2020', '2021']

dates = []
articles=[]

for m in folders:
    path0 = os.path.join(path, m)
    files = os.listdir(path0)
    for i in files:
        path11 = os.path.join(path0,i) #path of each date
        artic = os.listdir(path11) 
        artic = [f for f in artic if f.endswith('txt')]
        # os.chdir(path1)
        
        for j in artic:
            date0 = i
            path12 = os.path.join(path11,j) #path of each article within certain date
            with open (path12, 'r+', encoding='utf-8',errors='ignore') as f:
                article=f.read()
                article=article.replace(' ', '')
                article=article.replace('\n','')
                articles.append(article)
                dates.append(date0)

## count the dates
flat_articles = articles

articlelist=pd.DataFrame(data = flat_articles)
articlelist['date'] = dates
   

# save count of keywords into DataFrame
u1=rexepu.keywords(flat_articles,rexepu.pu1)
articlelist['u1']=u1
u2=rexepu.keywords(flat_articles,rexepu.pu2)
articlelist['u2']=u2
u3=rexepu.keywords(flat_articles,rexepu.pu3)
articlelist['u3']=u3
u4=rexepu.keywords(flat_articles,rexepu.pu4)
articlelist['u4']=u4
u5=rexepu.keywords(flat_articles,rexepu.pu5)
articlelist['u5']=u5
u6=rexepu.keywords(flat_articles,rexepu.pu6)
articlelist['u6']=u6
u7=rexepu.keywords(flat_articles,rexepu.pu7)
articlelist['u7']=u7
u8=rexepu.keywords(flat_articles,rexepu.pu8)
articlelist['u8']=u8
u9=rexepu.keywords(flat_articles,rexepu.pu9)
articlelist['u9']=u9
u10=rexepu.keywords(flat_articles,rexepu.pu10)
articlelist['u10']=u10

e1=rexepu.keywords(flat_articles,rexepu.pe1)
articlelist['e1']=e1
e2=rexepu.keywords(flat_articles,rexepu.pe2)
articlelist['e2']=e2

p1 =rexepu.keywords(flat_articles,rexepu.pp1)
articlelist['p1']=p1
p2 =rexepu.keywords(flat_articles,rexepu.pp2)
articlelist['p2']=p2
p3 =rexepu.keywords(flat_articles,rexepu.pp3)
articlelist['p3']=p3
p4 =rexepu.keywords(flat_articles,rexepu.pp4)
articlelist['p4']=p4
p5 =rexepu.keywords(flat_articles,rexepu.pp5)
articlelist['p5']=p5
p6 =rexepu.keywords(flat_articles,rexepu.pp6)
articlelist['p6']=p6
p7 =rexepu.keywords(flat_articles,rexepu.pp7)
articlelist['p7']=p7
p8 =rexepu.keywords(flat_articles,rexepu.pp8)
articlelist['p8']=p8
p9 =rexepu.keywords(flat_articles,rexepu.pp9)
articlelist['p9']=p9
p10 =rexepu.keywords(flat_articles,rexepu.pp10)
articlelist['p10']=p10
p11 =rexepu.keywords(flat_articles,rexepu.pp11)
articlelist['p11']=p11
p12 =rexepu.keywords(flat_articles,rexepu.pp12)
articlelist['p12']=p12
p13 =rexepu.keywords(flat_articles,rexepu.pp13)
articlelist['p13']=p13
p14 =rexepu.keywords(flat_articles,rexepu.pp14)
articlelist['p14']=p14
p15 =rexepu.keywords(flat_articles,rexepu.pp15)
articlelist['p15']=p15
p16 =rexepu.keywords(flat_articles,rexepu.pp16)
articlelist['p16']=p16
p17 =rexepu.keywords(flat_articles,rexepu.pp17)
articlelist['p17']=p17
p18 =rexepu.keywords(flat_articles,rexepu.pp18)
articlelist['p18']=p18 
p19 =rexepu.keywords(flat_articles,rexepu.pp19)
articlelist['p19']=p19

t1 =rexepu.keywords(flat_articles,rexepu.tp1)
articlelist['t1']=t1
t2 =rexepu.keywords(flat_articles,rexepu.tp2)
articlelist['t2']=t2
t3 =rexepu.keywords(flat_articles,rexepu.tp3)
articlelist['t3']=t3
t4 =rexepu.keywords(flat_articles,rexepu.tp4)
articlelist['t4']=t4
t5 =rexepu.keywords(flat_articles,rexepu.tp5)
articlelist['t5']=t5
t6 =rexepu.keywords(flat_articles,rexepu.tp6)
articlelist['t6']=t6
t7 =rexepu.keywords(flat_articles,rexepu.tp7)
articlelist['t7']=t7
t8 =rexepu.keywords(flat_articles,rexepu.tp8)
articlelist['t8']=t8
t9 =rexepu.keywords(flat_articles,rexepu.tp9)
articlelist['t9']=t9
t10 =rexepu.keywords(flat_articles,rexepu.tp10)
articlelist['t10']=t10
t11 =rexepu.keywords(flat_articles,rexepu.tp11)
articlelist['t11']=t11
t12 =rexepu.keywords(flat_articles,rexepu.tp12)
articlelist['t12']=t12
t13 =rexepu.keywords(flat_articles,rexepu.tp13)
articlelist['t13']=t13
t14 =rexepu.keywords(flat_articles,rexepu.tp14)
articlelist['t14']=t14
t15 =rexepu.keywords(flat_articles,rexepu.tp15)
articlelist['t15']=t15
t16 =rexepu.keywords(flat_articles,rexepu.tp16)
articlelist['t16']=t16
t17 =rexepu.keywords(flat_articles,rexepu.tp17)
articlelist['t17']=t17
t18 =rexepu.keywords(flat_articles,rexepu.tp18)
articlelist['t18']=t18    

#m1 =rexepu.keywords(flat_articles,rexepu.mp1)
#articlelist['m1']=m1
m2 =rexepu.keywords(flat_articles,rexepu.mp2)
articlelist['m2']=m2
m3 =rexepu.keywords(flat_articles,rexepu.mp3)
articlelist['m3']=m3
m4 =rexepu.keywords(flat_articles,rexepu.mp4)
articlelist['m4']=m4
m5 =rexepu.keywords(flat_articles,rexepu.mp5)
articlelist['m5']=m5
m6 =rexepu.keywords(flat_articles,rexepu.mp6)
articlelist['m6']=m6

###generate index epu
u=[]
e=[]
p=[]
t=[]
m=[]

for i in range(len(flat_articles)):        
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

for i in range(len(flat_articles)):
    if (e1[i]>0 or e2[i]>0):
        e0=1
        e.append(e0)
    else:
        e0=0
        e.append(e0)
    
for i in range(len(flat_articles)):        
    if p1[i]>0 or \
       p2[i]>0 or \
       p3[i]>0 or \
       p4[i]>0 or \
       p5[i]>0 or \
       p6[i]>0 or \
       p7[i]>0 or \
       p8[i]>0 or \
       p9[i]>0 or \
       p10[i]>0 or \
       p11[i]>0 or \
       p12[i]>0 or \
       p13[i]>0 or \
       p14[i]>0 or \
       p15[i]>0 or \
       p16[i]>0 or \
       p17[i]>0 or \
       p18[i]>0 or \
       p19[i]>0:
           p0=1
           p.append(p0)
    else:
        p0=0
        p.append(p0)

for i in range(len(flat_articles)):        
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
     #m1[i]>0 or \
for i in range(len(flat_articles)):        
    if m2[i]>0 or \
       m3[i]>0 or \
       m4[i]>0 or \
       m5[i]>0 or \
       m6[i]>0:
           m0=1
           m.append(m0)
    else:
        m0=0
        m.append(m0)
     
epu=[]
mpu=[]
tpu=[]
tepu=[]
mepu=[]   

for i in range(len(flat_articles)):  
    if u[i]>0 and e[i]>0 and p[i]>0:
        epu0=1
        epu.append(epu0)
    else:
        epu0=0
        epu.append(epu0)
 
for i in range(len(flat_articles)):  
    if u[i]>0 and e[i]>0 and t[i]>0:
        tpu0=1
        tpu.append(tpu0)
    else:
        tpu0=0
        tpu.append(tpu0)

for i in range(len(flat_articles)):  
    if u[i]>0 and e[i]>0 and p[i]>0 and t[i]>0:
        tepu0=1
        tepu.append(tepu0)
    else:
        tepu0=0
        tepu.append(tepu0)

for i in range(len(flat_articles)):  
    if u[i]>0 and e[i]>0 and m[i]>0:
        mpu0=1
        mpu.append(mpu0)
    else:
        mpu0=0
        mpu.append(mpu0)

for i in range(len(flat_articles)):  
    if u[i]>0 and e[i]>0 and p[i]>0 and m[i]>0:
        mepu0=1
        mepu.append(mepu0)
    else:
        mepu0=0
        mepu.append(mepu0)


if len(e)==len(p)==len(u)==len(epu)==len(mpu)==len(mepu)==len(tpu)==len(tepu)==len(flat_articles)==len(dates):
    print('Pass')
else:
    print('Alert')

#put epu index into DataFrame
articlelist['e']=e
articlelist['p']=p
articlelist['u']=u
articlelist['t']=t
articlelist['epu']=epu
articlelist['tpu']=tpu
articlelist['tepu']=tepu    
articlelist['mpu']=mpu
articlelist['mepu']=mepu    

banmian = re.compile(u'\d{2}版')

bans = []
cleans = []
for i in flat_articles: #50
    ban0 = ''.join(re.findall(banmian,i)[0])
    bans.append(ban0)
    cl = re.sub(u'\d{2}版', ' ', i)
    cl = re.sub(u'\s+', '', cl)

    cleans.append(cl)

articlelist['clean_match'] = cleans
articlelist['banmian'] = bans

articlelist=articlelist.rename(columns={0:'match'})

articlelist = articlelist.drop_duplicates(subset='clean_match', keep="first")

articlelist = articlelist[['match', 'date', 'e', 'p', 'u', 't', 'epu', 'tpu', 'tepu', 'mpu', 'mepu']]

articlelist['date1'] = pd.to_datetime(articlelist['date'], format = '%Y%m%d')

articlelist['year'] = articlelist['date1'].dt.year


sum1 = articlelist.groupby('year').sum()

sum1.to_excel(r'count for epu seperate categories.xlsx')





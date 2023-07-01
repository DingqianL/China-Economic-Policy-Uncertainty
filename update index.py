# -*- coding: utf-8 -*-
"""
Created on Fri May  3 10:09:33 2019

@author: dingq
"""

import os
import pandas as pd
import re
import sys
sys.path.append(r'C:\Users\dingq\AppData\Roaming\Python\Python39\site-packages')
import rexepu

# for RMRB
path1 = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete\2023'
folders = os.listdir(path1)

folders = [f for f in folders if not f.endswith('.ini')]

folders = folders[-28:]



for i in folders:
    date=folders #the folder of each date, there are 365 folders named after date
    counts=[]
    articles0=[]
    for i in folders:
       	path11=os.path.join(path1,i) #path of each date
        artic = os.listdir(path11) #count the number of articles for each date
        artic = [f for f in artic if f.endswith('.txt')]
        # os.chdir(path1)
        count = len(artic)
        counts.append(count)
        articles=[]
        for j in artic:
            path12=os.path.join(path11,j) #path of each article within certain date
            with open (path12, 'r+', encoding='utf-8',errors='ignore') as f:
                article=f.read()
                article=article.replace(' ', '')
                article=article.replace('\n','')
                articles.append(article)
        articles0.append(articles)

## count the dates
dates=[[f] for f in date]
cous=[]
for i in articles0:
    cou=len(i)
    cous.append(cou)

dates0=[a*b for a,b in zip(dates,cous)]
flat_articles = [item for sublist in articles0 for item in sublist]
flat_dates = [item for sublist in dates0 for item in sublist]
 
articlelist=pd.DataFrame(data=flat_articles)
articlelist['date']=flat_dates
   

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
#m2 =rexepu.keywords(flat_articles,rexepu.mp2)
#articlelist['m2']=m2
#m3 =rexepu.keywords(flat_articles,rexepu.mp3)
#articlelist['m3']=m3
#m4 =rexepu.keywords(flat_articles,rexepu.mp4)
#articlelist['m4']=m4
#m5 =rexepu.keywords(flat_articles,rexepu.mp5)
#articlelist['m5']=m5
#m6 =rexepu.keywords(flat_articles,rexepu.mp6)
#articlelist['m6']=m6

###generate index epu
u=[]
e=[]
p=[]
t=[]
#m=[]

for i in range(len(flat_articles)):        
    if u1[i]>0 or u2[i]>0 or u3[i]>0 or u4[i]>0 or u5[i]>0 or u6[i]>0 or u7[i]>0 or u8[i]>0 or u9[i]>0 or u10[i]>0:
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
    if p1[i]>0 or p2[i]>0 or p3[i]>0 or p4[i]>0 or p5[i]>0 or p6[i]>0 or p7[i]>0 or p8[i]>0 or p9[i]>0 or p10[i]>0 or p11[i]>0 or p12[i]>0 or p13[i]>0 or p14[i]>0 or p15[i]>0 or p16[i]>0 or p17[i]>0 or p18[i]>0 or p19[i]>0:
           p0=1
           p.append(p0)
    else:
        p0=0
        p.append(p0)

for i in range(len(flat_articles)):        
    if t1[i]>0 or t2[i]>0 or t3[i]>0 or t4[i]>0 or t5[i]>0 or t6[i]>0 or t7[i]>0 or t8[i]>0 or t9[i]>0 or t10[i]>0 or t11[i]>0 or t12[i]>0 or t13[i]>0 or t14[i]>0 or t15[i]>0 or t16[i]>0 or t17[i]>0 or t18[i]>0: 
           t0=1
           t.append(t0)
    else:
        t0=0
        t.append(t0)
     #m1[i]>0 or \


#for i in range(len(flat_articles)):        
 #   if m2[i]>0 or \
 #      m3[i]>0 or \
 #      m4[i]>0 or \
 #      m5[i]>0 or \
 #      m6[i]>0:
 #          m0=1
 #          m.append(m0)
 #   else:
 #       m0=0
 #       m.append(m0)
     
epu=[]
#mpu=[]
tpu=[]
#tepu=[]
#mepu=[]   

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

#for i in range(len(flat_articles)):  
#    if u[i]>0 and e[i]>0 and p[i]>0 and t[i]>0:
#        tepu0=1
#        tepu.append(tepu0)
#    else:
#        tepu0=0
#        tepu.append(tepu0)

#for i in range(len(flat_articles)):  
#    if u[i]>0 and e[i]>0 and m[i]>0:
#        mpu0=1
#        mpu.append(mpu0)
#    else:
#        mpu0=0
#        mpu.append(mpu0)

#for i in range(len(flat_articles)):  
#    if u[i]>0 and e[i]>0 and p[i]>0 and m[i]>0:
#        mepu0=1
#        mepu.append(mepu0)
#    else:
#        mepu0=0
#        mepu.append(mepu0)


if len(e)==len(p)==len(u)==len(epu)==len(tpu)==len(flat_articles)==len(flat_dates):
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
#articlelist['tepu']=tepu    
#articlelist['mpu']=mpu
#articlelist['mepu']=mepu    

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

   # path1=r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\csv_RMRB_20180904'
  #  path2=path1+'\\'+'all_epu'+year+'.xlsx'

#articlelist.to_excel(path2,encoding='utf8')

epu_test=articlelist.filter(['date','epu','tpu'],axis=1)
epu_test.head(10)

epu_test1=epu_test.groupby('date').sum()
epu_test1.head(10)

epu_test2=epu_test.groupby('date').size()
epu_test2.head(10)

epudailyrmrb=pd.concat([epu_test1,epu_test2],axis=1)
epudailyrmrb=epudailyrmrb.rename(columns={0:'count'})
epudailyrmrb.head(5)
len(epudailyrmrb)

#change date format
epudailyrmrb['date']=epudailyrmrb.index
epudailyrmrb['date']=pd.to_datetime(epudailyrmrb['date'])
#epudaily.drop('date', axis=1, inplace=True)
epudailyrmrb = epudailyrmrb.set_index('date')
epudailyrmrb.head(10)





###### for GMRB
path2 = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\gmrb\2023'

folders = os.listdir(path2)
folders = [f for f in folders if not f.endswith('.ini')]


folders = folders[-28:]
folders

for i in folders:
    date=folders #the folder of each date, there are 365 folders named after date
    counts=[]
    articles0=[]
    for i in folders:
        path21=os.path.join(path2,i) #path of each date
        artic=os.listdir(path21) #count the number of articles for each date
        artic = [f for f in artic if f.endswith('txt')]
       # os.chdir(path1)
        count=len(artic)
        counts.append(count)
        articles=[]
        for j in artic:
            path22=os.path.join(path21,j) #path of each article within certain date
            with open (path22, 'r+', encoding='utf-8',errors='ignore') as f:
                article=f.read()
                article=article.replace(' ', '')
                article=article.replace('\n','')
                articles.append(article)
        articles0.append(articles)

## count the dates
dates=[[f] for f in date]
cous=[]
for i in articles0:
    cou=len(i)
    cous.append(cou)

dates0=[a*b for a,b in zip(dates,cous)]
flat_articles = [item for sublist in articles0 for item in sublist]
flat_dates = [item for sublist in dates0 for item in sublist]
 
articlelist=pd.DataFrame(data=flat_articles)
articlelist['date']=flat_dates
   

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
#m2 =rexepu.keywords(flat_articles,rexepu.mp2)
#articlelist['m2']=m2
#m3 =rexepu.keywords(flat_articles,rexepu.mp3)
#articlelist['m3']=m3
#m4 =rexepu.keywords(flat_articles,rexepu.mp4)
#articlelist['m4']=m4
#m5 =rexepu.keywords(flat_articles,rexepu.mp5)
#articlelist['m5']=m5
#m6 =rexepu.keywords(flat_articles,rexepu.mp6)
#articlelist['m6']=m6

###generate index epu
u=[]
e=[]
p=[]
t=[]
#m=[]

for i in range(len(flat_articles)):        
    if u1[i]>0 or u2[i]>0 or u3[i]>0 or u4[i]>0 or u5[i]>0 or u6[i]>0 or u7[i]>0 or u8[i]>0 or u9[i]>0 or u10[i]>0:
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
    if p1[i]>0 or p2[i]>0 or p3[i]>0 or p4[i]>0 or p5[i]>0 or p6[i]>0 or p7[i]>0 or p8[i]>0 or p9[i]>0 or p10[i]>0 or p11[i]>0 or p12[i]>0 or p13[i]>0 or p14[i]>0 or p15[i]>0 or p16  [i]>0 or p17[i]>0 or p18[i]>0 or p19[i]>0:
           p0=1
           p.append(p0)
    else:
        p0=0
        p.append(p0)

for i in range(len(flat_articles)):        
    if t1[i]>0 or t2[i]>0 or t3[i]>0 or t4[i]>0 or t5[i]>0 or t6[i]>0 or t7[i]>0 or t8[i]>0 or t9[i]>0 or t10[i]>0 or t11[i]>0 or t12[i]>0 or t13[i]>0 or t14[i]>0 or t15[i]>0 or t16[i]>0 or t17[i]>0 or t18[i]>0: 
           t0=1
           t.append(t0)
    else:
        t0=0
        t.append(t0)
     #m1[i]>0 or \
#for i in range(len(flat_articles)):        
 #   if m2[i]>0 or \
  #     m3[i]>0 or \
   #    m4[i]>0 or \
    #   m5[i]>0 or \
     #  m6[i]>0:
      #     m0=1
       #    m.append(m0)
    #else:
     #   m0=0
  #      m.append(m0)
     
epu=[]
#mpu=[]
tpu=[]
#tepu=[]
#mepu=[]   

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

#for i in range(len(flat_articles)):  
#    if u[i]>0 and e[i]>0 and p[i]>0 and t[i]>0:
#        tepu0=1
#        tepu.append(tepu0)
#    else:
#        tepu0=0
#        tepu.append(tepu0)

#for i in range(len(flat_articles)):  
#    if u[i]>0 and e[i]>0 and m[i]>0:
#        mpu0=1
#        mpu.append(mpu0)
#    else:
#        mpu0=0
#        mpu.append(mpu0)

#for i in range(len(flat_articles)):  
#    if u[i]>0 and e[i]>0 and p[i]>0 and m[i]>0:
#        mepu0=1
#        mepu.append(mepu0)
#    else:
#        mepu0=0
#        mepu.append(mepu0)


if len(e)==len(p)==len(u)==len(epu)==len(tpu)==len(flat_articles)==len(flat_dates):
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
  
articlelist=articlelist.rename(columns={0:'match'})

banmian = re.compile(u'\d{2}版')

bans = []
cleans = []
for i in flat_articles:
    ban0 = ''.join(re.findall(banmian,i)[0])
    bans.append(ban0)
    cl = re.sub(u'\d{2}版', ' ', i)
    cl = re.sub(u'\s+', '', cl)
    cleans.append(cl)

articlelist['clean_match'] = cleans
articlelist['banmian'] = bans

articlelist=articlelist.rename(columns={0:'match'})

articlelist = articlelist.drop_duplicates(subset='clean_match', keep="first")


   # path1=r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\csv_RMRB_20180904'
  #  path2=path1+'\\'+'all_epu'+year+'.xlsx'

#articlelist.to_excel(path2,encoding='utf8')

epu_test=articlelist.filter(['date','epu','tpu'],axis=1)
epu_test.head(10)

epu_test1=epu_test.groupby('date').sum()
epu_test1.head(10)

epu_test2=epu_test.groupby('date').size()
epu_test2.head(10)

epudailygmrb=pd.concat([epu_test1,epu_test2],axis=1)
epudailygmrb=epudailygmrb.rename(columns={0:'count'})
epudailygmrb.head(5)
len(epudailygmrb)

#change date format
epudailygmrb['date']=epudailygmrb.index
epudailygmrb['date']=pd.to_datetime(epudailygmrb['date'])
#epudaily.drop('date', axis=1, inplace=True)
epudailygmrb = epudailygmrb.set_index('date')
epudailygmrb.head(10)

## combine these two
epudaily_update = epudailygmrb.join(epudailyrmrb, lsuffix='_gmrb', rsuffix='_rmrb')

epudaily_update.head()

path = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\rmrb_gmrb'
os.chdir(path)
epudaily_update.to_csv(r'update202302_join.csv')


## for daily 
#epu
epudailygmrb['epu_count'] = epudailygmrb['epu']/epudailygmrb['count']
epudailyrmrb['epu_count'] = epudailyrmrb['epu']/epudailyrmrb['count']

epudailygmrb['epu_sd'] = epudailygmrb['epu_count']/epudailygmrb['epu_count'].std()
epudailyrmrb['epu_sd'] = epudailyrmrb['epu_count']/epudailyrmrb['epu_count'].std()

epu_updated = (epudailygmrb['epu_sd']+epudailyrmrb['epu_sd'])/2

epu_update = pd.DataFrame(epu_updated)
epu_update['epu'] = (epu_update['epu_sd']/epu_update['epu_sd'].mean())*100
epu_update.to_csv(r'update2021_on_D_epu02.csv')

#tpu
epudailygmrb['tpu_count'] = epudailygmrb['tpu']/epudailygmrb['count']
epudailyrmrb['tpu_count'] = epudailyrmrb['tpu']/epudailyrmrb['count']

epudailygmrb['tpu_sd'] = epudailygmrb['tpu_count']/epudailygmrb['tpu_count'].std()
epudailyrmrb['tpu_sd'] = epudailyrmrb['tpu_count']/epudailyrmrb['tpu_count'].std()

epu_updated = (epudailygmrb['tpu_sd']+epudailyrmrb['tpu_sd'])/2

epu_update = pd.DataFrame(epu_updated)
epu_update['tpu'] = (epu_update['tpu_sd']/epu_update['tpu_sd'].mean())*100
epu_update.to_csv(r'update2023_on_D_tpu02.csv')
## for monthly

epudailygmrb['date']=epudailygmrb.index
epudailyrmrb['date']=epudailyrmrb.index

epudailygmrb['year'] = epudailygmrb['date'].dt.year
epudailyrmrb['year'] = epudailyrmrb['date'].dt.year

epudailygmrb['month'] = epudailygmrb['date'].dt.month
epudailyrmrb['month'] = epudailyrmrb['date'].dt.month

epudailygmrb['quarter'] = epudailygmrb['date'].dt.quarter
epudailyrmrb['quarter'] = epudailyrmrb['date'].dt.quarter

# monthly combing 2 newspapers
epudailygmrb_M = epudailygmrb.groupby(['year','month']).sum()
epudailyrmrb_M = epudailyrmrb.groupby(['year','month']).sum()

epudailygmrb_M = epudailygmrb_M[['epu','tpu','count']]
epudailyrmrb_M = epudailyrmrb_M[['epu','tpu','count']]

epudailygmrb_M['epu_count'] = epudailygmrb_M['epu']/epudailygmrb_M['count']
epudailyrmrb_M['epu_count'] = epudailyrmrb_M['epu']/epudailyrmrb_M['count']

epudailygmrb_M['tpu_count'] = epudailygmrb_M['tpu']/epudailygmrb_M['count']
epudailyrmrb_M['tpu_count'] = epudailyrmrb_M['tpu']/epudailyrmrb_M['count']


epudailygmrb_M['epu_sd'] = epudailygmrb_M['epu_count']/0.005363632
epudailyrmrb_M['epu_sd'] = epudailyrmrb_M['epu_count']/0.004338274

epudailygmrb_M['tpu_sd'] = epudailygmrb_M['tpu_count']/0.002504516
epudailyrmrb_M['tpu_sd'] = epudailyrmrb_M['tpu_count']/0.002502147


epu_updated_M = (epudailygmrb_M['epu_sd']+epudailyrmrb_M['epu_sd'])/2
tpu_updated_M = (epudailygmrb_M['tpu_sd']+epudailyrmrb_M['tpu_sd'])/2

epu_update_M  = pd.DataFrame(epu_updated_M )
tpu_update_M  = pd.DataFrame(tpu_updated_M )

epu_update_M ['epu'] = (epu_update_M ['epu_sd']/1.4395)*100
tpu_update_M ['tpu'] = (tpu_update_M ['tpu_sd']/0.700721)*100

del epu_update_M['epu_sd']
del tpu_update_M['tpu_sd']

epu_update_M.to_csv(r'update2019_on_M_epu202301.csv')
tpu_update_M.to_csv(r'update2019_on_M_tpu202301.csv')


## for quarterly

## update index for TPU      

articlelist[articlelist['epu']>0]['match'].to_excel(r'checknov_rmrb.xlsx')

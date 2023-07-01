# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 18:28:12 2020

@author: dingq
"""
import re
import os
import pandas as pd
import rexepu
import datetime
from datetime import timedelta

os.chdir(r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete')
file = r'rmrb1946_2006_full.txt'

with open(file,'r+',errors='ignore') as f:
    text=f.read()
text=text.replace(' ', '') #delete space
text=text.replace('\n','') #delete lines

#identify dates and split annual text into single article with date label
datepattern=re.compile(r'\d{4}\.\d{2}\.\d{2}')
match = re.split(datepattern, text) #split into single article
del match[0]
del match[60356]

del match[165936]

del match[227002]

dateextract=re.findall(datepattern,text) #identify dates

date=[i.replace('.','-') for i in dateextract] #formalize date
del date[60356]
del date[165936]
del date[227002]

##to make sure the #of text matches that of date
if len(match)!=len(date):
    print('Split Error!')
else:
    print('Congrats, no error in splitting!')

#the original file contains all the text in one txt file, I split them into independent txt files
#m=0
#while m<len(match):
#    if m<10:
#        n='00'+str(m)
#    elif 10<=m<100:
#        n='0'+str(m)
#    else:
#        n=str(m)
#    with open(date[m]+'-'+n+'.txt','w') as f:
 #       texts=f.write(match[m])
  #  m=m+1


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

p1 =rexepu.keywords(match,rexepu.pp1)
articlelist['p1']=p1
p2 =rexepu.keywords(match,rexepu.pp2)
articlelist['p2']=p2
p3 =rexepu.keywords(match,rexepu.pp3)
articlelist['p3']=p3
p4 =rexepu.keywords(match,rexepu.pp4)
articlelist['p4']=p4
p5 =rexepu.keywords(match,rexepu.pp5)
articlelist['p5']=p5
p6 =rexepu.keywords(match,rexepu.pp6)
articlelist['p6']=p6
p7 =rexepu.keywords(match,rexepu.pp7)
articlelist['p7']=p7
p8 =rexepu.keywords(match,rexepu.pp8)
articlelist['p8']=p8
p9 =rexepu.keywords(match,rexepu.pp9)
articlelist['p9']=p9
p10 =rexepu.keywords(match,rexepu.pp10)
articlelist['p10']=p10
p11 =rexepu.keywords(match,rexepu.pp11)
articlelist['p11']=p11
p12 =rexepu.keywords(match,rexepu.pp12)
articlelist['p12']=p12
p13 =rexepu.keywords(match,rexepu.pp13)
articlelist['p13']=p13
p14 =rexepu.keywords(match,rexepu.pp14)
articlelist['p14']=p14
p15 =rexepu.keywords(match,rexepu.pp15)
articlelist['p15']=p15
p16 =rexepu.keywords(match,rexepu.pp16)
articlelist['p16']=p16
p17 =rexepu.keywords(match,rexepu.pp17)
articlelist['p17']=p17
p18 =rexepu.keywords(match,rexepu.pp18)
articlelist['p18']=p18
p19 =rexepu.keywords(match,rexepu.pp19)
articlelist['p19']=p19

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
u=[]
e=[]
p=[]
t=[]

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

     
epu=[]
for i in range(len(match)):  
    if u[i]>0 and e[i]>0 and p[i]>0:
        epu0=1
        epu.append(epu0)
    else:
        epu0=0
        epu.append(epu0)
 
if len(e)==len(p)==len(u)==len(epu)==len(match)==len(date):
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
articlelist['e'] = e
articlelist['p'] = p
articlelist['u'] = u
articlelist['epu'] = epu
articlelist['tpu'] = tpu

articlelist=articlelist.rename(columns={0:'match'})


banmian = re.compile(u'(版次\：\d{1})|(【版面】第\d{0,2}版)|(<版次\>\=\d{2})')

bans = []
cleans = []

for i in match:
    try:
        ban0 = ''.join(re.findall(banmian,i)[0])
        bans.append(ban0)
        cl = re.sub(u'(版次\：\d{1})|(【版面】第\d{0,2}版)|(<版次\>\=\d{2})', ' ', i)
        cl = re.sub(u'\s+', '', cl)
        cleans.append(cl)
        
        
    except IndexError:
        bans.append(0)
        cleans.append(i)

articlelist['banmian'] = bans
articlelist['clean'] = cleans

#articlelist = articlelist.loc[articlelist['date'].apply(lambda x: x[0].isin(['1','2']))]

articlelist = articlelist.loc[articlelist['date'].apply(lambda x: x.startswith(('1','2')))]
## 1522231

articlelist = articlelist.loc[articlelist['banmian']!=0]

articlelist['date'] = pd.to_datetime(articlelist['date'])
articlelist['year'] = articlelist['date'].dt.year
articlelist['month'] = articlelist['date'].dt.month


articlelist0 = articlelist.groupby(['year','month']).count()
articlelist1 = articlelist.groupby(['year','month']).sum()

articlelist2 = pd.merge(articlelist0, articlelist1, left_index = True, right_index = True)
articlelist2 = articlelist2[['date','epu_y', 'tpu_y']]
articlelist2 = articlelist2.rename(columns = {'date':'count', 'epu_y':'epu','tpu_y':'tpu'})


articlelist_clean = articlelist.drop_duplicates(subset='clean', keep="first")
## 1495738
articlelist_clean = articlelist_clean[['year', 'month','date','epu','tpu']]

articlelist_clean = articlelist_clean.reset_index(drop = True)
articlelist_clean = articlelist_clean[['year', 'month','date','epu','tpu']]

articlelist_clean0 = articlelist_clean.groupby(['year','month']).count()
articlelist_clean1 = articlelist_clean.groupby(['year','month']).sum()

articlelist_clean2 = pd.merge(articlelist_clean0, articlelist_clean1, left_index = True, right_index = True)
articlelist_clean2 = articlelist_clean2[['date','epu_y', 'tpu_y']]
articlelist_clean2 = articlelist_clean2.rename(columns = {'date':'count', 'epu_y':'epu','tpu_y':'tpu'})
articlelist_clean2 = articlelist_clean2[['count', 'epu', 'tpu']]

articlelist_compare = pd.merge(articlelist2, articlelist_clean2, left_index = True, right_index = True,suffixes = ("_all","_clean"))

os.chdir(r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt')
articlelist_compare = articlelist_compare.reset_index(drop = False)
articlelist_compare.to_excel(r'validate fuplication rmrb_1949_2006.xlsx')


####
epu_test=articlelist.filter(['date','epu','e'],axis=1)
epu_test.head(10)

epu_test1=epu_test.groupby('date').sum()
epu_test1.head(10)

epu_test2=epu_test.groupby('date').size()
epu_test2.head(10)

epudaily=pd.concat([epu_test1,epu_test2],axis=1)
epudaily=epudaily.rename(columns={0:'count'})
epudaily.head(10)


epudaily['epu_count']=epudaily['epu']/epudaily['count']
epudaily['epu_econ']=epudaily['epu']/epudaily['e']

epudaily.head(10)
path3=r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\RMRB_compelete\epu'
epudaily.to_csv(os.path.join(path3,'epudaily'+file[:4]+'.csv'))

import os
import pandas as pd

folder = r'C:\Users\dingq\Documents\200_academic\220_Academic_My dissertation\225_data_txt\gmrb'

file = r'new term 2000-2007 eu.xlsx'
os.chdir(folder)
df = pd.read_excel(file, sheet_name='all')

df = df.dropna()
df.reset_index(inplace = True, drop = True)

df['date'] = pd.to_datetime(df['date'])

df = df.drop_duplicates()
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

df_epu = df.groupby(['year','month']).count()
df_epu.reset_index(inplace = True)
df_epu[['year', 'month']] = df_epu[['year', 'month']].astype(str)

df_count = pd.read_excel(r'count number of articles 2000_2018.xlsx')
df_count['date'] = df_count['date'].astype(str)
df_count['year'] = df_count['date'].apply(lambda x: x[:4])
df_count['month'] = df_count['date'].apply(lambda x: x[5:])

df_merge = pd.merge(df_epu, df_count, on = ['year', 'month'], how = 'left')
df_merge = df_merge.filter(['year', 'month', 'title', 'count'])

df_merge = df_merge.rename(columns = {'title': 'epu'})
df_merge = df_merge.fillna(method = 'bfill')

df_merge.to_excel(r'new p term 2000_2007.xlsx', index = False)



#%%
import pandas as pd 
%matplotlib inline
from datetime import datetime as dt
nmbs = pd.read_csv('persoonsongevallen/nmbs_tweets.csv')

#%%
nmbs.date.head()

#%%
nmbs.info(verbose=True)

#%%
nmbs.date.describe()

#%%
nmbs['year'] = pd.to_datetime(nmbs['date'], format = '%Y-%m-%d').dt.year

#%%
nmbs.year.unique()

#%%
nmbs.year.value_counts().sort_values(ascending=False)

#%%
nmbs['month'] = pd.to_datetime(nmbs['date'], format = '%Y-%m-%d').dt.month

#%%
nmbs.month.value_counts().sort_values(ascending=False)

#%%
maanden = nmbs.month.value_counts().reset_index()

#%%
maanden.rename(columns = {'index' : 'month', 'month' : 'count'}, inplace=True)

#%%
maanden.sort_values('month').plot.bar(x='month', y='count')

#%%
nmbs['day'] = pd.to_datetime(nmbs['date'], format = '%Y-%m-%d').dt.day

#%%
dagen = nmbs.day.value_counts().reset_index()

#%%
dagen.rename(columns = {'index' : 'day', 'day' : 'count'}, inplace=True)

#%%
dagen.plot.bar(x='day', y='count')

#%%
nmbs.day.hist(bins=60, grid=False)

#%%
nmbs.year.hist(bins=15, grid=False)

#%%
nmbs.month.hist(bins=40, grid=False)

#%%
c2015 = nmbs[nmbs.year == 2015]

#%%
c2015.month.hist(bins=40, grid=False)

#%%
c2015.month.value_counts()

#%%

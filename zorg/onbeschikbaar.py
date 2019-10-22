#%%
import pandas as pd
from datetime import datetime as dt
import os
%matplotlib inline

#%%
data = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/zorg/supplyproblems.csv'), parse_dates=['Supply Problem Start Date', 'Supply Problem End Date'])
data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')
data = data[data['human/veterinary'] == 'human']
data['name'] = data.name_medicinal_product.str.split().str.get(0)
data['start_year'] = pd.to_datetime(data.supply_problem_start_date, format='%Y-%m-%d').dt.year

#%%
data.info()

#%%
data.head()

#%%
no_end = data[data.supply_problem_end_date.isna()]

#%%
data.mah.nunique()

#%%
data.mah.value_counts().head()

#%%
data.start_year.hist()

#%%
data.supply_problem_reason.value_counts()

#%%
len(data[data.supply_problem_reason.isna()].index)

#%%
data.name.value_counts()

#%%
current = pd.read_csv(os.path.expanduser('~/Desktop/vrtnws_data/zorg/current.csv'), parse_dates=['SUPPLY PROBLEM START DATE', 'SUPPLY PROBLEM EXPECTED END DATE'])
current.columns = current.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')

#%%
current.info()

#%%
no_end.info()

#%%
no_end.cti_extended.value_counts()

#%%
changes = pd.read_csv('~/Desktop/vrtnws_data/zorg/changes.csv')
changes.columns = changes.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')

#%%
changes.info()

#%%
changes.cti_extended.value_counts()

#%%
import numpy as np
merged = pd.merge(no_end, current, on=['cti_extended', 'supply_problem_start_date'], how='left', indicator='exists')

#%%
both = merged[merged.exists == 'both']

#%%
both.info()

#%%

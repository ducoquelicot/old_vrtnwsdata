#%%
import pandas as pd 

changes = pd.read_csv('zorg/changes.csv')
changes2 = pd.read_csv('zorg/changes2310.csv')

#%%
changes.head()

#%%
pd.concat([changes, changes2]).loc[
    changes.index.symmetric_difference(changes2.index)
]
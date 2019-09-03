#%%
import pandas as pd
tim = pd.read_csv('timverheyden.csv')

#%%
tim.info()

#%%
niet_tim = tim[tim.username != 'timverheyden']

#%%
tim.info()

#%%
niet_tim.info()

#%%
niet_tim.to_csv('tweets_tim.csv')

#%%

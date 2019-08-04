#%%
import pandas as pd
%matplotlib inline
bevolking = pd.read_csv('nieuwe_buren/melted.csv')

#%%
bevolking.head()

#%%
gemeentes = bevolking[bevolking.gemeente.notna()]

#%%
gemeentes.info(verbose=True, null_counts=True)

#%%
gemeentes.info()

#%%
gemeentes.groupby(['gemeente', 'leeftijdsklasse', 'geslacht', 'nationaliteit', 'burgerlijke_staat', 'jaar']).aantal.max()

#%%
gem_2019 = gemeentes[gemeentes.jaar == 2019]

#%%
gem_2019.head()

#%%
gem_2019.groupby('gemeente').aantal.max().reset_index()

#%%
gem_2019 = gem_2019[gem_2019.leeftijdsklasse.notna()]

#%%
gem_2019 = gem_2019[gem_2019.geslacht.notna()]

#%%
gem_2019 = gem_2019[gem_2019.nationaliteit.notna()]

#%%
gem_2019 = gem_2019[gem_2019.burgerlijke_staat.notna()]

#%%
mode_values = gem_2019.loc[gem_2019.groupby('gemeente').aantal.idxmax()].reset_index()

#%%
mode_values.head(20)

#%%
mode_values.to_csv('nieuwe_buren/mode_gemeentes.csv', index=False)

#%%
gem_2009 = gemeentes[gemeentes.jaar == 2009]

#%%
gem_2009 = gem_2009[gem_2009.leeftijdsklasse.notna()]
gem_2009 = gem_2009[gem_2009.geslacht.notna()]
gem_2009 = gem_2009[gem_2009.nationaliteit.notna()]
gem_2009 = gem_2009[gem_2009.burgerlijke_staat.notna()]

#%%
gem_2009.head()

#%%
mode_values09 = gem_2009.loc[gem_2009.groupby('gemeente').aantal.idxmax()].reset_index()

#%%
mode_values09.head()

#%%
mode_values09.to_csv('nieuwe_buren/mode_gemeentes09.csv')

#%%

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

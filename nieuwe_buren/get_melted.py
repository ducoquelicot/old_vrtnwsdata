#%%
import pandas as pd 
%matplotlib inline
bevolking = pd.read_csv('nieuwe_buren/bevolking_leeft_gesl_nat_burgst20002019.csv', sep=';')

#%%
bevolking.info(verbose=True)

#%%
melted = bevolking.melt(id_vars=['land', 'gewest', 'provincie', 'arrondissement', 'gemeente', 'alle_leeftijden', 'leeftijdsklasse', 'mannen_en_vrouwen', 'geslacht', 'belgen_en_nietbelgen', 'nationaliteit', 'alle_burgerlijkestaten', 'burgerlijke_staat'],
value_vars=['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019'],
var_name='jaar', value_name='aantal')

#%%
melted.aantal = melted.aantal.fillna(0.0)

#%%
melted.aantal = melted.aantal.astype(int)

#%%
melted.head()

#%%
melted.jaar = melted.jaar.astype(int)

#%%
gemeentes = melted[melted.gemeente.notna()]

#%%
gemeentes.head()

#%%
gem_2019 = gemeentes[gemeentes.jaar == 2019]

#%%
gem_2019[gem_2019.leeftijdsklasse == '100 jaar en meer'].sort_values('aantal', ascending=False).head(10)

#%%
melted.to_csv('nieuwe_buren/melted.csv', index=False, chunksize=10000, encoding='utf-8')

#%%
melted.info(verbose=True, null_counts=)

#%%
melted.gemeente.unique()

#%%
melted.groupby(['gemeente', 'jaar'])['geslacht', 'nationaliteit', 'burgerlijke_staat'].apply(list)

#%%

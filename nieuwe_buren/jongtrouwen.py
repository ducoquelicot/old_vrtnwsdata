#%%
import pandas as pd 
%matplotlib inline
trouwen = pd.read_csv('nieuwe_buren/bevolking_leeftijd_burgst20092019.csv')

#%%
trouwen.info()

#%%
trouwen.columns = trouwen.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')

#%%
trouwen = trouwen.melt(id_vars=['belgië', 'gewest', 'provincie', 'arrondissement', 'gemeente', 'alle_leeftijden', 'leeftijdsklasse', 'alle_burgerlijke_staten', 'burgerlijke_staat'],
value_vars=['bevolking_op_01_januari_2009', 'bevolking_op_01_januari_2010', 'bevolking_op_01_januari_2011', 'bevolking_op_01_januari_2012', 'bevolking_op_01_januari_2013', 'bevolking_op_01_januari_2014', 'bevolking_op_01_januari_2015', 'bevolking_op_01_januari_2016', 'bevolking_op_01_januari_2017', 'bevolking_op_01_januari_2018', 'bevolking_op_01_januari_2019'],
var_name='jaar', value_name='aantal')

#%%
trouwen.aantal = trouwen.aantal.fillna(0.0)
trouwen.aantal = trouwen.aantal.astype(int)
trouwen.jaar = trouwen.jaar.str.replace('bevolking_op_01_januari_', '')
trouwen.jaar = trouwen.jaar.astype(int)

#%%
trouwen.head()

#%%
trouwen.leeftijdsklasse.unique()

#%%
leeftijden = ['Minder dan 5 jaar', 'Van 5 tot 9 jaar', 'Van 10 tot 14 jaar', 'Van 15 tot 19 jaar', 'Van 20 tot 24 jaar']
jaar19 = [2019]
gehuwd = ['Gehuwd']
jong_gehuwd19 = trouwen[trouwen.leeftijdsklasse.isin(leeftijden) & trouwen.jaar.isin(jaar19) & trouwen.gemeente.notna() & trouwen.burgerlijke_staat.isin(gehuwd) & (trouwen.aantal != 0)]
jong_gehuwd19 = jong_gehuwd19.groupby(['gemeente', 'leeftijdsklasse', 'burgerlijke_staat']).agg({'aantal' : 'sum'})

#%%
jong_gehuwd19.head()

#%%
som_jong = jong_gehuwd19.groupby(level=0).agg({'aantal' : 'sum'})

#%%
som_jong.head()

#%%
som_jong.sort_values('aantal', ascending=False).head(10)

#%%
kindjes = ['Van 15 tot 19 jaar' , 'Van 10 tot 14 jaar']
extra_jong = trouwen[(trouwen.leeftijdsklasse.isin(kindjes)) & trouwen.gemeente.notna() & (trouwen.jaar == 2019) & (trouwen.burgerlijke_staat == 'Gehuwd') & trouwen.aantal.notna()]

#%%
extra_jong[(extra_jong.leeftijdsklasse == 'Van 10 tot 14 jaar') & (extra_jong.aantal != 0)]

#%%
totaal = trouwen[trouwen.gemeente.notna() & trouwen.leeftijdsklasse.isna() & (trouwen.jaar == 2019)]

#%%
som_jong = som_jong.reset_index()

#%%
totaal = totaal.groupby('gemeente')['aantal'].sum().reset_index()

#%%
merged = som_jong.merge(totaal, on='gemeente')

#%%
merged.rename(columns = {'aantal_x' : 'aantal', 'aantal_y' : 'bevolking'}, inplace=True)

#%%
merged['percentage'] = merged['aantal']/merged['bevolking'] * 100

#%%
merged.percentage = merged.percentage.round(1)

#%%
merged.sort_values('percentage', ascending=False).head(10)

#%%
merged[['percentage']].hist(bins=30)

#%%
merged.sort_values('percentage', ascending=False).head(10)

#%%
leeftijden = ['Minder dan 5 jaar', 'Van 5 tot 9 jaar', 'Van 10 tot 14 jaar', 'Van 15 tot 19 jaar', 'Van 20 tot 24 jaar']
jaar09 = [2009]
gehuwd = ['Gehuwd']
jong_gehuwd09 = trouwen[trouwen.leeftijdsklasse.isin(leeftijden) & trouwen.jaar.isin(jaar09) & trouwen.gemeente.notna() & trouwen.burgerlijke_staat.isin(gehuwd) & (trouwen.aantal != 0)]
jong_gehuwd09 = jong_gehuwd09.groupby(['gemeente', 'leeftijdsklasse', 'burgerlijke_staat']).agg({'aantal' : 'sum'})

#%%
som_jong09 = jong_gehuwd09.groupby(level=0).agg({'aantal' : 'sum'}).reset_index()

#%%
totaal09 = trouwen[trouwen.gemeente.notna() & trouwen.leeftijdsklasse.isna() & (trouwen.jaar == 2009)]

#%%
totaal09 = totaal09.groupby('gemeente')['aantal'].sum().reset_index()

#%%
merged09 = som_jong09.merge(totaal09, on='gemeente')
merged09.rename(columns = {'aantal_x' : 'aantal', 'aantal_y' : 'bevolking'}, inplace=True)
merged09['percentage'] = merged09['aantal']/merged09['bevolking'] * 100
merged09.percentage = merged09.percentage.round(1)

#%%
merged09.head()

#%%
merged09[['percentage']].hist(bins=60)

#%%
merged09.sort_values('percentage', ascending=False).head(10)

#%%
leeftijden = ['Minder dan 5 jaar', 'Van 5 tot 9 jaar', 'Van 10 tot 14 jaar', 'Van 15 tot 19 jaar', 'Van 20 tot 24 jaar']
alle_jaren = trouwen[trouwen.gewest.isna() & trouwen.provincie.isna() & trouwen.arrondissement.isna() & trouwen.gemeente.isna() & trouwen.leeftijdsklasse.isin(leeftijden) & (trouwen.burgerlijke_staat == 'Gehuwd')]
alle_jaren = alle_jaren.groupby('jaar')['aantal'].sum().reset_index()

#%%
alle_jaren.set_index('jaar').plot(ylim=(0,50000), title='Aantal jonggehuwden 2009-2019')

#%%
leeftijden = ['Minder dan 5 jaar', 'Van 5 tot 9 jaar', 'Van 10 tot 14 jaar', 'Van 15 tot 19 jaar', 'Van 20 tot 24 jaar']
jaar18 = [2018]
gehuwd = ['Gehuwd']
jong_gehuwd18 = trouwen[trouwen.leeftijdsklasse.isin(leeftijden) & trouwen.jaar.isin(jaar18) & trouwen.gemeente.notna() & trouwen.burgerlijke_staat.isin(gehuwd) & (trouwen.aantal != 0)]
jong_gehuwd18 = jong_gehuwd18.groupby(['gemeente', 'leeftijdsklasse', 'burgerlijke_staat']).agg({'aantal' : 'sum'})

#%%
som_jong18 = jong_gehuwd18.groupby(level=0).agg({'aantal' : 'sum'}).reset_index()

#%%
totaal18 = trouwen[trouwen.gemeente.notna() & trouwen.leeftijdsklasse.isna() & (trouwen.jaar == 2018)]
totaal18 = totaal18.groupby('gemeente')['aantal'].sum().reset_index()

#%%
merged18 = som_jong18.merge(totaal18, on='gemeente')
merged18.rename(columns = {'aantal_x' : 'aantal', 'aantal_y' : 'bevolking'}, inplace=True)
merged18['percentage'] = merged18['aantal']/merged18['bevolking'] * 100
merged18.percentage = merged18.percentage.round(1)

#%%
merged18[['percentage']].hist(bins=30)

#%%
merged18.sort_values('percentage', ascending=False).head(10)

#%%
leeftijden = ['Minder dan 5 jaar', 'Van 5 tot 9 jaar', 'Van 10 tot 14 jaar', 'Van 15 tot 19 jaar', 'Van 20 tot 24 jaar']
stjoost = trouwen[(trouwen.gemeente == 'Sint-Joost-ten-Node') & trouwen.leeftijdsklasse.isin(leeftijden) & (trouwen.burgerlijke_staat == 'Gehuwd')]

#%%
stjoost.groupby('jaar').agg({'aantal' : 'sum'}).plot(ylim=(0,700), title='Aantal jonggehuwden in St-Joost 2009-2019')

#%%
som_jong.head()

#%%
nationaliteit = pd.read_csv('nieuwe_buren/bevolking_nationaliteit20002019.csv')

#%%
nationaliteit = nationaliteit[nationaliteit.gemeente.notna() & (nationaliteit.nationaliteit == 'niet-Belgen') & (nationaliteit.jaar == 2019)]

#%%
nationaliteit = nationaliteit[['gemeente', 'aantal']]

#%%
nationaliteit = nationaliteit.reset_index(drop=True)

#%%
correlatie = som_jong.merge(nationaliteit, on='gemeente')

#%%
correlatie.rename(columns = {'aantal_x' : 'jonggehuwden', 'aantal_y' : 'nietbelgen'}, inplace=True)

#%%
correlatie = correlatie.set_index('gemeente')

#%%
correlatie.corr()

#%%
merged.head()

#%%
percentage = merged[['gemeente', 'percentage']]

#%%
percentage.head()

#%%
nationaliteit.head()

#%%
nietbelgen = nationaliteit[nationaliteit.gemeente.notna() & (nationaliteit.jaar == 2019) & (nationaliteit.nationaliteit == 'niet-Belgen')]

#%%
totaal = nationaliteit[nationaliteit.gemeente.notna() & nationaliteit.nationaliteit.isna() & (nationaliteit.jaar == 2019)]

#%%
nietbelgen = nietbelgen[['gemeente', 'aantal']]
totaal = totaal[['gemeente', 'aantal']]

#%%
merged2 = nietbelgen.merge(totaal, on='gemeente')

#%%
merged2.rename(columns = {'aantal_x' : 'nietbelgen', 'aantal_y' : 'bevolking'}, inplace=True)

#%%
merged2['percentage'] = merged2['nietbelgen']/merged2['bevolking'] * 100
merged2.percentage = merged2.percentage.round(1)

#%%
merged2 = merged2[['gemeente', 'percentage']]

#%%
ratio = percentage.merge(merged2, on='gemeente')

#%%
ratio.rename(columns = {'percentage_x' : 'jonggehuwd', 'percentage_y' : 'nietbelgen'}, inplace=True)

#%%
ratio.set_index('gemeente').corr()

#%%
nats = pd.read_csv('nieuwe_buren/bev_nat_ges9219tot.csv')
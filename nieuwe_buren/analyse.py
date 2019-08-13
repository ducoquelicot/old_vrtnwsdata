#%%
import pandas as pd
%matplotlib inline
kenmerken = pd.read_csv('nieuwe_buren/melted.csv')
burgerlijke_staat = pd.read_csv('nieuwe_buren/bevolking_burgerlijkestand20002019.csv')
geslacht = pd.read_csv('nieuwe_buren/bevolking_geslacht20002019.csv')
leeftijdsklasse = pd.read_csv('nieuwe_buren/bevolking_leeftijdsklasse20002019.csv')
nationaliteit = pd.read_csv('nieuwe_buren/bevolking_nationaliteit20002019.csv')
mode_gemeentes = pd.read_csv('nieuwe_buren/mode_gemeentes0919.csv')
bevolking = pd.read_csv('nieuwe_buren/bevolking0919.csv')

#%%
kenmerken.head()

#%%
gemeentes = kenmerken[kenmerken.gemeente.notna()]

#%%
gemeentes.info()

#%%
gemeentes.groupby(['gemeente', 'leeftijdsklasse', 'geslacht', 'nationaliteit', 'burgerlijke_staat', 'jaar']).aantal.max()

#%%
gem_2019 = gemeentes[gemeentes.jaar == 2019]

#%%
gem_2019 = gem_2019[gem_2019.leeftijdsklasse.notna()]
gem_2019 = gem_2019[gem_2019.geslacht.notna()]
gem_2019 = gem_2019[gem_2019.nationaliteit.notna()]
gem_2019 = gem_2019[gem_2019.burgerlijke_staat.notna()]

#%%
mode_values = gem_2019.loc[gem_2019.groupby('gemeente').aantal.idxmax()].reset_index()

#%%
mode_values.head()

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
mode_values09 = gem_2009.loc[gem_2009.groupby('gemeente').aantal.idxmax()].reset_index()

#%%
mode_values09.to_csv('nieuwe_buren/mode_gemeentes09.csv', index=False)

#%%
leeftijdsklasse.columns = leeftijdsklasse.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')

#%%
leeftijdsklasse = leeftijdsklasse.melt(id_vars=['belgië', 'gewest', 'provincie', 'arrondissement', 'gemeente', 'alle_leeftijden', 'leeftijdsklasse'],
value_vars=['bevolking_op_01_januari_2000', 'bevolking_op_01_januari_2001', 'bevolking_op_01_januari_2002', 'bevolking_op_01_januari_2003', 'bevolking_op_01_januari_2004', 'bevolking_op_01_januari_2005', 'bevolking_op_01_januari_2006', 'bevolking_op_01_januari_2007', 'bevolking_op_01_januari_2008', 'bevolking_op_01_januari_2009', 'bevolking_op_01_januari_2010', 'bevolking_op_01_januari_2011', 'bevolking_op_01_januari_2012', 'bevolking_op_01_januari_2013', 'bevolking_op_01_januari_2014', 'bevolking_op_01_januari_2015', 'bevolking_op_01_januari_2016', 'bevolking_op_01_januari_2017', 'bevolking_op_01_januari_2018', 'bevolking_op_01_januari_2019'],
var_name='jaar', value_name='aantal')

#%%
leeftijdsklasse.aantal = leeftijdsklasse.aantal.fillna(0.0)
leeftijdsklasse.aantal = leeftijdsklasse.aantal.astype(int)
leeftijdsklasse.jaar = leeftijdsklasse.jaar.str.replace('bevolking_op_01_januari_', '')
leeftijdsklasse.jaar = leeftijdsklasse.jaar.astype(int)

#%%
leeftijdsklasse.to_csv('nieuwe_buren/bevolking_leeftijdsklasse20002019.csv', index=False)

#%%
leeftijdsklasse.head()

#%%
gem_lft = leeftijdsklasse[leeftijdsklasse.gemeente.notna()]

#%%
honderd = gem_lft[gem_lft.leeftijdsklasse == '100 jaar en meer']

#%%
years = [2009, 2019]
honderd0919 = honderd[honderd.jaar.isin(years)].reset_index(drop=True)

#%%
honderd0919[honderd0919.jaar == 2009].sort_values('aantal', ascending=False).head(10)

#%%
honderd0919[honderd0919.jaar == 2019].sort_values('aantal', ascending=False).head(10)

#%%
jaren = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
leeftijd = ['100 jaar en meer']
leeftijdsklasse[leeftijdsklasse.leeftijdsklasse.isin(leeftijd) & leeftijdsklasse.gemeente.isna() & leeftijdsklasse.arrondissement.isna() & leeftijdsklasse.provincie.isna() & leeftijdsklasse.gewest.isna() & leeftijdsklasse.jaar.isin(jaren)]

#%%
jaar = [2019]
leeftijdsklasse[leeftijdsklasse.jaar.isin(jaar) & leeftijdsklasse.leeftijdsklasse.isin(leeftijd) & leeftijdsklasse.gewest.notna() & leeftijdsklasse.provincie.isna() & leeftijdsklasse.arrondissement.isna() & leeftijdsklasse.gemeente.isna()].sort_values('aantal', ascending=False)

#%%
jaar = [2019]
leeftijdsklasse[leeftijdsklasse.jaar.isin(jaar) & leeftijdsklasse.leeftijdsklasse.isin(leeftijd) & leeftijdsklasse.gewest.notna() & leeftijdsklasse.provincie.notna() & leeftijdsklasse.arrondissement.isna() & leeftijdsklasse.gemeente.isna()].sort_values('aantal', ascending=False)

#%%
import matplotlib.ticker as ticker

#%%
leeftijd = ['100 jaar en meer']
jaren = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
over_time = leeftijdsklasse[leeftijdsklasse.leeftijdsklasse.isin(leeftijd) & leeftijdsklasse.gemeente.isna() & leeftijdsklasse.arrondissement.isna() & leeftijdsklasse.provincie.isna() & leeftijdsklasse.gewest.isna() & leeftijdsklasse.jaar.isin(jaren)].reset_index(drop=True)
over_time = over_time[['jaar', 'aantal']]
over_time = over_time.set_index('jaar')
ot_plot = over_time.plot(title='Honderdjarigen van 2009 tot 2019', ylim=(0,2500))
ot_plot.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

#%%
bevolking.columns = bevolking.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')

#%%
bevolking = bevolking.melt(id_vars=['belgië', 'gewest', 'provincie', 'arrondissement', 'gemeente'],
value_vars=['bevolking_op_01_januari_2009', 'bevolking_op_01_januari_2010', 'bevolking_op_01_januari_2011', 'bevolking_op_01_januari_2012', 'bevolking_op_01_januari_2013', 'bevolking_op_01_januari_2014', 'bevolking_op_01_januari_2015', 'bevolking_op_01_januari_2016', 'bevolking_op_01_januari_2017', 'bevolking_op_01_januari_2018', 'bevolking_op_01_januari_2019'],
var_name='jaar', value_name='aantal')

#%%
bevolking.aantal = bevolking.aantal.fillna(0.0)
bevolking.aantal = bevolking.aantal.astype(int)
bevolking.jaar = bevolking.jaar.str.replace('bevolking_op_01_januari_', '')
bevolking.jaar = bevolking.jaar.astype(int)

#%%
bevolking.to_csv('nieuwe_buren/bevolking0919.csv', index=False)

#%%
jaar = [2019]
bevolking19 = bevolking[bevolking.jaar.isin(jaar) & bevolking.gemeente.notna()]
bevolking19 = bevolking19[['gemeente', 'jaar', 'aantal']].reset_index(drop=True)

#%%
bevolking19.sort_values('aantal', ascending=False).head(10).set_index('gemeente').drop(['jaar'], axis=1).plot.barh(title='Grootste gemeenten in 2019')

#%%
jaar = [2009]
bevolking09 = bevolking[bevolking.jaar.isin(jaar) & bevolking.gemeente.notna()]
bevolking09[['gemeente', 'jaar', 'aantal']].reset_index(drop=True).sort_values('aantal', ascending=False).head(10).set_index('gemeente').drop('jaar', axis=1).plot.barh(title='Grootste gemeenten in 2009')

#%%
honderd19 = honderd0919[honderd0919.jaar == 2019]
honderd19 = honderd19[['gemeente', 'jaar', 'aantal']].reset_index(drop=True)

#%%
honderd19.sort_values('aantal', ascending=False).head(10).set_index('gemeente').drop(['jaar'], axis=1).plot.barh(title='Gemeentes met meeste 100+ in 2019')

#%%
honderd09 = honderd0919[honderd0919.jaar == 2009]
honderd09 = honderd09[['gemeente', 'jaar', 'aantal']].reset_index(drop=True)
honderd09.sort_values('aantal', ascending=False).head(10).set_index('gemeente').drop(['jaar'], axis=1).plot.barh(title='Gemeentes met meeste 100+ in 2009')

#%%
nationaliteit.info(verbose=True)

#%%
nationaliteit.columns = nationaliteit.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')

#%%
nationaliteit = nationaliteit.melt(id_vars=['belgië', 'gewest', 'provincie', 'arrondissement', 'gemeente', 'belgen_en_nietbelgen', 'nationaliteit'],
value_vars=['bevolking_op_01_januari_2000', 'bevolking_op_01_januari_2001', 'bevolking_op_01_januari_2002', 'bevolking_op_01_januari_2003', 'bevolking_op_01_januari_2004', 'bevolking_op_01_januari_2005', 'bevolking_op_01_januari_2006', 'bevolking_op_01_januari_2007', 'bevolking_op_01_januari_2008', 'bevolking_op_01_januari_2009', 'bevolking_op_01_januari_2010', 'bevolking_op_01_januari_2011', 'bevolking_op_01_januari_2012', 'bevolking_op_01_januari_2013', 'bevolking_op_01_januari_2014', 'bevolking_op_01_januari_2015', 'bevolking_op_01_januari_2016', 'bevolking_op_01_januari_2017', 'bevolking_op_01_januari_2018', 'bevolking_op_01_januari_2019'],
var_name='jaar', value_name='aantal')

#%%
nationaliteit.aantal = nationaliteit.aantal.fillna(0.0)
nationaliteit.aantal = nationaliteit.aantal.astype(int)
nationaliteit.jaar = nationaliteit.jaar.str.replace('bevolking_op_01_januari_', '')
nationaliteit.jaar = nationaliteit.jaar.astype(int)

#%%
nationaliteit.to_csv('nieuwe_buren/bevolking_nationaliteit20002019.csv', index=False)

#%%
jaar = [2019]
nationaliteit19 = nationaliteit[nationaliteit.jaar.isin(jaar) & nationaliteit.gemeente.notna() & nationaliteit.nationaliteit.notna()].reset_index(drop=True)

#%%
nationaliteit19.head()

#%%
mode_nationaliteit = nationaliteit19.loc[nationaliteit19.groupby('gemeente').aantal.idxmax()].reset_index(drop=True)

#%%
mode_nationaliteit[mode_nationaliteit.nationaliteit != 'Belgen']

#%%
nationaliteit19[nationaliteit19.nationaliteit != 'Belgen'].sort_values('aantal', ascending=False).reset_index(drop=True).head(10).set_index('gemeente').drop(['belgië', 'gewest', 'provincie', 'belgen_en_nietbelgen', 'nationaliteit', 'jaar'], axis=1).plot.barh(title='Gemeentes met meeste niet-Belgen in 2019')

#%%
bevolking19.sort_values('aantal', ascending=False).head(10).set_index('gemeente').drop(['jaar'], axis=1).plot.barh(title='Grootste gemeenten in 2019')

#%%
belgen = ['Belgen']
jaar = [2019]
nationaliteit[nationaliteit.jaar.isin(jaar) & ~nationaliteit.nationaliteit.isin(belgen) & nationaliteit.gemeente.isna() & nationaliteit.nationaliteit.notna() & nationaliteit.arrondissement.notna()].reset_index(drop=True).sort_values('aantal', ascending=False).head(10)

#%%
belgen = ['Belgen']
jaar = [2019]
nationaliteit[nationaliteit.jaar.isin(jaar) & ~nationaliteit.nationaliteit.isin(belgen) & nationaliteit.gemeente.isna() & nationaliteit.nationaliteit.notna() & nationaliteit.arrondissement.isna() & nationaliteit.provincie.notna()].reset_index(drop=True).sort_values('aantal', ascending=False).head(10)


#%%
belgen = ['Belgen']
jaar = [2019]
nationaliteit[nationaliteit.jaar.isin(jaar) & ~nationaliteit.nationaliteit.isin(belgen) & nationaliteit.gemeente.isna() & nationaliteit.nationaliteit.notna() & nationaliteit.arrondissement.isna() & nationaliteit.provincie.isna() & nationaliteit.gewest.notna()].reset_index(drop=True).sort_values('aantal', ascending=False).head(10)


#%%
jaar = [2009]
nationaliteit09 = nationaliteit[nationaliteit.jaar.isin(jaar) & nationaliteit.gemeente.notna() & nationaliteit.nationaliteit.notna()].reset_index(drop=True)


#%%
mode_nationaliteit09 = nationaliteit09.loc[nationaliteit09.groupby('gemeente').aantal.idxmax()].reset_index(drop=True)

#%%
mode_nationaliteit09[mode_nationaliteit09.nationaliteit != 'Belgen']

#%%
nationaliteit09[nationaliteit09.nationaliteit != 'Belgen'].sort_values('aantal', ascending=False).reset_index(drop=True).head(10).set_index('gemeente').drop(['belgië', 'gewest', 'provincie', 'belgen_en_nietbelgen', 'nationaliteit', 'jaar'], axis=1).plot.barh(title='Gemeentes met meeste niet-Belgen in 2009')

#%%
jaren = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
belgen = ['Belgen']
nat_ot = nationaliteit[nationaliteit.gewest.isna() & nationaliteit.nationaliteit.notna() & ~nationaliteit.nationaliteit.isin(belgen) & nationaliteit.provincie.isna() & nationaliteit.arrondissement.isna() & nationaliteit.gemeente.isna() & nationaliteit.jaar.isin(jaren)].reset_index(drop=True)
nat_ot[['jaar', 'aantal']].set_index('jaar').plot(title='Aantal niet-Belgen 2009 tot 2019', ylim=(0, 1500000)).xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

#%%
geslacht.columns = geslacht.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')

#%%
geslacht.info()

#%%
geslacht = geslacht.melt(id_vars=['belgië', 'gewest', 'provincie', 'arrondissement', 'gemeente', 'mannen_en_vrouwen', 'geslacht'],
value_vars=['bevolking_op_01_januari_2000', 'bevolking_op_01_januari_2001', 'bevolking_op_01_januari_2002', 'bevolking_op_01_januari_2003', 'bevolking_op_01_januari_2004', 'bevolking_op_01_januari_2005', 'bevolking_op_01_januari_2006', 'bevolking_op_01_januari_2007', 'bevolking_op_01_januari_2008', 'bevolking_op_01_januari_2009', 'bevolking_op_01_januari_2010', 'bevolking_op_01_januari_2011', 'bevolking_op_01_januari_2012', 'bevolking_op_01_januari_2013', 'bevolking_op_01_januari_2014', 'bevolking_op_01_januari_2015', 'bevolking_op_01_januari_2016', 'bevolking_op_01_januari_2017', 'bevolking_op_01_januari_2018', 'bevolking_op_01_januari_2019'],
var_name='jaar', value_name='aantal')

#%%
geslacht.aantal = geslacht.aantal.fillna(0.0)
geslacht.aantal = geslacht.aantal.astype(int)
geslacht.jaar = geslacht.jaar.str.replace('bevolking_op_01_januari_', '')
geslacht.jaar = geslacht.jaar.astype(int)

#%%
geslacht.to_csv('nieuwe_buren/bevolking_geslacht20002019.csv', index=False)

#%%
jaar = [2019]
geslacht19 = geslacht[geslacht.gemeente.notna() & geslacht.geslacht.notna() & geslacht.jaar.isin(jaar)].reset_index(drop=True)

#%%
vrouwen = ['Vrouwen']
geslacht19[geslacht19.geslacht.isin(vrouwen)].sort_values('aantal', ascending=False).reset_index(drop=True).head(10).set_index('gemeente').drop(['belgië', 'gewest', 'provincie', 'arrondissement', 'mannen_en_vrouwen', 'geslacht', 'jaar'], axis=1).plot.barh(title='Gemeentes met de meeste vrouwen in 2019')

#%%
mannen = ['Mannen']
geslacht19[geslacht19.geslacht.isin(mannen)].sort_values('aantal', ascending=False).reset_index(drop=True).head(10).set_index('gemeente').drop(['belgië', 'gewest', 'provincie', 'arrondissement', 'mannen_en_vrouwen', 'geslacht', 'jaar'], axis=1).plot.barh(title='Gemeentes met de meeste mannen in 2019')

#%%
mode_geslacht19 = geslacht19.loc[geslacht19.groupby('gemeente').aantal.idxmax()].reset_index(drop=True)

#%%
mode_geslacht19.geslacht.value_counts()

#%%
jaar = [2009]
geslacht09 = geslacht[geslacht.gemeente.notna() & geslacht.geslacht.notna() & geslacht.jaar.isin(jaar)].reset_index(drop=True)

#%%
vrouwen = ['Vrouwen']
geslacht09[geslacht09.geslacht.isin(vrouwen)].sort_values('aantal', ascending=False).reset_index(drop=True).head(10).set_index('gemeente').drop(['belgië', 'gewest', 'provincie', 'arrondissement', 'mannen_en_vrouwen', 'geslacht', 'jaar'], axis=1).plot.barh(title='Gemeentes met de meeste vrouwen in 2009')

#%%
mannen = ['Mannen']
geslacht09[geslacht09.geslacht.isin(mannen)].sort_values('aantal', ascending=False).reset_index(drop=True).head(10).set_index('gemeente').drop(['belgië', 'gewest', 'provincie', 'arrondissement', 'mannen_en_vrouwen', 'geslacht', 'jaar'], axis=1).plot.barh(title='Gemeentes met de meeste mannen in 2009')

#%%
mode_geslacht09 = geslacht09.loc[geslacht09.groupby('gemeente').aantal.idxmax()].reset_index(drop=True)

#%%
mode_geslacht09.geslacht.value_counts()

#%%
jaren = [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
geslacht_ot = geslacht[geslacht.gewest.isna() & geslacht.provincie.isna() & geslacht.arrondissement.isna() & geslacht.gemeente.isna() & geslacht.geslacht.notna() & geslacht.jaar.isin(jaren)].reset_index(drop=True)

#%%
pivot = geslacht_ot[['geslacht', 'jaar', 'aantal']].pivot(index='jaar', columns='geslacht', values='aantal')

#%%
pivot.plot(title='Ontwikkeling mannen en vrouwen 2009-2019', ylim=(0,6000000)).xaxis.set_major_locator(ticker.MaxNLocator(integer=True))

#%%
verhouding19 = geslacht19.groupby(['gemeente', 'geslacht']).agg({'aantal' : 'sum'})

#%%
verh_schema19 = verhouding19.groupby(level=0).apply(lambda x: 100 * x / int(x.sum()))

#%%
verh_schema19.aantal = verh_schema19.aantal.round(0)

#%%
verh_schema19[(verh_schema19.aantal < 45.0) | (verh_schema19.aantal > 55.0)]

#%%
unstacked = verhouding19.unstack()

#%%
unstacked.head(20).plot.barh(stacked=True, colormap='summer', title='Verhouding m/v in 2019')

#%%
verhouding09 = geslacht09.groupby(['gemeente', 'geslacht']).agg({'aantal' : 'sum'})

#%%
verh_schema09 = verhouding09.groupby(level=0).apply(lambda x: 100 * x / int(x.sum()))

#%%
verh_schema09.aantal = verh_schema09.aantal.round(0)

#%%
verh_schema09[(verh_schema09.aantal < 47.0) | (verh_schema09.aantal > 52.0)]

#%%
leeftijden = ['Van 15 tot 19 jaar', 'Van 20 tot 24 jaar', 'Van 25 tot 29 jaar']
jaar = [2019]
jonge_mensen = leeftijdsklasse[leeftijdsklasse.leeftijdsklasse.isin(leeftijden) & leeftijdsklasse.jaar.isin(jaar) & leeftijdsklasse.gemeente.notna()]
jonge_mensen = jonge_mensen.groupby(['gemeente', 'leeftijdsklasse']).agg({'aantal' : 'sum'})

#%%
jonge_mensen.head()

#%%
tot_jong = jonge_mensen.groupby('gemeente').aantal.sum().reset_index()

#%%
tot_jong.sort_values('aantal', ascending=False).head(10).set_index('gemeente').plot.barh(title='Gemeentes met de meeste jonge mensen 2019')

#%%
leeftijden = ['Van 15 tot 19 jaar', 'Van 20 tot 24 jaar', 'Van 25 tot 29 jaar']
jaar = [2009]
jong09 = leeftijdsklasse[leeftijdsklasse.leeftijdsklasse.isin(leeftijden) & leeftijdsklasse.jaar.isin(jaar) & leeftijdsklasse.gemeente.notna()]
jong09 = jong09.groupby(['gemeente', 'leeftijdsklasse']).agg({'aantal' : 'sum'})

#%%
tot_jong09 = jong09.groupby('gemeente').aantal.sum().reset_index()

#%%
jaar19 = [2019]
leeftijden = ['Van 15 tot 19 jaar', 'Van 20 tot 24 jaar', 'Van 25 tot 29 jaar']
jong_verh19 = leeftijdsklasse[(leeftijdsklasse.gemeente.notna()) & (leeftijdsklasse.jaar.isin(jaar19)) & ((leeftijdsklasse.leeftijdsklasse.isin(leeftijden)) | (leeftijdsklasse.leeftijdsklasse.isna()))].reset_index(drop=True)
jong_verh19.leeftijdsklasse = jong_verh19.leeftijdsklasse.fillna('Alles')
jong_verh_19 = jong_verh19.groupby(['gemeente', 'leeftijdsklasse']).agg({'aantal' : 'sum'})
jong_verhouding19 = jong_verh_19.groupby(level=0).apply(lambda x: 100 * x / float(x.max())).aantal.round(0).reset_index()
jong_verhouding19.aantal.value_counts()

#%%
jaar09 = [2009]
leeftijden = ['Van 15 tot 19 jaar', 'Van 20 tot 24 jaar', 'Van 25 tot 29 jaar']
jong_verh09 = leeftijdsklasse[(leeftijdsklasse.gemeente.notna()) & (leeftijdsklasse.jaar.isin(jaar09)) & ((leeftijdsklasse.leeftijdsklasse.isin(leeftijden)) | (leeftijdsklasse.leeftijdsklasse.isna()))].reset_index(drop=True)
jong_verh09.leeftijdsklasse = jong_verh09.leeftijdsklasse.fillna('Alles')
jong_verh_09 = jong_verh09.groupby(['gemeente', 'leeftijdsklasse']).agg({'aantal' : 'sum'})
jong_verhouding09 = jong_verh_09.groupby(level=0).apply(lambda x: 100 * x / float(x.max())).aantal.round(0).reset_index()
jong_verhouding09.aantal.value_counts()

#%%
jong_verhouding19.head()

#%%
jong_verhouding19.aantal.value_counts().reset_index().drop(1, axis=0).set_index('index').plot(title='Verdeling percentage jonge mensen 2019')

#%%
jong_verhouding19[jong_verhouding19.aantal == 14.0]

#%%
jong_verhouding19[jong_verhouding19.aantal == 13.0]

#%%
jong_verhouding19[jong_verhouding19.aantal == 12.0]

#%%
jong_verhouding19[jong_verhouding19.aantal == 11.0]

#%%
jong_verhouding19[jong_verhouding19.aantal == 2.0]

#%%
verhoudingjong09 = jong_verhouding09[jong_verhouding09.leeftijdsklasse != 'Alles']

#%%
verhoudingjong19 = jong_verhouding19[jong_verhouding19.leeftijdsklasse != 'Alles']

#%%
verhoudingjong19.to_csv('nieuwe_buren/verhoudingjong19.csv', index=False)
verhoudingjong09.to_csv('nieuwe_buren/verhoudingjong09.csv', index=False)

#%%
tot_jong09.sort_values('aantal', ascending=False).head(10).set_index('gemeente').plot.barh(title='Gemeentes met de meeste jonge mensen 2009')

#%%
jaar = [2019]
leeftijd19 = leeftijdsklasse[leeftijdsklasse.gemeente.notna() & leeftijdsklasse.jaar.isin(jaar) & leeftijdsklasse.leeftijdsklasse.notna()]
mode_lft19 = leeftijd19.loc[leeftijd19.groupby('gemeente').aantal.idxmax()].reset_index(drop=True)

#%%
mode_lft19.head(10)

#%%
mode_lft19.leeftijdsklasse.value_counts()

#%%
mode_lft19[mode_lft19.leeftijdsklasse == 'Van 20 tot 24 jaar']

#%%
mode_lft19[mode_lft19.leeftijdsklasse == 'Van 15 tot 19 jaar']

#%%
mode_lft19[mode_lft19.leeftijdsklasse == 'Van 70 tot 74 jaar']

#%%
mode_lft19[mode_lft19.leeftijdsklasse == 'Minder dan 5 jaar']

#%%
leeftijd19[leeftijd19.leeftijdsklasse == 'Minder dan 5 jaar'].sort_values('aantal', ascending=False).head(10).drop(['belgië', 'gewest', 'provincie', 'arrondissement', 'alle_leeftijden', 'leeftijdsklasse', 'jaar'], axis=1).set_index('gemeente').plot.barh(title='Gemeente met meeste kinderen < 5 in 2019')

#%%
jaar = [2019]
belgie19 = leeftijdsklasse[leeftijdsklasse.gewest.isna() & leeftijdsklasse.provincie.isna() & leeftijdsklasse.arrondissement.isna() & leeftijdsklasse.gemeente.isna() & leeftijdsklasse.leeftijdsklasse.notna() & leeftijdsklasse.jaar.isin(jaar)]
belgie19 = belgie19.groupby(['leeftijdsklasse']).agg({'aantal' : 'sum'})
belgie19.plot.bar(title='Verdeling per leeftijdsklasse België 2019')

#%%
jaar09 = [2009]
belgie09 = leeftijdsklasse[leeftijdsklasse.gewest.isna() & leeftijdsklasse.provincie.isna() & leeftijdsklasse.arrondissement.isna() & leeftijdsklasse.gemeente.isna() & leeftijdsklasse.leeftijdsklasse.notna() & leeftijdsklasse.jaar.isin(jaar09)]
belgie09 = belgie09.groupby(['leeftijdsklasse']).agg({'aantal' : 'sum'})
belgie09.plot.bar(title='Verdeling per leeftijdsklasse België 2009')

#%%
jaar = [2019]
belg_verh = leeftijdsklasse[(leeftijdsklasse.gemeente.notna()) & (leeftijdsklasse.jaar.isin(jaar)) & ((leeftijdsklasse.leeftijdsklasse == 'Minder dan 5 jaar') | (leeftijdsklasse.leeftijdsklasse.isna()))].reset_index(drop=True)

#%%
belg_verh.head()

#%%
belg_verh.leeftijdsklasse = belg_verh.leeftijdsklasse.fillna('Alles')

#%%
belg_verh_2 = belg_verh.groupby(['gemeente', 'leeftijdsklasse']).agg({'aantal' : 'sum'})

#%%
vijf_verhouding = belg_verh_2.groupby(level=0).apply(lambda x: 100 * x / float(x.max())).aantal.round(0).reset_index()

#%%
vijf_verhouding.aantal.value_counts().reset_index().drop(0, axis=0).set_index('index').plot(title='Verdeling percentage vijfjarigen')

#%%
vijf_verhouding[vijf_verhouding.aantal == 2.0]

#%%
vijf_verhouding[vijf_verhouding.aantal == 9.0]

#%%
vijf_verhouding[vijf_verhouding.aantal == 8.0]

#%%
vijf_verhouding[vijf_verhouding.aantal == 3.0]

#%%
jaar09 = [2009]
belg_verh09 = leeftijdsklasse[(leeftijdsklasse.gemeente.notna()) & (leeftijdsklasse.jaar.isin(jaar09)) & ((leeftijdsklasse.leeftijdsklasse == 'Minder dan 5 jaar') | (leeftijdsklasse.leeftijdsklasse.isna()))].reset_index(drop=True)
belg_verh09.leeftijdsklasse = belg_verh09.leeftijdsklasse.fillna('Alles')
belg_verh_209 = belg_verh09.groupby(['gemeente', 'leeftijdsklasse']).agg({'aantal' : 'sum'})
vijf_verhouding09 = belg_verh_2.groupby(level=0).apply(lambda x: 100 * x / float(x.max())).aantal.round(0).reset_index()
vijf_verhouding09.aantal.value_counts()

#%%
vijf_verhouding09.aantal.value_counts().reset_index().drop(0, axis=0).set_index('index').plot(title='Verdeling percentage vijfjarigen')

#%%
vijf_verhouding09[vijf_verhouding09.aantal == 9.0]

#%%
jaar19 = [2019]
verh_ouderen19 = leeftijdsklasse[(leeftijdsklasse.gemeente.notna()) & (leeftijdsklasse.jaar.isin(jaar19)) & ((leeftijdsklasse.leeftijdsklasse == 'Van 70 tot 74 jaar') | (leeftijdsklasse.leeftijdsklasse.isna()))].reset_index(drop=True)
verh_ouderen19.leeftijdsklasse = verh_ouderen19.leeftijdsklasse.fillna('Alles')
verh_ouderen_19 = verh_ouderen19.groupby(['gemeente', 'leeftijdsklasse']).agg({'aantal' : 'sum'})
oud_verhouding19 = verh_ouderen_19.groupby(level=0).apply(lambda x: 100 * x / float(x.max())).aantal.round(0).reset_index()
oud_verhouding19.aantal.value_counts()

#%%
jaar09 = [2009]
verh_ouderen09 = leeftijdsklasse[(leeftijdsklasse.gemeente.notna()) & (leeftijdsklasse.jaar.isin(jaar09)) & ((leeftijdsklasse.leeftijdsklasse == 'Van 70 tot 74 jaar') | (leeftijdsklasse.leeftijdsklasse.isna()))].reset_index(drop=True)
verh_ouderen09.leeftijdsklasse = verh_ouderen09.leeftijdsklasse.fillna('Alles')
verh_ouderen_09 = verh_ouderen09.groupby(['gemeente', 'leeftijdsklasse']).agg({'aantal' : 'sum'})
oud_verhouding09 = verh_ouderen_09.groupby(level=0).apply(lambda x: 100 * x / float(x.max())).aantal.round(0).reset_index()
oud_verhouding09.aantal.value_counts()

#%%
oud_verhouding19.aantal.value_counts().reset_index().drop(0, axis=0).set_index('index').plot(title='Verdeling percentage 70-74 in 2019')

#%%
oud_verhouding09.aantal.value_counts().reset_index().drop(0, axis=0).set_index('index').plot.hist(title='Verdeling percentage 70-74 in 2009')

#%%
oud_verhouding19[oud_verhouding19.aantal == 11.0]

#%%
oud_verhouding19[oud_verhouding19.aantal == 10.0]

#%%
oud_verhouding09[oud_verhouding09.aantal == 7.0]

#%%

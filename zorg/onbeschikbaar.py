#%%
import pandas as pd
from datetime import datetime as dt
import os

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
changes = pd.read_csv('~/Desktop/vrtnws_data/zorg/changes.csv', parse_dates=['BEGINDATUM ONBESCHIKBAARHEID'])
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
both['name_y'] = both['name_y'].str.replace('"', '')
both['packaging_type_y'] = both['packaging_type_y'].str.replace('"', '')

#%%
check = both[(both.pack_size_x != both.pack_size_y) | (both.name_medicinal_product != both.name_y) | (both.pharmaceutical_form_x != both.pharmaceutical_form_y) | (both.packaging_type_x != both.packaging_type_y)]

#%%
check.to_csv('zorg/check.csv', index=False)

#%%
no_end.to_csv('zorg/geen_einddatum.csv')
both.to_csv('zorg/still_noend.csv')

#%%
changes.info()

#%%
available = changes[changes.reden_delta == 'Terug beschikbaar']

#%%
merged_2 = pd.merge(no_end, available, left_on=['cti_extended', 'supply_problem_start_date'], right_on=['cti_extended', 'begindatum_onbeschikbaarheid'], how='left', indicator='exists')

#%%
merged_2.exists.value_counts()

#%%
both_2 = merged_2[merged_2.exists == 'both']

#%%
both_2.info()

#%%
both_2[both_2.supply_problem_start_date != both_2.begindatum_onbeschikbaarheid]

#%%
both_2['benaming'] = both_2['benaming'].str.replace('"', '')

#%%
check_2 = both_2[(both_2.name_medicinal_product != both_2.benaming) | (both_2.pack_size != both_2.verpakkingsgrootte) | (both_2.packaging_type != both_2.verpakkingstype) | (both_2.mah != both_2.vergunninghouder)]

#%%
check_2.info()

#%%
check_2.to_csv('zorg/check_2.csv', index=False)

#%%
len(both_2.index)

#%%
changes2210 = pd.read_csv('zorg/changes2210.csv', parse_dates=['BEGINDATUM ONBESCHIKBAARHEID'])
changes2210.columns = changes.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '').str.replace('-', '')

#%%
available2 = changes2210[changes2210.reden_delta == 'Terug beschikbaar']

#%%
merged_2210 = pd.merge(no_end, available2, left_on=['cti_extended', 'supply_problem_start_date'], right_on=['cti_extended', 'begindatum_onbeschikbaarheid'], how='left', indicator='exists')

#%%
both_2210 = merged_2210[merged_2210.exists == 'both']

#%%
both_2210['benaming'] = both_2210['benaming'].str.replace('"', '')

#%%
pd.concat([both_2, both_2210]).loc[
    both_2.index.symmetric_difference(both_2210.index)]

#%%
len(changes[changes.reden_delta != 'Terug beschikbaar'].index)

#%%
others = changes[changes.reden_delta != 'Terug beschikbaar']

#%%
merged_others = pd.merge(no_end, others, left_on=['cti_extended', 'supply_problem_start_date'], right_on=['cti_extended', 'begindatum_onbeschikbaarheid'], how='left', indicator='exists')

#%%
len(merged_others[merged_others.exists == 'both'].index)

#%%
check_3 = merged_others[merged_others.exists == 'both']

#%%
check_3.to_csv('zorg/check_3.csv', index=False)

#%%
check_3.reden_delta.value_counts()

#%%
check_3[check_3.vermoedelijke_einddatum_onbeschikbaarheid < '2019-10-23']

#%%
indices = merged[merged.exists == 'both'].index

#%%
merged.drop(indices, inplace=True)

#%%
merged.info()

#%%
leftovers = merged.drop(columns=['name_y', 'authorisation_holder', 'pharmaceutical_form_y', 'packaging_type_y', 'pack_size_y', 'cnk', 'fmd_code', 'supply_problem_expected_end_date', 'supply_problem_reason_y', 'parallel_distributor', 'derogation', 'exists'])

#%%
leftovers.info()

#%%
both_2.info()

#%%
leftover_both.info()

#%%
check_4 = pd.merge(both_2, leftover_both, how='outer', on=['cti_extended', 'supply_problem_start_date'], indicator='joint')

#%%
check_4.joint.value_counts()

#%%
check_4[check_4.joint == 'left_only']

#%%
leftovers_next = pd.merge(leftovers, available, how='outer', left_on=['cti_extended', 'supply_problem_start_date'], right_on=['cti_extended', 'begindatum_onbeschikbaarheid'], indicator='exists')

#%%
leftovers_next.exists.value_counts()

#%%
leftovers.cti_extended.nunique()

#%%
available.cti_extended.nunique()

#%%
len(available.index)

#%%
available.groupby(['cti_extended', 'begindatum_onbeschikbaarheid', 'verpakkingstype', 'verpakkingsgrootte']).count().sort_values(by=['benaming'], ascending=False).head(10)

#%%
available.to_csv('zorg/weer_beschikbaar.csv')

#%%
current.cti_extended.nunique()

#%%
available_clean = available.drop_duplicates(['cti_extended', 'begindatum_onbeschikbaarheid', 'verpakkingstype', 'verpakkingsgrootte'])

#%%
available_clean.cti_extended.nunique()

#%%
len(available_clean.index)

#%%
leftovers_next = pd.merge(leftovers, available_clean, how='outer', left_on=['cti_extended', 'supply_problem_start_date'], right_on=['cti_extended', 'begindatum_onbeschikbaarheid'], indicator='exists')

#%%
leftovers_next.exists.value_counts()

#%%
leftovers_next.info()

#%%
leftovers_dropped = leftovers_next[(leftovers_next.exists != 'both') & (leftovers_next.exists != 'right_only')]

#%%
len(leftovers_dropped.index)

#%%
leftovers_third = leftovers_dropped.drop(columns=['benaming', 'farmaceutische_vorm', 'verpakkingstype', 'verpakkingsgrootte', 'cnk', 'fmd_code', 'vergunninghouder', 'begindatum_onbeschikbaarheid', 'vermoedelijke_einddatum_onbeschikbaarheid', 'reden_onbeschikbaarheid', 'parallel_verdeler', 'reden_delta', 'exists'])

#%%
leftovers_third.info()

#%%
others.cti_extended.nunique()

#%%
len(others.index)

#%%
others_clean = others.drop_duplicates(['cti_extended', 'begindatum_onbeschikbaarheid', 'verpakkingstype', 'verpakkingsgrootte', 'cnk', 'fmd_code'])

#%%
len(others_clean.index)

#%%
leftovers_four = pd.merge(leftovers_third, others_clean, how='left', left_on=['cti_extended', 'supply_problem_start_date'], right_on=['cti_extended', 'begindatum_onbeschikbaarheid'], indicator='exists')

#%%
leftovers_four.exists.value_counts()

#%%
leftovers_third.groupby(['cti_extended', 'supply_problem_start_date']).count().sort_values(by='pack_size_x', ascending=False)

#%%
leftovers_third[leftovers_third.duplicated(['cti_extended', 'supply_problem_start_date'])]

#%%
others_clean[others_clean.duplicated(['cti_extended', 'begindatum_onbeschikbaarheid'])]

#%%
leftovers_four[leftovers_four.duplicated(['cti_extended', 'begindatum_onbeschikbaarheid'])]

#%%
leftovers_clean = leftovers_four.dropna(subset=['name_medicinal_product', 'pharmaceutical_form_x', 'begindatum_onbeschikbaarheid', 'verpakkingsgrootte'], axis='index', how='all')

#%%
len(leftovers_clean.index)

#%%
leftovers_clean.exists.value_counts()

#%%
changes[changes.duplicated(['cti_extended', 'begindatum_onbeschikbaarheid'])]

#%%
changes_clean = changes.drop_duplicates(['cti_extended', 'begindatum_onbeschikbaarheid', 'verpakkingstype', 'verpakkingsgrootte', 'cnk', 'fmd_code'])

#%%
changes_clean[changes_clean.duplicated(['cti_extended', 'begindatum_onbeschikbaarheid'])]

#%%
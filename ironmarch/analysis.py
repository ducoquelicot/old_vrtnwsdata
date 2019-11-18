import pandas as pd

results = pd.read_csv('./result.csv', sep=';')
members = pd.read_csv('./core_members.csv')

merged = pd.merge(members, results, on='ip_address', how='left')
merged.to_csv('./merged.csv', index=False)
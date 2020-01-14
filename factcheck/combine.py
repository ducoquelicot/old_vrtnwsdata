import os, glob
import pandas as pd 

files = glob.glob('*.csv')

df = pd.concat((pd.read_csv(f, header=0) for f in files))
df.to_csv('tweets.csv', index=False)
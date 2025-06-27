import pandas as pd

df = pd.read_csv('Reviews.csv', sep=',', header=None)
df = df[:100000]

df.to_csv('prep_100000.tsv', sep='\t', index=False, header=None)


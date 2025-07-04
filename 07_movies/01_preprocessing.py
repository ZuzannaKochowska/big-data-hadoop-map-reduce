import pandas as pd

df = pd.read_csv('movies_metadata.csv', sep=',')
df = df[:100000]
df.to_csv('movies_metadata.tsv', sep='\t', index=False)
import pandas as pd

df = pd.read_csv('text.csv')
print(df.info())

df.to_csv('text.csv', sep='\t', header=False, index=False)


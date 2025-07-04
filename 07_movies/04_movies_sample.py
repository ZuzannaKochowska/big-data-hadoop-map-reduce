import pandas as pd

df = pd.read_csv('movies_clean.csv')
df.head(50).to_csv('movies_data_sample.csv', index=False)

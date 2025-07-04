import pandas as pd

df = pd.read_csv("movies_metadata.csv", low_memory=False)

columns_to_keep = [
    'id', 'title', 'original_language', 'release_date', 'budget',
    'revenue', 'runtime', 'vote_average', 'vote_count'
]

df_clean = df[columns_to_keep].copy()

df_clean['release_date'] = pd.to_datetime(df_clean['release_date'], errors='coerce')
df_clean = df_clean.dropna(subset=['release_date'])

df_clean['budget'] = pd.to_numeric(df_clean['budget'], errors='coerce').fillna(0).astype('Int64')
df_clean['revenue'] = pd.to_numeric(df_clean['revenue'], errors='coerce').fillna(0).astype('Int64')
df_clean['vote_count'] = pd.to_numeric(df_clean['vote_count'], errors='coerce').fillna(0).astype('Int64')
df_clean['runtime'] = pd.to_numeric(df_clean['runtime'], errors='coerce').fillna(0).astype(float)
df_clean['vote_average'] = pd.to_numeric(df_clean['vote_average'], errors='coerce').fillna(0).astype(float)

df_clean.to_csv("movies_clean.csv", index=False)

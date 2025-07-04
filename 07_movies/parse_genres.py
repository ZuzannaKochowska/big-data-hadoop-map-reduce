import pandas as pd
import ast

df = pd.read_csv("movies_metadata.csv", low_memory=False)

df['genres'] = df['genres'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) and x != '' else [])

genres_data = []

for idx, row in df.iterrows():
    movie_id = row['id']
    try:
        for genre in row['genres']:
            genres_data.append({
                'movie_id': movie_id,
                'genre_id': genre.get('id'),
                'genre_name': genre.get('name')
            })
    except (ValueError, TypeError):
        continue

genres_df = pd.DataFrame(genres_data)

genres_df.to_csv("genres.csv", index=False)

print("Zapisano genres.csv")

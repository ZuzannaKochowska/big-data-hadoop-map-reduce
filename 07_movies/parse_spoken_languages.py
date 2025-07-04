import pandas as pd
import ast

df = pd.read_csv("movies_metadata.csv", low_memory=False)

df['spoken_languages'] = df['spoken_languages'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) and x != '' else [])

languages_data = []

for idx, row in df.iterrows():
    movie_id = row['id']
    try:
        for lang in row['spoken_languages']:
            languages_data.append({
                'movie_id': movie_id,
                'language_code': lang.get('iso_639_1'),
                'language_name': lang.get('name')
            })
    except (ValueError, TypeError):
        continue

languages_df = pd.DataFrame(languages_data)

languages_df.to_csv("spoken_languages.csv", index=False)

print("Zapisano spoken_languages.csv")

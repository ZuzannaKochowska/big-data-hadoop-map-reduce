import pandas as pd
import ast

df = pd.read_csv("movies_metadata.csv", low_memory=False)

df['production_countries'] = df['production_countries'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) and x != '' else [])

countries_data = []

for idx, row in df.iterrows():
    movie_id = row['id']
    try:
        for country in row['production_countries']:
            countries_data.append({
                'movie_id': movie_id,
                'iso_code': country.get('iso_3166_1'),
                'country_name': country.get('name')
            })
    except (ValueError, TypeError):
        continue

countries_df = pd.DataFrame(countries_data)

countries_df.to_csv("production_countries.csv", index=False)

print("Zapisano production_countries.csv")

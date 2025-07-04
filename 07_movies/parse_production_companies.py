import pandas as pd
import ast

df = pd.read_csv("movies_metadata.csv", low_memory=False)

df['production_companies'] = df['production_companies'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) and x != '' else [])

companies_data = []

for idx, row in df.iterrows():
    movie_id = row['id']
    try:
        for company in row['production_companies']:
            companies_data.append({
                'movie_id': movie_id,
                'company_id': company.get('id'),
                'company_name': company.get('name')
            })
    except (ValueError, TypeError):
        continue

companies_df = pd.DataFrame(companies_data)

companies_df.to_csv("production_companies.csv", index=False)

print("Zapisano production_companies.csv")

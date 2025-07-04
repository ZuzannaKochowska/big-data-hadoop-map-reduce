import pandas as pd
import ast

df = pd.read_csv("movies_metadata.csv", low_memory=False)

df['belongs_to_collection'] = df['belongs_to_collection'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) and x != '' else None)

collections_data = []

for idx, row in df.iterrows():
    movie_id = row['id']
    collection = row['belongs_to_collection']
    if isinstance(collection, dict):  
        collections_data.append({
            'movie_id': movie_id,
            'collection_id': collection.get('id'),
            'collection_name': collection.get('name')
        })


collections_df = pd.DataFrame(collections_data)

collections_df.to_csv("collections.csv", index=False)

print("Zapisano collections.csv")

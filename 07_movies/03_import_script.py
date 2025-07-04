import pandas as pd
from sqlalchemy import create_engine, text


engine = create_engine("mysql+mysqlconnector://root:password!@localhost:3306/movies_database")
with engine.connect() as conn:
    conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
    conn.execute(text("TRUNCATE TABLE movies;"))
    conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))

df = pd.read_csv(r"C:\Users\Zuza\Desktop\python\DANE\movies_clean.csv")

# === KROK 2: Ustawienia połączenia ===
user = "root"
password = "password!"
host = "localhost"
port = 3306
database = "movies_database"
# === KROK 3: Połącz się z bazą ===
engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")

# === KROK 4: Wyczyść tabelę (jeśli chcesz) ===
with engine.connect() as conn:
    conn.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
    conn.execute(text("TRUNCATE TABLE movies;"))
    conn.execute(text("SET FOREIGN_KEY_CHECKS=1;"))

# === KROK 5: Załaduj dane do MySQL ===
df.to_sql(name='movies_clean', con=engine, if_exists='append', index=False)

print("✅ Import zakończony pomyślnie.")

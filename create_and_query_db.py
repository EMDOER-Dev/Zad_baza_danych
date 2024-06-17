import sqlite3
import pandas as pd

# Tworzymy połączenie do bazy danych SQLite (jeśli nie istnieje, zostanie utworzona nowa baza danych)
conn = sqlite3.connect('air_quality.db')

# Ładujemy dane z plików CSV do pandas DataFrame
stations_df = pd.read_csv('clean_stations.csv')
measure_df = pd.read_csv('clean_measure.csv')

# Zapisujemy DataFrame'y do bazy danych jako tabele SQL
stations_df.to_sql('stations', conn, if_exists='replace', index=False)
measure_df.to_sql('measurements', conn, if_exists='replace', index=False)

# Sprawdzamy, czy dane zostały poprawnie wczytane
# Pobierzmy pierwsze 5 wierszy z tabeli stations jako przykład
query = "SELECT * FROM stations LIMIT 5"
results = conn.execute(query).fetchall()
print(results)

# Zamykamy połączenie do bazy danych
conn.close()
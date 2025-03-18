import pandas as pd
import numpy as np

file_path = '/Users/lukashein/Documents/VS_Code_Data/testPraktikum-1/customers-100.csv'
df = pd.read_csv(file_path)
print(df.head())  # Überprüfe die ersten paar Zeilen des DataFrames

# Umwandlung des DataFrames in ein NumPy-Array
data_array = df.to_numpy()

# Extrahieren der Spalten aus dem NumPy-Array
running_index = data_array[:, 0]
kundennummer = data_array[:, 1]
vorname = data_array[:, 2]

# Ausgabe der extrahierten Daten
print(running_index)
print(kundennummer)
print(vorname)
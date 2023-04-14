import csv
import os
import pandas as pd
import re
# Define el path utilizando la función join del módulo os
# G:\Mi unidad\Proyectos\En Curso\EGS\USTA\Migración
# path = os.path.join("G:\\","Mi unidad", "Proyectos", "En Curso", "EGS", "USTA", "Migración")
path = os.path.join("C:\\","Users","carlo","Google Drive", "Proyectos", "En Curso", "EGS", "USTA", "Migración")
# Imprime el path resultante
print(path)

# Especifica la ruta del archivo CSV que quieres leer
archivo_entrada = path + "\\Up_00_MIGRACION_PROCESSES.csv"

# Especifica la ruta del archivo CSV que quieres guardar
archivo_salida = path + "\\Out_Up_00_MIGRACION_PROCESSES.csv"

df = pd.read_csv(archivo_entrada)

print(df.describe())
columnas=['acts','pretensions','observations']
for columna in columnas:
    df[columna] = df[columna].apply(lambda x: re.sub(r'[^a-zA-Z0-9 .,;-]+', '', str(x)))

for columna in columnas:
    df[columna].fillna('NULL', inplace=True)
    df.loc[df[columna] == 'nan', columna] = 'NULL'

# df['type_area_id'].fillna('NULL', inplace=True)
# print(df.describe())

df.to_csv(archivo_salida, sep='|', quotechar = '"', index=False)

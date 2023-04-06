import csv
import os
import pandas as pd

# Define el path utilizando la función join del módulo os
# G:\Mi unidad\Proyectos\En Curso\EGS\USTA\Migración
path = os.path.join("G:\\","Mi unidad", "Proyectos", "En Curso", "EGS", "USTA", "Migración")

# Imprime el path resultante
print(path)

# Especifica la ruta del archivo CSV que quieres leer
archivo_entrada = path + "\Datos_00_MIGRACION_PROCESSES.csv"

# Especifica la ruta del archivo CSV que quieres guardar
archivo_salida = path + "\Out_Datos_00_MIGRACION_PROCESSES.csv"

df = pd.read_csv(archivo_entrada)

print(df.describe())

df.to_csv(archivo_salida, sep='|', quotechar = '"', index=False)

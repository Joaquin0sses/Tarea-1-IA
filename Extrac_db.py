import pandas as pd

# Ruta del archivo CSV de entrada
archivo_csv = 'ruta/a/tu/archivo.csv'

# Leer el archivo CSV completo
df = pd.read_csv(archivo_csv)

# Si hay más de 10000 filas, limitar a 10000
df_reducido = df.head(10000)

# Guardar el archivo CSV reducido
archivo_salida = 'archivo_reducido.csv'
df_reducido.to_csv(archivo_salida, index=False)

print(f'Archivo reducido a 10000 filas guardado como {archivo_salida}')
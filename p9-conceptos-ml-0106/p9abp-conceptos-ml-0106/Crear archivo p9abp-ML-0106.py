
# Samuel Nicola NC 0106
# NL 44

import pandas as pd

# 1. Crear un dataset de ejemplo
datos = {
    'id_paciente': [101, 102, 103, 104, 105],
    'edad': [45, 32, 56, 28, 63],
    'nivel_glucosa': [145, 95, 180, 110, 200],
    'presion_arterial': [85, 75, 95, 80, 100],
    'indice_masa_corporal': [30.5, 24.0, 33.2, 26.1, 35.8],
    'diagnostico_diabetes': [1, 0, 1, 0, 1]
}

df = pd.DataFrame(datos)

# 2. Eliminar la columna que no aporta al aprendizaje
df = df.drop(columns=['id_paciente'])

# 3. Separar variables de entrada (X) y variable objetivo (y)
X = df[['edad', 'nivel_glucosa', 'presion_arterial',
        'indice_masa_corporal']]

y = df['diagnostico_diabetes']

# 4. Mostrar estructura
print("--- DATOS DE ENTRADA (FEATURES - X) ---")
print(X.head(2))

print("\n--- VARIABLE OBJETIVO (TARGET - y) ---")
print(y.head(2))

# 5. Mostrar todas las columnas utilizadas
print("\n--- COLUMNAS DEL DATASET ---")
print(df.columns)

print("\nPrograma ejecutado correctamente")

print("Samuwl Nicola NC 0106")
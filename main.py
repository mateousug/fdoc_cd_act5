import pandas as pd

print("="*70)
print("DATASET BASE")
print("="*70)

datos = {
    'Nombre':  ['Ana', 'Bob', 'Clara', 'Diego', 'Eva'],
    'Edad':    [25, 30, 22, None, 28],
    'Ciudad':  ['Madrid', 'Lima', 'Bogotá', 'Medellín', None],
    'Ingreso': [3000, 4500, 2800, 5000, None]
}

df = pd.DataFrame(datos)
df.to_csv('actividad_semana5.csv', index=False)
print(df)
print("\n")

print("="*70)
print("1) SERIES — CREAR Y OPERAR")
print("="*70)

print("\n--- Series desde lista ---")
lista_numeros = [10, 20, 30, 40, 50]
serie_lista = pd.Series(lista_numeros)
print(serie_lista)

print("\n--- Series desde diccionario ---")
dict_datos = {'a': 100, 'b': 200, 'c': 300, 'd': 400}
serie_dict = pd.Series(dict_datos)
print(serie_dict)

print("\n--- Acceso por índice ---")
print(f"Elemento en posición 2 (lista): {serie_lista[2]}")
print(f"Elemento con clave 'c' (dict): {serie_dict['c']}")

print("\n--- Modificar valor ---")
serie_lista[2] = 99
print("Serie modificada (índice 2 = 99):")
print(serie_lista)

print("\n--- Multiplicar por 2 ---")
serie_multiplicada = serie_lista * 2
print(serie_multiplicada)
print("\n")

print("="*70)
print("2) DATAFRAME — CREAR Y EXPLORAR")
print("="*70)

df_nuevo = pd.DataFrame(datos)
print("\n--- DataFrame creado ---")
print(df_nuevo)

print("\n--- Nombres de columnas ---")
print(df_nuevo.columns.tolist())

print("\n--- Tipos de datos ---")
print(df_nuevo.dtypes)
print("\n")

print("="*70)
print("3) INSPECCIONAR Y EXPLORAR")
print("="*70)

print("\n--- Primeras 3 filas (head) ---")
print(df.head(3))

print("\n--- Últimas 2 filas (tail) ---")
print(df.tail(2))

print("\n--- Información del DataFrame (info) ---")
print(df.info())

print("\n--- Dimensiones (shape) ---")
print(f"Forma: {df.shape} (filas, columnas)")

print("\n--- Estadísticas descriptivas (describe) ---")
print(df.describe())
print("\n")

print("="*70)
print("4) ACCEDER A COLUMNAS Y FILAS")
print("="*70)

print("\n--- Columna 'Nombre' ---")
print(df['Nombre'])

print("\n--- Fila índice 1 con loc ---")
print(df.loc[1])

print("\n--- Fila índice 1 con iloc ---")
print(df.iloc[1])

print("\n--- Valor en fila 1, columna 'Edad' ---")
print(f"loc: {df.loc[1, 'Edad']}")
print(f"iloc: {df.iloc[1, 1]}")
print("\n")

print("="*70)
print("5) OPERACIONES BÁSICAS")
print("="*70)

print("\n--- Incrementar Edad en 5 años ---")
df_operaciones = df.copy()
df_operaciones['Edad'] = df_operaciones['Edad'] + 5
print(df_operaciones[['Nombre', 'Edad']])

print("\n--- Crear columna Ingreso_anual (Ingreso * 12) ---")
df_operaciones['Ingreso_anual'] = df_operaciones['Ingreso'].fillna(0) * 12
print(df_operaciones[['Nombre', 'Ingreso', 'Ingreso_anual']])
print("\n")

print("="*70)
print("6) FILTRAR DATOS")
print("="*70)

print("\n--- Personas con Edad > 30 ---")
filtro_edad = df[df['Edad'] > 30]
print(filtro_edad)

print("\n--- Personas de Madrid o Lima ---")
filtro_ciudad = df[df['Ciudad'].isin(['Madrid', 'Lima'])]
print(filtro_ciudad)
print("\n")

print("="*70)
print("7) MANEJO DE VALORES FALTANTES")
print("="*70)

print("\n--- Detectar valores nulos (isna) ---")
print(df.isna())

print("\n--- Cantidad de nulos por columna ---")
print(df.isna().sum())

print("\n--- Rellenar valores faltantes ---")
df_limpio = df.copy()
df_limpio['Edad'] = df_limpio['Edad'].fillna(0)
df_limpio['Ciudad'] = df_limpio['Ciudad'].fillna('Desconocido')
mediana_ingreso = df_limpio['Ingreso'].median()
df_limpio['Ingreso'] = df_limpio['Ingreso'].fillna(mediana_ingreso)
print(df_limpio)
print(f"\nMediana de Ingreso usada: {mediana_ingreso}")
print("\n")

print("="*70)
print("8) LEER Y GUARDAR DATOS")
print("="*70)

print("\n--- Leer CSV 'actividad_semana5.csv' ---")
df_leido = pd.read_csv('actividad_semana5.csv')
print(df_leido.head())

print("\n--- Guardar CSV con columnas seleccionadas ---")
df_seleccion = df[['Nombre', 'Edad', 'Ciudad']]
df_seleccion.to_csv('personas_seleccion.csv', index=False)
print("Archivo 'personas_seleccion.csv' guardado con columnas: Nombre, Edad, Ciudad")
print("\n")

print("="*70)
print("9) EJERCICIO INTEGRADO")
print("="*70)

print("\n--- Procesamiento integrado ---")
df_integrado = df.copy()

df_integrado['Edad'] = df_integrado['Edad'].fillna(0) + 5
print("✓ Edad incrementada en 5 años")

df_integrado['Ingreso_anual'] = df_integrado['Ingreso'].fillna(0) * 12
print("✓ Columna Ingreso_anual creada")

df_filtrado = df_integrado[df_integrado['Ingreso_anual'] > 36000]
print(f"✓ Filtradas {len(df_filtrado)} personas con Ingreso_anual > 36000")

df_filtrado = df_filtrado.sort_values('Ingreso_anual', ascending=False)
print("✓ Ordenado por Ingreso_anual (descendente)")

df_filtrado.to_csv('personas_filtradas.csv', index=False)
print("✓ Archivo 'personas_filtradas.csv' guardado")

print("\n--- Resultado final ---")
print(df_filtrado)

print("\n" + "="*70)
print("ACTIVIDAD COMPLETADA")
print("="*70)
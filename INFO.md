# Actividad 5: Pandas Básico - Información

## Descripción
Esta actividad cubre los conceptos fundamentales de Pandas, incluyendo Series, DataFrames, inspección de datos, acceso, operaciones básicas, filtrado, manejo de valores faltantes y lectura/escritura de archivos CSV.

## Dataset
El dataset base contiene información de 5 personas con las siguientes columnas:
- **Nombre**: Nombre de la persona (string)
- **Edad**: Edad en años (numérico, contiene valores nulos)
- **Ciudad**: Ciudad de residencia (string, contiene valores nulos)
- **Ingreso**: Ingreso mensual (numérico, contiene valores nulos)

## Ejercicios Cubiertos

### 1. Series - Crear y Operar
- Creación de Series desde lista y diccionario
- Acceso por índice y clave
- Modificación de valores
- Operaciones aritméticas sobre Series

### 2. DataFrame - Crear y Explorar
- Creación de DataFrame desde diccionario
- Visualización de nombres de columnas
- Verificación de tipos de datos

### 3. Inspeccionar y Explorar
- `head()`: Primeras filas
- `tail()`: Últimas filas
- `info()`: Información general
- `shape`: Dimensiones del DataFrame
- `describe()`: Estadísticas descriptivas

### 4. Acceder a Columnas y Filas
- Acceso a columnas como Series
- `loc[]`: Acceso por etiquetas
- `iloc[]`: Acceso por posición numérica
- Acceso a valores específicos

### 5. Operaciones Básicas
- Incremento de valores en columnas
- Creación de nuevas columnas calculadas
- Manejo de valores nulos en operaciones

### 6. Filtrar Datos
- Filtrado con condiciones numéricas
- Filtrado con múltiples valores usando `isin()`

### 7. Manejo de Valores Faltantes
- Detección con `isna()`
- Conteo de valores nulos por columna
- Rellenado con `fillna()` usando valores constantes y estadísticas (mediana)

### 8. Leer y Guardar Datos
- Lectura de archivos CSV con `read_csv()`
- Escritura de archivos CSV con `to_csv()`
- Selección de columnas específicas para exportar

### 9. Ejercicio Integrado
Pipeline completo que incluye:
- Transformación de datos
- Creación de columnas calculadas
- Filtrado basado en condiciones
- Ordenamiento
- Exportación de resultados

## Archivos Generados

### actividad_semana5.csv
Dataset original con todas las columnas y valores (incluidos nulos).

### personas_seleccion.csv
Subconjunto del dataset con columnas: Nombre, Edad, Ciudad.

### personas_filtradas.csv
Resultado del ejercicio integrado con personas que tienen:
- Edad incrementada en 5 años
- Ingreso_anual > 36000
- Ordenado por Ingreso_anual descendente

## Requisitos
- Python 3.x
- pandas

## Ejecución
```bash
python actividad5_pandas.py
```

## Conceptos Clave

### Series
Estructura de datos unidimensional con índice. Puede crearse desde listas, diccionarios o arrays.

### DataFrame
Estructura bidimensional (tabla) con filas y columnas etiquetadas. Cada columna es una Series.

### loc vs iloc
- **loc[]**: Acceso basado en etiquetas (nombres)
- **iloc[]**: Acceso basado en posiciones numéricas (0, 1, 2...)

### Valores Faltantes
- `None` o `NaN` representan valores faltantes
- `isna()` detecta valores nulos
- `fillna()` rellena con valores específicos

### Filtrado
Se usan expresiones booleanas para crear máscaras que seleccionan filas específicas.

## Resultado Esperado
El script ejecuta automáticamente todos los ejercicios y muestra:
- Outputs de cada operación
- DataFrames resultantes
- Archivos CSV generados
- Confirmación de operaciones completadas
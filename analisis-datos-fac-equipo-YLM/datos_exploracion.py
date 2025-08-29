# calidad_datos.py
import pandas as pd
import numpy as np


SEPARADOR = "=" * 100
# Leer los datos
df = pd.read_excel('C:/Users/linar/OneDrive/Escritorio/Python/analisis-datos-fac-equipo-1/analisis-datos-fac-equipo-YLM/Datos/JEFAB_2024.xlsx')
print(df)


print(SEPARADOR)


# Nombres de las variables
print("=== NOMBRES DE LAS VARIABLES ===")
print(df.columns)

print(SEPARADOR)

# Análisis de datos faltantes
print("=== ANÁLISIS DE DATOS FALTANTES ===")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
print("Top 10 columnas con más datos faltantes:")
missing_info = pd.DataFrame({
'Columna': missing_data.index,
'Datos_Faltantes': missing_data.values,
'Porcentaje': missing_percent.values
}).sort_values('Datos_Faltantes', ascending=False)
print(missing_info.head(11))

print(SEPARADOR)

# Análisis de duplicados
print(f"\n=== ANÁLISIS DE DUPLICADOS ===")
print(f"Registros duplicados: {df.duplicated().sum()}")

print(SEPARADOR)

# Análisis de tipos de datos
print(f"\n=== TIPOS DE DATOS ===")
print(df.dtypes.value_counts()) 

print(SEPARADOR)

# Identificar columnas problemáticas
print(f"\n=== COLUMNAS CON CARACTERES ESPECIALES ===")
problematic_columns = [col for col in df.columns if 'Ã' in col or 'â' in col]
print(f"Columnas con encoding problemático: {len(problematic_columns)}")
for col in problematic_columns[:5]:
    print(f" - {col}")

print(SEPARADOR)

print(f"\n=== CAMBIOS EN LA VARIABLE NUMERO DE HIJOS ===")
# 1) Asegurar NUMERO_HIJOS como numérico para detectar NaN
df['NUMERO_HIJOS'] = pd.to_numeric(df['NUMERO_HIJOS'], errors='coerce')


cols = df.columns.tolist()
idx = cols.index('NUMERO_HIJOS')
left_col = cols[idx - 1]  # columna de la izquierda

# 3) Normalizar texto ('NO', 'no', ' No ', incluso 'N0' con cero) y aplicar regla:
left_norm = (df[left_col].astype(str)
                         .str.strip()
                         .str.upper()
                         .str.replace('N0', 'NO', regex=False))

mask = left_norm.eq('NO') & df['NUMERO_HIJOS'].isna()
df.loc[mask, 'NUMERO_HIJOS'] = 0  # poner 0 donde a la izquierda dice NO y NUMERO_HIJOS estaba vacío

print(f"\n=== VERIFRICACION DE CAMBIOS ===")
print(f"Columna izquierda detectada: {left_col}")
print(f"Filas modificadas: {int(mask.sum())}")
print(df['NUMERO_HIJOS'].value_counts(dropna=False).sort_index().head(10))
print(df.loc[mask, [left_col, 'NUMERO_HIJOS']].head(10))

print(SEPARADOR)

print(f"\n=== IMPUTACION EN NUMERO DE HIJOS ===")
was_na = df['NUMERO_HIJOS'].isna()


fill_val = float(np.nanmedian(df['NUMERO_HIJOS'])) #Con mediana


s_imp = (
    df['NUMERO_HIJOS'].fillna(fill_val) #Relleno los NA
     .round()          # p. ej., 1.6 -> 2
     .clip(lower=0)    # jamás < 0 en un conteo
     .astype('Int64')  # entero con NA permitido (nullable)
)


df['NUMERO_HIJOS'] = s_imp
df['NUMERO_HIJOS_imputado'] = was_na  # True si se imputó, False si era original


print(f"Mediana usada: {fill_val}")
print(df['NUMERO_HIJOS'].value_counts(dropna=False).sort_index().head(12))

print("=== ANÁLISIS DE DATOS FALTANTES ===")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
print("Top 10 columnas con más datos faltantes:")
missing_info = pd.DataFrame({
'Columna': missing_data.index,
'Datos_Faltantes': missing_data.values,
'Porcentaje': missing_percent.values
}).sort_values('Datos_Faltantes', ascending=False)

print("\nFaltantes en NUMERO_HIJOS:")
print(missing_info[ missing_info['Columna'] == 'NUMERO_HIJOS' ])

print(SEPARADOR)

print(f"\n=== IMPUTACION EN EDAD ===")
df['EDAD2'] = pd.to_numeric(df['EDAD2'], errors='coerce')
was_nae = df['EDAD2'].isna()


fill_vale = float(np.nanmedian(df['EDAD2'])) #Con mediana


e_imp = (
    df['EDAD2'].fillna(fill_vale) #Relleno los NA
     .round()          # p. ej., 1.6 -> 2
     .clip(lower=0)    # jamás < 0 en un conteo
     .astype('Int64')  # entero con NA permitido (nullable)
)


df['EDAD2'] = e_imp
df['EDAD2_imputado'] = was_nae  # True si se imputó, False si era original


print(f"Mediana usada: {fill_vale}")
print(df['EDAD2'].value_counts(dropna=False).sort_index().head(12))

print("=== ANÁLISIS DE DATOS FALTANTES ===")
missing_data = df.isnull().sum()
missing_percent = (missing_data / len(df)) * 100
print("Top 10 columnas con más datos faltantes:")
missing_info = pd.DataFrame({
'Columna': missing_data.index,
'Datos_Faltantes': missing_data.values,
'Porcentaje': missing_percent.values
}).sort_values('Datos_Faltantes', ascending=False)

print("\nFaltantes en EDAD:")
print(missing_info[ missing_info['Columna'] == 'EDAD2' ])






    # calidad_datos.py
import pandas as pd, unicodedata, re
import numpy as np
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib.pyplot as plt

SEPARADOR = "=" * 100

# Leer los datos
df = pd.read_excel('C:\\Users\\linar\\OneDrive\\Escritorio\\Python\\analisis-datos-fac-equipo-1\\analisis-datos-fac-equipo-YLM\\Datos\\JEFAB_2024.xlsx')

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

# Identificar columnas problemáticas
print(f"\n=== COLUMNAS CON CARACTERES ESPECIALES ===")
problematic_columns = [col for col in df.columns if 'Ã' in col or 'â' in col]
print(f"Columnas con encoding problemático: {len(problematic_columns)}")
for col in problematic_columns[:5]:
    print(f" - {col}")

print(SEPARADOR)


#Cambiamos sintaxis de la variable nivel educativo
print("=== DEPURAR COLUMNA DE NIVEL EDUCATIVO ===")
col = 'NIVEL_EDUCATIVO'

def norm_txt(x):
    if pd.isna(x): return x
    t = unicodedata.normalize('NFKD', str(x)).encode('ascii','ignore').decode()
    return re.sub(r'\s+', ' ', t).upper().strip()

df[col] = df[col].map(norm_txt)

# 2) Unificar typos/variantes
df[col] = df[col].replace({
    r'.*(ESPECIALIZA|MAESTR|MAGISTER|DOCTOR|PHD).*'   : 'POSGRADO',
    r'.*(UNIVERSITAR|PROFESIONA|PREGRADO).*'          : 'PROFESIONAL',
    r'.*TECNOL.*'                                     : 'TECNOLOGICO',  
    r'.*T[EA]CNI.*'                                   : 'TECNICO',      
    r'^BASICA PRIMARIA$'                              : 'PRIMARIA',
    r'^(BASICA SECUNDARIA|BACHILLER|MEDIA)$'          : 'SECUNDARIA',
    r'^(N/?A|N A|NA)$'                                : 'NO APLICA',
    r'^(OTROS?|OTRA)$'                                : 'OTRO',
}, regex=True)


print(sorted(df[col].dropna().unique()))
print(df[col].value_counts(dropna=False))

print(SEPARADOR)

#Se pone un 0 si la respuesta a "HIJOS" es NO
print(f"\n=== CAMBIOS EN LA VARIABLE NUMERO DE HIJOS Y PONER 0 SI NO TIENEN ===")

df['NUMERO_HIJOS'] = pd.to_numeric(df['NUMERO_HIJOS'], errors='coerce')
cols = df.columns.tolist()
idx = cols.index('NUMERO_HIJOS')
left_col = cols[idx - 1]  #columna de la izquierda (HIJOS)

# Se normaliza el texto ('NO', 'no', ' No ')
left_norm = (df[left_col].astype(str)
                         .str.strip()
                         .str.upper()
                         .str.replace('N0', 'NO', regex=False))

mask = left_norm.eq('NO') & df['NUMERO_HIJOS'].isna()
df.loc[mask, 'NUMERO_HIJOS'] = 0  

print(f"\n=== VERIFRICACION DE CAMBIOS ===")
print(f"Columna izquierda detectada: {left_col}")
print(f"Filas modificadas: {int(mask.sum())}")
print(df['NUMERO_HIJOS'].value_counts(dropna=False).sort_index().head(10))
print(df.loc[mask, [left_col, 'NUMERO_HIJOS']].head(10))

print(SEPARADOR)

#Se Imputan los datos faltantes NUMERO_HIJOS, EDAD2 E HIJOS_EN_HOGAR
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

print(f"Mediana usada: {fill_val}")
print(df['NUMERO_HIJOS'].value_counts(dropna=False).sort_index().head(12))

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

print(f"Mediana usada: {fill_vale}")
print(df['EDAD2'].value_counts(dropna=False).sort_index().head(12))

print(SEPARADOR)

print(f"\n=== IMPUTACION EN HIJOS EN HOGAR ===")
df['HIJOS_EN_HOGAR'] = pd.to_numeric(df['HIJOS_EN_HOGAR'], errors='coerce')
was_nae = df['HIJOS_EN_HOGAR'].isna()


fill_vale = float(np.nanmedian(df['HIJOS_EN_HOGAR'])) #Con mediana


e_imp = (
    df['HIJOS_EN_HOGAR'].fillna(fill_vale) #Relleno los NA
     .round()          # p. ej., 1.6 -> 2
     .clip(lower=0)    # jamás < 0 en un conteo
     .astype('Int64')  # entero con NA permitido (nullable)
)

df['HIJOS_EN_HOGAR'] = e_imp

print(f"Mediana usada: {fill_vale}")
print(df['HIJOS_EN_HOGAR'].value_counts(dropna=False).sort_index().head(12))

print(SEPARADOR)

#Luego de tener el dataset depurado y limpio sin faltantes, extraemos variables a trabajar
print("=== EXTRAEMOS UNICAMENTE LAS VARIABLES A TRABAJAR ===")
deseadas = [
    "EDAD2","SEXO","NIVEL EDUCATIVO","ESTRATO","CATEGORIA","GRADO","ESTADO_CIVIL",
    "HIJOS","HABITA_VIVIENDA_FAMILIAR","RELACION_AMBOS_PADRES","RELACION_HERMANOS",
    "TIPO_RELACION_PAREJA","NUMERO_HIJOS","RELACION_HIJOS",
    "RESPONSABILIDAD_ACADEMICA_BIENESTAR_HIJOS","PERS_A_CARG_HIJOS",
    "HIJOS_EN_HOGAR","HERMANOS"
]

norm = lambda s: re.sub(r'[^a-z0-9]','', unicodedata.normalize('NFKD', str(s)).encode('ascii','ignore').decode().lower())
map_df = {norm(c): c for c in df.columns}
sel   = [map_df[norm(w)] for w in deseadas if norm(w) in map_df]
falt  = [w for w in deseadas if norm(w) not in map_df]

df = df[sel].copy()
print("Seleccionadas:", sel)
print("No encontradas:", falt)
print(df)

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
print(missing_info.head(19))

print(SEPARADOR)

#=================================================================================================================================================================
#ANÁLISIS DEMOGRAFICO
#=================================================================================================================================================================

# Explorar estructura básica
print("=== INFORMACIÓN GENERAL ===")
print(f"Total de registros: {len(df)}")
print(f"Total de columnas: {len(df.columns)}")

# Análisis de edad
print("\n=== ANÁLISIS DE EDAD ===")
print(f"Edad promedio: {df['EDAD2'].mean():.1f} años")
print(f"Edad mínima: {df['EDAD2'].min()} años")
print(f"Edad máxima: {df['EDAD2'].max()} años")

# Gráfico de edades
plt.figure(figsize=(10, 6))
plt.hist(df['EDAD2'], bins=20, edgecolor='black')
plt.title('Distribución de Edades del Personal FAC')
plt.xlabel('Edad')
plt.ylabel('Cantidad de Personal')
plt.show()

#=================================================================================================================================================================
# PREGUNTA 1: ¿Cuál es el rango de edad más común?
#=================================================================================================================================================================

# Creo los rangos de edad de 5 en 5 años.
# Uso la función pd.cut para clasificar cada persona dentro de un rango.
df['RANGO_EDAD'] = pd.cut(
    df['EDAD2'],
    bins=[17, 22, 27, 32, 37, 42, 47, 52, 57, 62, 67, 70],  # intervalos de 5 en 5
    labels=['18-22', '23-27', '28-32', '33-37', '38-42', '43-47', 
            '48-52', '53-57', '58-62', '63-67', '68-69'],   # nombres de los rangos
    right=True  # incluyo el valor del límite derecho en cada intervalo
)

# Cuento cuántas personas hay en cada rango de edad.
frecuencias_rango = df['RANGO_EDAD'].value_counts().sort_values(ascending=False)

print("=== FRECUENCIA DE RANGOS DE EDAD ===")
print(frecuencias_rango)

# Identifico el rango más frecuente y el número de personas que están en él.
rango_mas_comun = frecuencias_rango.idxmax()
cantidad_mas_comun = frecuencias_rango.max()

print(f"\nEl rango de edad más común es: '{rango_mas_comun}' con {cantidad_mas_comun} personas.")


# VISUALIZACIÓN
# Hago un gráfico de barras para visualizar mejor la distribución por rangos de edad.
plt.figure(figsize=(10, 6))
frecuencias_rango.sort_index().plot(kind='bar', color='steelblue', edgecolor='black')
plt.title('Distribución por Rango de Edad - Personal FAC')
plt.xlabel('Rango de Edad')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=0)
plt.show()


# Análisis de género
print("\n=== ANÁLISIS DE GÉNERO ===")
print(df['SEXO'].value_counts())

#=================================================================================================================================================================
# PREGUNTA 2: ¿Hay diferencias en la distribución por sexo?
#=================================================================================================================================================================

# Cuento cuántas personas hay en cada categoría de género
conteo_genero = df['SEXO'].value_counts()

print("=== DISTRIBUCIÓN POR SEXO ===")
print(conteo_genero)

# También calculo los porcentajes para ver mejor la proporción
porcentajes_genero = df['SEXO'].value_counts(normalize=True) * 100
print("\n=== PORCENTAJES POR SEXO ===")
print(porcentajes_genero.round(1))

# Identifico cuál es el sexo más frecuente
sexo_mas_comun = conteo_genero.idxmax()
cantidad_mas_comun = conteo_genero.max()

print(f"\nEl sexo más común es: '{sexo_mas_comun}' con {cantidad_mas_comun} personas.")

# ===============================
# VISUALIZACIÓN
# ===============================

# Hago un gráfico de barras para visualizar la diferencia entre sexos
colores = ['skyblue', 'lightpink']  # defino los colores para representar las variables(hombre y mujer)
ax = conteo_genero.plot(kind='bar', color=colores, edgecolor='black')# Creo el gráfico de barras

# Agrego título y etiquetas
plt.title('Distribución por Sexo - Personal FAC')
plt.xlabel('Sexo')
plt.ylabel('Cantidad de Personas')
plt.xticks(rotation=0)

# Agrego los valores correspondientes a la cantidad de personas por sexo encima de cada barra
for p in ax.patches:
    ax.annotate(str(p.get_height()), 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom')

plt.legend(conteo_genero.index, title="Sexo", loc="lower left")# Agrego leyenda al gráfico
plt.show()

# Hago un gráfico de torta (pie chart) mostrando los porcentajes
plt.figure(figsize=(6, 6))
conteo_genero.plot(
    kind='pie',
    autopct='%1.1f%%',   # Muestra el porcentaje con un decimal
    startangle=90,       # Gira el inicio para que quede más ordenado
    colors=['steelblue', '#FF7FAF'],  # Colores para cada sexo
    wedgeprops={'edgecolor': 'black'}    # Bordes en negro para mejor visualización
)
plt.title('Distribución por Sexo - Personal FAC')
plt.ylabel('')  # Quito la etiqueta del eje Y porque no se necesita en pie chart
# Agrego la leyenda
plt.legend(
    labels=conteo_genero.index,  # Los nombres de las categorías (Hombre, Mujer.)
    title="Sexo",                # Título de la leyenda
    loc="lower left"            
)

plt.show()



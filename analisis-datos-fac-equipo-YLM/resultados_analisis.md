
# Resultados del análisis — Proyecto FAC

Aquí documentamos los análisis de nuestro proyecto (A: Demografía · B: Datos familiares · C: Calidad de datos).

---

## Calidad de Datos

Aseguramos que el dataset sea **consistente, completo y estandarizado**.  
Partimos de **<6423>** registros y **<231>** variables; para el análisis usamos **18 columnas** (≈ **<8>%**), todas documentadas en el **diccionario**.

---

## Procedimiento

**Diagnóstico inicial**
- Cuantificación de faltantes por variable y verificación de duplicados.

- Revisión de *encoding* en nombres de columnas y tipos de datos.

**Estandarización**
- `NIVEL_EDUCATIVO`: normalización (mayúsculas, sin tildes) y **unificación** de variantes a un catálogo controlado  
  (Posgrado, Profesional, Tecnológico, Técnico, Secundaria, Primaria, No Aplica, Otro).


- **Regla de negocio**: coherencia `HIJOS` ↔ `NUMERO_HIJOS`  
  (si `HIJOS = NO` ⇒ `NUMERO_HIJOS = 0` cuando estuviera vacío).

**Faltantes (imputación por mediana)**
- `NUMERO_HIJOS`, `EDAD2`, `HIJOS_EN_HOGAR`: imputación con **mediana**, manteniendo valores **enteros ≥ 0**.

**Selección final (18 variables)**
- `EDAD2`, `SEXO`, `NIVEL EDUCATIVO`, `ESTRATO`, `CATEGORIA`, `GRADO`, `ESTADO_CIVIL`, `HIJOS`,  
  `HABITA_VIVIENDA_FAMILIAR`, `RELACION_AMBOS_PADRES`, `RELACION_HERMANOS`, `TIPO_RELACION_PAREJA`,  
  `NUMERO_HIJOS`, `RELACION_HIJOS`, `RESPONSABILIDAD_ACADEMICA_BIENESTAR_HIJOS`, `PERS_A_CARG_HIJOS`,  
  `HIJOS_EN_HOGAR`, `HERMANOS`.

---

## Resultados

- **Comparabilidad**: categorías unificadas permiten cruces limpios (p. ej., `NIVEL_EDUCATIVO × SEXO/ESTRATO`). 

- **Trazabilidad**: decisiones documentadas y reproducibles con Git/GitHub.

- Dataset con **18 variables** estandarizadas y reglas de negocio aplicadas. 

- **Reducción de faltantes** en variables clave (conteos/edad).  

- **Catálogos** alineados con el **diccionario** del proyecto.

---
📊 Informe de Análisis Demográfico – Proyecto FAC Bienestar Familiar

Como analista demográfica del equipo, se realizó un análisis de los datos provenientes de la encuesta de bienestar familiar aplicada al personal de la Fuerza Aérea Colombiana (FAC). El propósito fue caracterizar la población encuestada desde una perspectiva demográfica, explorando variables como edad, género, categoría militar, nivel educativo y estrato socioeconómico.

La base de datos fue depurada previamente por el experto en calidad de datos, quedando conformada por 6423 registros y 18 variables listas para su análisis.

# 👤 Análisis de Edad

Edad mínima: 18 años
Edad promedio: 36.7 años
Edad máxima: 69 años
El rango de edad más común fue 33–37 años (1267 personas), seguido de 28–32 años (1211 personas).
Esto indica que gran parte del personal de la FAC encuestado se encuentra en edades de madurez profesional, lo que influye en su desarrollo laboral y familiar.

# 🚹🚺 Distribución por Sexo

Hombres: 4470 (69.6%)
Mujeres: 1953 (30.4%)
Existe una clara predominancia masculina, coherente con el contexto militar.
Sin embargo, la participación femenina es significativa, representando casi un tercio de la muestra, lo que refleja avances en inclusión y diversidad dentro de la institución.
Sí existen diferencias en la distribución por género: los hombres son mayoría, pero las mujeres tienen una presencia importante.

# 🎖️ Categoría Militar

El análisis de la categoría militar muestra que:
Suboficiales: 2650 personas (grupo más frecuente)
Civiles: segundo lugar
Oficiales: menor proporción
Los suboficiales concentran la mayor parte de la muestra, por lo que las estrategias de bienestar deben priorizar a este grupo.

# 🎓 Análisis Nivel Educativo y Sexo

![Imagen de WhatsApp 2025-08-29 a las 14 10 04_37d2e8ce](https://github.com/user-attachments/assets/9150b10d-1dad-4b74-b48b-bbafa71fde80)

# 📈 Análisis Edad y Nivel Educativo

![Imagen de WhatsApp 2025-08-29 a las 14 42 12_f4b19365](https://github.com/user-attachments/assets/9fac220b-8c4d-4a12-b0d7-e82a6ef3795e)

# 🏘️ Análisis Estrato Socioeconómico y Nivel Educativo

![Imagen de WhatsApp 2025-08-29 a las 14 51 36_92c8299f](https://github.com/user-attachments/assets/dc44e5db-52f9-4f16-92df-245b30b7ede8)




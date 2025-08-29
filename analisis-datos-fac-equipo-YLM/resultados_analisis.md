
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


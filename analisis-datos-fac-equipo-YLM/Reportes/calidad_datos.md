# Control de Calidad de Datos — Funcionario C (Lina Rozo)

**Proyecto:** Encuesta de Bienestar Familiar FAC  
**Rol:** Experta/o en Calidad de Datos (Funcionario C)  
**Editor:** Visual Studio Code (VS Code) · **Gestión:** Git/GitHub  
**Fuente:** `JEFAB_2024.xlsx`

---

## 1) Alcance y tamaño del conjunto de datos
- **Registros totales (filas):** **<6423>**.  
- **Columnas totales (variables):** **<231>**.  
- **Objetivo del QC:** asegurar **consistencia, completitud, estandarización y trazabilidad** antes del análisis.

---

## 2) Perfilado inicial (diagnóstico)
- **Estructura:** revisión de nombres de columnas y tipos de datos para identificar desalineaciones (texto vs. numérico).  
- **Faltantes:** cuantificación de valores nulos por variable, con priorización de las que concentran mayor proporción de NA.  
- **Duplicados:** verificación del número de registros duplicados para evidenciar posibles errores de captura o consolidación.  
- **Encoding:** identificación de nombres de columnas con caracteres extraños (p. ej., `Ã`, `â`), indicando posibles problemas de codificación a corregir.

---

## 3) Estandarización y recodificación de categorías
### 3.1 `NIVEL_EDUCATIVO`
- **Normalización del contenido:** se transformaron las respuestas a **mayúsculas**, **sin tildes** y con espacios uniformes.  
- **Unificación de variantes/typos** mediante reglas de texto:  
  - Especializaciones, maestrías, doctorados, PhD → **POSGRADO**.  
  - Universitario/profesional/pregrado → **PROFESIONAL**.  
  - Tecnológico → **TECNOLOGICO**.  
  - Técnico → **TECNICO**.  
  - Básica primaria → **PRIMARIA**.  
  - Básica secundaria/bachiller/media → **SECUNDARIA**.  
  - N/A, NA → **NO APLICA**.  
  - Otros/Otra → **OTRO**.  
- **Verificación:** se revisaron las categorías resultantes y sus frecuencias para garantizar homogeneidad.

### 3.2 Reglas de negocio (coherencias lógicas)
- Si **`HIJOS = "NO"`** y **`NUMERO_HIJOS`** estaba vacío, se definió **`NUMERO_HIJOS = 0`**.  
- Se estandarizaron variantes de texto para asegurar la detección (p. ej., “N0” → “NO”).

---

## 4) Tratamiento de faltantes (imputación)
- **Criterio aplicado:** **imputación por mediana** en variables discretas y no negativas, con ajuste a enteros ≥ 0.  
- **Variables tratadas:**
  - **`NUMERO_HIJOS`:** se imputó con la mediana del conjunto, asegurando valores enteros y no negativos.  
  - **`EDAD2`:** se imputó con la mediana y se redondeó a años completos.  
  - **`HIJOS_EN_HOGAR`:** se imputó con la mediana, restringiendo a valores enteros y ≥ 0.  
- **Justificación:** la mediana reduce sensibilidad a atípicos y respeta la naturaleza discreta de los conteos/edad.

---

## 5) Selección final de variables (subconjunto para análisis)
- Se retuvo un subconjunto de **18 columnas** alineadas con el **diccionario de variables** del proyecto:  
  `EDAD2`, `SEXO`, `NIVEL EDUCATIVO`, `ESTRATO`, `CATEGORIA`, `GRADO`, `ESTADO_CIVIL`, `HIJOS`,  
  `HABITA_VIVIENDA_FAMILIAR`, `RELACION_AMBOS_PADRES`, `RELACION_HERMANOS`, `TIPO_RELACION_PAREJA`,  
  `NUMERO_HIJOS`, `RELACION_HIJOS`, `RESPONSABILIDAD_ACADEMICA_BIENESTAR_HIJOS`, `PERS_A_CARG_HIJOS`,  
  `HIJOS_EN_HOGAR`, `HERMANOS`.

- **Cobertura sobre el total de columnas:** **18 / <231> ≈ <8>%**.  

- **Nota de nomenclatura:** en documentación se recomienda la forma **MAYUSCULAS_SIN_TILDES** (p. ej., `NIVEL_EDUCATIVO`, `PERSONAS_A_CARGO_HIJOS`), manteniendo mapeo con las etiquetas originales.

---

## 6) Validaciones posteriores al subconjunto
- **Faltantes:** reprofilado de NA sobre las 18 columnas y confirmación de reducción/control.  
- **Consistencia:** verificación de reglas lógicas (p. ej., `HIJOS = NO` ⇒ `NUMERO_HIJOS = 0`; coherencia con `HIJOS_EN_HOGAR`).  
- **Categorías:** revisión de las categorías resultantes en `NIVEL EDUCATIVO` tras normalización y unificación.

---

## 7) Diccionario resumido (subconjunto utilizado)
- `EDAD2`: edad depurada (años).  
- `SEXO`: categoría biográfica reportada.  
- `NIVEL EDUCATIVO`: máximo nivel alcanzado (contenido normalizado).  
- `ESTRATO`: estrato socioeconómico (si aplica).  
- `CATEGORIA`: categoría laboral/administrativa FAC.  
- `GRADO`: rango jerárquico militar.  
- `ESTADO_CIVIL`: estado civil actual.  
- `HIJOS`: indicador de hijos (sí/no).  
- `HABITA_VIVIENDA_FAMILIAR`: condición de vivienda.  
- `RELACION_AMBOS_PADRES`: calidad de relación con ambos padres.  
- `RELACION_HERMANOS`: calidad de relación con hermanos.  
- `TIPO_RELACION_PAREJA`: situación de pareja.  
- `NUMERO_HIJOS`: total de hijos.  
- `RELACION_HIJOS`: calidad de relación con los hijos.  
- `RESPONSABILIDAD_ACADEMICA_BIENESTAR_HIJOS`: responsable académico/bienestar.  
- `PERS_A_CARG_HIJOS`: número de personas a cargo de los hijos.  
- `HIJOS_EN_HOGAR`: número de hijos que conviven en el hogar.  
- `HERMANOS`: número total de hermanos.

---

Este documento refleja las decisiones de control de calidad para la **versión actual** del dataset. Cualquier cambio posterior (nuevos dominios, reglas o variables) debe registrarse y versionarse para mantener la **trazabilidad** del proceso, se utilizó el versionamiento con **Git/GitHub** y edición en **VS Code** para asegurar reproducibilidad.
 




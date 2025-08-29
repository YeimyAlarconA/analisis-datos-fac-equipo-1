# Proyecto FAC — Análisis Básico de Encuesta de Bienestar Familiar De la Fuerza Aerea Colombiana (FAC)

> **Estado:** En progreso · **Repositorio:** _[Link Repositorio](https://github.com/YeimyAlarconA/analisis-datos-fac-equipo-1.git)_ · **Última actualización:** 2025-08-29

## Objetivo del Proyecto
Trabajar en equipo usando **Git/GitHub** y **Visual Studio Code (VS Code)** para realizar un **análisis descriptivo básico** de datos reales de una **encuesta de bienestar familiar** del personal de la **Fuerza Aérea Colombiana (FAC)**. El foco está en: (1) perfil demográfico, (2) estructura del hogar y (3) control de calidad de la base.

## Organización del Equipo
- **Estudiante A — Líder de análisis demográfico:** Yeimy Alarcón
- **Estudiante B — Especialista en datos familiares:** Maria José Galindo
- **Estudiante C — Experto en calidad de datos:** Lina Rozo

> Cada rol tiene responsabilidades principales (abajo) y tareas de apoyo cruzadas para revisión por pares.

## Alcance Analítico 
### A. Demografía (Líder: Yeimy Alarcon)
Define el alcance demográfico y las variables foco (EDAD, SEXO, NIVEL_EDUCATIVO, ESTRATO, CATEGORIA).

Ejecuta los cruces : NIVEL_EDUCATIVO × SEXO, EDAD × NIVEL_EDUCATIVO y NIVEL_EDUCATIVO × ESTRATO, con indicadores descriptivos y visualizaciones sintéticas.

Entrega tablas y 3–5 gráficos con interpretaciones breves y coordina criterios de corte y segmentación con los roles B y C.

### B. Datos Familiares (Líder: Maria Jose Galindo)

Caracteriza la estructura del hogar (tamaño, PARENTESCO, HIJOS, HIJOS_EN_HOGAR, PERSONAS_A_CARGO_HIJOS) y la dinámica familiar.

Verifica coherencias básicas (p. ej., si HIJOS = NO ⇒ NUMERO_HIJOS = 0) y alinea definiciones con los catálogos del diccionario.

Entrega tablas resumen y gráficos listos para publicación, coordinando segmentaciones con A e informando hallazgos de calidad a C.

### C. Calidad de Datos (Líder: Lina Rozo)
Perfilado y validación: tipado de variables, dominios/catálogos válidos, rangos y formatos.

Completitud: porcentaje y patrón de NA por variable/subgrupo; mapa de faltantes y priorización de campos críticos.


## Diccionario de Variables 

Del conjunto original se seleccionaron únicamente 18 columnas para el análisis.

- `EDAD` : Años cumplidos.
- `SEXO`: Categoría biográfica reportada.
- `NIVEL_EDUCATIVO`: Máximo nivel alcanzado.
- `ESTRATO`: Estrato socioeconómico (si aplica).
- `CATEGORIA`: Categoría laboral/administrativa en la FAC.
- `GRADO`: Rango jerárquico de la persona en la FAC a la fecha de la encuesta.
- `ESTADO_CIVIL`: estado civil actual.
- `HIJOS`: indica si tiene hijos.
- `HABITA_VIVIENDA`: Tenencia/condición de vivienda.
- `RELACION_AMBOS_PADRES`: Calidad de relación con ambos padres.
- `RELACION_HERMANOS`: Calidad de relación con hermanos.
- `TIPO_RELACION_PAREJA`: Situación de pareja.
- `NUMERO_HIJOS`: Total de hijos que tiene.
- `RELACION_HIJO`: Calidad de relación con los hijos.
- `RESPONSABILIDAD_ACADEMICA_BIENESTAR_HIJOS`: Quién asume la responsabilidad académica y de bienestar de los hijos.
- `PERSONAS_A_CARGO_HIJOS`: Nº de personas responsables de los hijos.
- `HIJOS_EN_HOGAR`: Nº de hijos que conviven en el hogar.
- `HERMANOS`: Nº total de hermanos.

## Requisitos Técnicos
- **Python** ≥ 3.10 
- Paquetes sugeridos (Python): `pandas`, `numpy`, `matplotlib`, `seaborn` _(o `plotly` si se requiere interactividad)_
- Editor: **Visual Studio Code (VS Code)** / Jupyter. Formato de notebooks: `.ipynb` en `notebooks/`.

A continuación se presentan los análisis derivados de nuestra exploración sistemática de los datos, desarrollados bajo un flujo de trabajo colaborativo y reproducible con Git/GitHub y Visual Studio Code. Este repositorio consolida los procedimientos, resultados y evidencias que sustentan el estudio —desde la caracterización demográfica y familiar hasta las verificaciones de calidad de la información— siguiendo estándares de versionamiento, documentación y control de cambios. El equipo implementó convenciones de nomenclatura, resguardos de confidencialidad y trazabilidad de transformaciones, de modo que cada hallazgo pueda ser revisado, replicado y ampliado por los integrantes del proyecto y por revisores externos.

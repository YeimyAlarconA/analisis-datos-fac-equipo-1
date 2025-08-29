
# 📊 Resultados del análisis — Proyecto FAC

Aquí documentamos los análisis de nuestro proyecto (A: Demografía · B: Datos familiares · C: Calidad de datos).

---

## 🧹 Calidad de Datos

Aseguramos que el dataset sea **consistente, completo y estandarizado**.  
Partimos de **<6423>** registros y **<231>** variables; para el análisis usamos **18 columnas** (≈ **<8>%**), todas documentadas en el **diccionario**.

---

## ⚙️ Procedimiento

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

## ✅ Resultados

- **Comparabilidad**: categorías unificadas permiten cruces limpios (p. ej., `NIVEL_EDUCATIVO × SEXO/ESTRATO`). 

- **Trazabilidad**: decisiones documentadas y reproducibles con Git/GitHub.

- Dataset con **18 variables** estandarizadas y reglas de negocio aplicadas. 

- **Reducción de faltantes** en variables clave (conteos/edad).  

- **Catálogos** alineados con el **diccionario** del proyecto.

---
# 📊 Análisis Demográfico

Como analista demográfica del equipo, se realizó un análisis de los datos provenientes de la encuesta de bienestar familiar aplicada al personal de la Fuerza Aérea Colombiana (FAC). El propósito fue caracterizar la población encuestada desde una perspectiva demográfica, explorando variables como edad, género, categoría militar, nivel educativo y estrato socioeconómico.

La base de datos fue depurada previamente por el experto en calidad de datos, quedando conformada por 6423 registros y 18 variables listas para su análisis.

## 👤 Análisis de Edad

- Edad mínima: 18 años
- Edad promedio: 36.7 años
- Edad máxima: 69 años
  
El rango de edad más común fue 33–37 años (1267 personas), seguido de 28–32 años (1211 personas).
Esto indica que gran parte del personal de la FAC encuestado se encuentra en edades de madurez profesional, lo que influye en su desarrollo laboral y familiar.

## 🚹🚺 Distribución por Sexo

- Hombres: 4470 (69.6%)
- Mujeres: 1953 (30.4%)
  
Existe una clara predominancia masculina, coherente con el contexto militar.
Sin embargo, la participación femenina es significativa, representando casi un tercio de la muestra, lo que refleja avances en inclusión y diversidad dentro de la institución.
Sí existen diferencias en la distribución por género: los hombres son mayoría, pero las mujeres tienen una presencia importante.

## 🎖️ Categoría Militar

El análisis de la categoría militar muestra que:
- Suboficiales: 2650 personas (grupo más frecuente)
- Civiles: segundo lugar
- Oficiales: menor proporción
  
Los suboficiales concentran la mayor parte de la muestra, por lo que las estrategias de bienestar deben priorizar a este grupo.

## 🎓 Análisis Nivel Educativo y Sexo

![Imagen de WhatsApp 2025-08-29 a las 14 10 04_37d2e8ce](https://github.com/user-attachments/assets/9150b10d-1dad-4b74-b48b-bbafa71fde80)

## 📈 Análisis Edad y Nivel Educativo

![Imagen de WhatsApp 2025-08-29 a las 16 11 58_d2409536](https://github.com/user-attachments/assets/3c8aef27-48fa-41c6-b59b-f0775f128133)

# 🏘️ Análisis Estrato Socioeconómico y Nivel Educativo

![Imagen de WhatsApp 2025-08-29 a las 14 51 36_92c8299f](https://github.com/user-attachments/assets/dc44e5db-52f9-4f16-92df-245b30b7ede8)


# 📖 Análisis Familiar

---

## 🔹 Pregunta 1
**¿Cuál es la distribución del estado civil en la muestra y qué nos dice sobre la conformación familiar?**

La distribución del estado civil evidencia que la mayoría de participantes se encuentran en **unión libre o casados**, lo cual refleja una tendencia hacia la vida en pareja establecida.  

También se observa una proporción considerable de **personas solteras**, lo que indica diversidad en las formas de organización familiar dentro de la muestra.  

La presencia de **divorciados y separados** es menor, pero señala que también existen familias reconstituidas o en transición.  

✅ **En términos generales:** la población analizada mantiene principalmente **estructuras familiares nucleares o en consolidación**, con un segmento relevante que todavía no ha conformado pareja estable.

<img width="760" height="430" alt="image" src="https://github.com/user-attachments/assets/b3dc9e35-1699-4c4d-97a3-0c5cfdf4a191" />


---

## 🔹 Pregunta 2
**¿Qué se observa en cuanto al número de hijos y la responsabilidad sobre ellos?**

En relación con los **hijos**, los datos muestran que una parte importante de los encuestados no tiene hijos, especialmente en los grupos de menor edad, mientras que en las personas de mayor edad se incrementa progresivamente el número de hijos hasta alcanzar un promedio de **casi dos**.  

Esto confirma un patrón coherente con el **ciclo vital familiar**, donde la etapa reproductiva se intensifica entre los **35 y 54 años**.  

En cuanto a la **responsabilidad**, se observa que la **madre** aparece como la principal figura encargada del bienestar académico y emocional de los hijos, aunque en relaciones familiares cercanas es más frecuente la **corresponsabilidad de ambos padres**.  

✅ **Interpretación:** los vínculos positivos entre los miembros de la familia favorecen un mayor compromiso compartido, mientras que en contextos conflictivos la carga recae mayormente en un solo progenitor.

<img width="707" height="433" alt="image" src="https://github.com/user-attachments/assets/f5180330-6f29-42b4-af92-5281751139fb" />


---

## 🔹 Pregunta 3
**¿Cómo se relaciona la convivencia en la vivienda familiar con la calidad de la relación entre los padres?**

Los resultados indican que la mayoría de las personas, independientemente de la calidad de la relación entre sus padres, **no habitan actualmente en la vivienda familiar**.  

Sin embargo, cuando la relación entre los padres es **cercana y positiva**, se observa una **mayor proporción de convivencia** en comparación con relaciones conflictivas o distantes.  

En casos de **conflicto o relaciones deterioradas**, predomina claramente la **no convivencia**, lo cual sugiere que los problemas de pareja tienen un impacto directo en la **estructura del hogar** y en la decisión de continuar o no compartiendo la misma vivienda.  

✅ **Conclusión:** la convivencia familiar se asocia positivamente con relaciones parentales cercanas y de calidad, mientras que los conflictos tienden a **fragmentar la unidad de cohabitación**.

<img width="776" height="437" alt="image" src="https://github.com/user-attachments/assets/b86fa764-a229-463d-9ae1-2f754da30bf3" />


## 🔹 Pregunta 4 Relación con hijos vs responsabilidad académica

✅ Hallazgo central
La calidad de la relación con los hijos se refleja directamente en el compromiso académico:
-	Relación positiva → mayor corresponsabilidad (ambos padres).
-	Relación conflictiva o distante → se delega principalmente en la madre o terceros.
-	La figura paterna tiende a desaparecer del rol educativo cuando la relación con los hijos se debilita.

<img width="999" height="556" alt="image" src="https://github.com/user-attachments/assets/724d3e00-5d51-41ea-8424-e92c249330ce" />


## 🔹 Pregunta 5 Convivencia vs relación entre ambos padres

✅ Hallazgo central
La gráfica revela que:
-	La convivencia en la vivienda familiar es baja en todos los casos, predominando el “No”.
-	Cuando la relación entre padres es cercana, hay más probabilidades de que los hijos sigan habitando con ellos.
-	En cambio, las relaciones distantes o conflictivas tienden a coincidir con ruptura de la convivencia familiar.

<img width="898" height="476" alt="image" src="https://github.com/user-attachments/assets/7d6a1b9b-34e2-474c-93a9-2d8dd06f3d26" />


## 🔹 Pregunta 6	Número de hijos por rango de edad

✅ Hallazgo central
La gráfica evidencia una curva creciente:
-	A menor edad, menos hijos.
-	A medida que aumenta la edad, el número promedio de hijos también crece, alcanzando su punto más alto en la población mayor a 55 años.
Esto es consistente con la idea de que la formación y consolidación familiar ocurre de manera progresiva a lo largo del ciclo de vida.

<img width="781" height="416" alt="image" src="https://github.com/user-attachments/assets/b0293759-4c22-4155-a5d2-df03502eff76" />

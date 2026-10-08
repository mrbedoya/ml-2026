# Introducción al aprendizaje automático

> Versión Markdown generada a partir de `00_2_IntroduccionAprendizajeAutomatico.html` · 19 diapositivas. Los gráficos se describen por su texto; las fórmulas están en LaTeX (`$...$`).

---

## 1. Introducción al aprendizaje automático

_Aprendizaje Automático I · Unidad 1_

Qué es, dónde se aplica y cómo se organiza un proyecto: de la inteligencia artificial a las técnicas de aprendizaje.

UNIVERSIDAD DE ANTIOQUIA JORGE BEDOYA

---

## 2. Machine Learning, Data Science, and Statistics

_Panorama_

> **Gráfico:** Machine Learning, Data Science y Statistics  
> Textos del gráfico: Statistics · Pattern · Recognition · Data · Science · Databases · Data Mining · KDD · Machine · Learning · AI · Computational · Neuroscience

**¿Qué es el aprendizaje automático?**

Subconjunto de la IA que usa máquinas para buscar patrones en los datos y construir modelos lógicos automáticamente.

**Qué cubre de las otras áreas del gráfico**

- **Inteligencia artificial** — es la rama de la IA que logra que las máquinas aprendan de los datos, en lugar de seguir solo reglas programadas a mano.
- **Data Mining y KDD** — aporta los algoritmos con los que se descubren patrones en la etapa de minería del proceso KDD.
- **Reconocimiento de patrones** — comparte su meta de identificar regularidades en los datos, y añade que el modelo mejora con la experiencia.
- **Estadística** — usa su base (probabilidad, inferencia, regresión) para estimar y validar los modelos.
- **Neurociencia computacional** — toma del cerebro la inspiración para las redes neuronales artificiales.

**Databases** queda por fuera: guarda y organiza los datos que el aprendizaje automático necesita, pero no aprende de ellos.

Referencias: Diagrama propio basado en: jamesmccaffrey.wordpress.com/2016/09/29/machine-learning-data-science-and-statistics/ · datasciencecentral.com/ms-data-science-vs-ms-machine-learning-ai-vs-ms-analytics/

---

## 3. Relación entre la IA y el aprendizaje automático

_Panorama_

> **Gráfico:** IA, aprendizaje automático, IA predictiva y generativa  
> Textos del gráfico: INTELIGENCIA ARTIFICIAL · IA · AI · APRENDIZAJE AUTOMÁTICO · ML · IA de · clasificación · y predictiva · IA · generativa

**Inteligencia artificial AI**

Cualquier técnica que permite a los computadores imitar la inteligencia humana usando lógica, reglas si-entonces y aprendizaje automático.

**Aprendizaje automático ML**

Subconjunto de la IA que usa máquinas para buscar patrones en los datos y construir modelos lógicos automáticamente.

**IA de clasificación y predictiva ML**

Reconoce patrones para identificar algo (clasificación) o predice tendencias futuras a partir de patrones estadísticos y datos históricos (predictiva).

**IA generativa DL**

Subconjunto del aprendizaje profundo (DL) que crea contenido e ideas nuevas con grandes modelos preentrenados llamados modelos fundacionales (FMs).

Referencias: Diagrama propio basado en: docs.aws.amazon.com/decision-guides/latest/machine-learning-on-aws-how-to-choose/guide.html

---

## 4. Relación entre la AI y el aprendizaje automático

_Definiciones_

*[Imagen]*

Inteligencia artificial

- **01** Máquina que imita las funciones “cognitivas”: **percibir**, **razonar**, **aprender** y **resolver problemas**<sup>1</sup>
- **02** Rama de las ciencias computacionales encargada de estudiar modelos de cómputo capaces de realizar actividades propias de los seres humanos en base a dos de sus características primordiales: el **razonamiento** y la **conducta**<sup>2</sup>
- **03** La capacidad de un sistema para **interpretar** correctamente datos externos, para **aprender** de dichos datos y emplear esos conocimientos para **lograr tareas** y metas concretas a través de la **adaptación flexible**<sup>3</sup>

Referencias: 1. Poole, David. «Computational Intelligence: A Logical Approach» · 2. Takeya · 3. Andreas Kaplan y Michael Haenlein

---

## 5. Aplicaciones

_Casos de uso_

*[Imagen]*

Finanzas y mercado

- **A** **Financieras y de banca** — Análisis de riesgos de crédito · Obtención de patrones de fraude en tarjetas de crédito · Correlaciones entre indicadores financieros
- **B** **Análisis de mercado** — Análisis de canasta de compra · Segmentación de clientes · Análisis de fidelidad de clientes. Reducción de fuga
- **C** **Seguros y salud privada** — Predicción de clientes que contratarán nuevas pólizas · Determinación de clientes que podrían ser potencialmente caros

---

## 6. Aplicaciones

_Casos de uso_

*[Imagen]*

Salud y ciencia

- **D** **Educación** — Selección o captación de estudiantes · Detección de abandonos o fracaso
- **E** **Medicina** — Identificación de patologías · Recomendación priorizada de fármacos
- **F** **Biología** — Análisis de secuencias de genes · Modelos de calidad del agua
- **G** **Telecomunicaciones · Procesos industriales · Etc.**

---

## 7. Perspectiva técnica

_Metodologías_

*[Imagen]*

Metodologías

Tres marcos de referencia para organizar un proyecto de análisis de datos:

- **01** **KDD · Knowledge Discovery in Databases**
- **02** **CRISP-DM · Cross Industry Standard Process for Data Mining**
- **03** **Big Data Analysis Pipeline · desafíos**

---

## 8. KDD: Knowledge Discovery in Databases process

_Metodología 1_

> **Gráfico:** Proceso KDD  
> Textos del gráfico: Selection · Selección · Preprocessing · Preprocesamiento · Transformation · Transformación · Data Mining · Minería de datos · Interpretation / Evaluation · Interpretación / Evaluación · Data · Datos · Target Data · Datos objetivo · Preprocessed Data · Datos preprocesados · Transformed Data · Datos transformados · Patterns · Patrones · Information · Información

1 · Selección 2 · Preprocesamiento 3 · Transformación 4 · Minería de datos 5 · Interpretación / Evaluación 6 · Actualización y monitorización

Referencias: Diagrama propio basado en: “From Data Mining to Knowledge Discovery”, AI Magazine, Vol 17, No. 3 (1996) · aaai.org/ojs/index.php/aimagazine/article/view/1230

---

## 9. Selección

_KDD · paso 1 de 6_

- **1** Selección e integración de los datos objetivo provenientes de fuentes múltiples y heterogéneas

> **Gráfico:** Proceso KDD  
> Textos del gráfico: Selection · Selección · Preprocessing · Preprocesamiento · Transformation · Transformación · Data Mining · Minería de datos · Interpretation / Evaluation · Interpretación / Evaluación · Data · Datos · Target Data · Datos objetivo · Preprocessed Data · Datos preprocesados · Transformed Data · Datos transformados · Patterns · Patrones · Information · Información

---

## 10. Preprocesamiento

_KDD · paso 2 de 6_

- **•** Eliminación de ruido y datos aislados o *outliers*.
- **•** Uso del conocimiento previo para eliminar las inconsistencias y los duplicados.
- **•** Escogencia y uso de estrategias para manejar la información faltante en los datasets.

> **Gráfico:** Proceso KDD  
> Textos del gráfico: Selection · Selección · Preprocessing · Preprocesamiento · Transformation · Transformación · Data Mining · Minería de datos · Interpretation / Evaluation · Interpretación / Evaluación · Data · Datos · Target Data · Datos objetivo · Preprocessed Data · Datos preprocesados · Transformed Data · Datos transformados · Patterns · Patrones · Information · Información

---

## 11. Transformación

_KDD · paso 3 de 6_

- **•** Preparación de los datos para el análisis.
- **•** Uso de transformaciones de atributos como: numerización, discretización, etc.
- **•** El resultado es un conjunto de filas y columnas denominado **vista minable**.

> **Gráfico:** Proceso KDD  
> Textos del gráfico: Selection · Selección · Preprocessing · Preprocesamiento · Transformation · Transformación · Data Mining · Minería de datos · Interpretation / Evaluation · Interpretación / Evaluación · Data · Datos · Target Data · Datos objetivo · Preprocessed Data · Datos preprocesados · Transformed Data · Datos transformados · Patterns · Patrones · Information · Información

---

## 12. Minería de datos

_KDD · paso 4 de 6_

- **•** Análisis de los patrones o relaciones a descubrir.
- **•** Se comprende de 3 pasos: **selección de la tarea** · **selección del algoritmo(s)** · **aplicación / entrenamiento del algoritmo**.

> **Gráfico:** Proceso KDD  
> Textos del gráfico: Selection · Selección · Preprocessing · Preprocesamiento · Transformation · Transformación · Data Mining · Minería de datos · Interpretation / Evaluation · Interpretación / Evaluación · Data · Datos · Target Data · Datos objetivo · Preprocessed Data · Datos preprocesados · Transformed Data · Datos transformados · Patterns · Patrones · Information · Información

---

## 13. Interpretación / Evaluación

_KDD · paso 5 de 6_

- **•** Implementación, interpretación o difusión del modelo.

> **Gráfico:** Proceso KDD  
> Textos del gráfico: Selection · Selección · Preprocessing · Preprocesamiento · Transformation · Transformación · Data Mining · Minería de datos · Interpretation / Evaluation · Interpretación / Evaluación · Data · Datos · Target Data · Datos objetivo · Preprocessed Data · Datos preprocesados · Transformed Data · Datos transformados · Patterns · Patrones · Information · Información

---

## 14. Actualización y monitorización

_KDD · paso 6 de 6_

- **•** Consiste en ir revalidando el modelo con cierta frecuencia sobre nuevos datos, con el objetivo de detectar si el modelo requiere una actualización.

> **Gráfico:** Proceso KDD  
> Textos del gráfico: Selection · Selección · Preprocessing · Preprocesamiento · Transformation · Transformación · Data Mining · Minería de datos · Interpretation / Evaluation · Interpretación / Evaluación · Data · Datos · Target Data · Datos objetivo · Preprocessed Data · Datos preprocesados · Transformed Data · Datos transformados · Patterns · Patrones · Information · Información

---

## 15. CRISP-DM

_Metodología 2_

> **Gráfico:** Ciclo CRISP-DM  
> Textos del gráfico: 01 · ENTENDIMIENTODEL NEGOCIO · 02 · ENTENDIMIENTODE LOS DATOS · 03 · PREPARACIÓNDE LOS DATOS · 04 · MODELADO · 05 · EVALUACIÓN · 06 · DESPLIEGUE · DATOS

**Cross Industry Standard Process for Data Mining** — seis fases en un ciclo alrededor de los datos:

1. 1 Entendimiento del negocio

2. 2 Entendimiento de los datos

3. 3 Preparación de los datos

4. 4 Modelado

5. 5 Evaluación

6. 6 Despliegue

Referencias: Diagrama propio basado en el ciclo CRISP-DM · imagen de referencia original: www.iic.uam.es

---

## 16. Big Data Analysis Pipeline

_Metodología 3_

CCC Big Data Pipeline from 2012\*

**Acquisition / Recording**Adquisición / Registro

**Extraction / Cleaning / Annotation**Extracción / Limpieza / Anotación

**Integration / Aggregation / Representation**Integración / Agregación / Representación

**Analysis / Modeling**Análisis / Modelado

**Interpretation**Interpretación

Desafíos en el Análisis de Big Data

Heterogeneity

Scale

Timeliness

Privacy

Human Collaboration

Overall System

Referencias: *From the Computing Community Consortium Big Data Whitepaper · cra.org/ccc/files/docs/init/bigdatawhitepaper.pdf

**Desafíos en el análisis de Big Data**

1. 1 Heterogeneidad e incompletitud

2. 2 Escalar: volumen de datos

3. 3 Puntualidad (*timeliness*): velocidad

4. 4 Privacidad

5. 5 Colaboración humana: un sistema de análisis de Big Data debe admitir la aportación de múltiples expertos humanos y la exploración compartida de resultados

---

## 17. Tareas de aprendizaje

_Relación entre las tareas y las técnicas de aprendizaje_

**Predictivo Supervisado Aprende con la respuesta conocida**

**Regresión**

Predecir un valor numérico

**Clasificación**

Predecir una categoría

**Descriptivo No supervisado Descubre estructura sin etiquetas**

**Análisis exploratorio**

Correlaciones (y dependencias) · Asociaciones

**Agrupamiento**

Clustering: formar grupos afines

**Reducción de la dimensionalidad**

Pasar de muchas variables a pocas

---

## 18. Técnicas

_Relación entre las tareas y las técnicas de aprendizaje_

| Técnica | Predictivo · supervisado | Descriptivo · no supervisado | Tareas |   |   |   |
| --- | --- | --- | --- | --- | --- | --- |
| Clasificación | Regresión | Clustering | Reglas de asociación | Otros factoriales, correl., dispersión |   |   |
| Redes Neuronales |   |   | *\** |   |   |   |
| Árboles de Decisión | *c4.5* | *CART* |   |   |   |   |
| Kohonen |   |   |   |   |   |   |
| Regresión lineal (local, global), exp.. |   |   |   |   |   |   |
| Reg. Logística |   |   |   |   |   |   |
| Kmeans | *\** |   |   |   |   |   |
| A Priori (asociaciones) |   |   |   |   |   |   |
| Estudios Factoriales, análisis multivariante |   |   |   |   |   |   |
| CN2 (Covering Algorithm · basado en reglas) |   |   |   |   |   |   |
| K-NN |   |   |   |   |   |   |
| RBF Radial-Basis Function |   |   |   |   |   |   |
| Bayes Classifiers |   |   |   |   |   |   |

José Hernández Orallo — Extracción Automática de Conocimiento en Bases de Datos e Ingeniería del Software

---

## 19. ¿Pre guntas ?

_Introducción al aprendizaje automático_

IA ⊃ ML KDD CRISP-DM Big Data Supervisado · No supervisado

github.com/mrbedoya/ml-2026

jorge·ml APRENDIZAJE AUTOMÁTICO I

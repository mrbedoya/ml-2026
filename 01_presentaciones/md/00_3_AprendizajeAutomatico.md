# Aprendizaje automático

> Versión Markdown generada a partir de `00_3_AprendizajeAutomatico.html` · 38 diapositivas. Los gráficos se describen por su texto; las fórmulas están en LaTeX (`$...$`).

---

## 1. Aprendizaje automático

_Analítica de datos · Universidad de Antioquia_

Tareas, modelos y su evaluación: del aprendizaje supervisado al no supervisado, y otros temas de aprendizaje.

Aprendizaje Automático I Supervisado · No supervisado

UNIVERSIDAD DE ANTIOQUIA JORGE BEDOYA

---

## 2. Temas a tratar

_Contenido_

*[Imagen]*

Aprendizaje

- **01** **Introducción**
- **02** **Tareas de aprendizaje**
- **03** **Modelos**
- **04** **Evaluación de modelos**
- **05** **Modelos supervisados** — Predicción Clasificación
- **06** **Modelos no supervisados** — Clustering Asociaciones Correlaciones Reducción de datos
- **07** **Otros temas de aprendizaje** — Series temporales Minería de texto Datos atípicos

Referencias: animalmascota.com/fotos-de-mamas-oso-ensenando-sus-crias

---

## 3. Aprendizaje automático: el mapa general

_1 · Introducción_

> **Gráfico:** Mapa del aprendizaje automático  
> Textos del gráfico: Machine · Learning · Aprendizaje automático · Supervised · Learning · Supervisado · Unsupervised · Learning · No supervisado · Reinforcement · Learning · Por refuerzo · Regression · Regresión · Classification · Clasificación · Dimensionality · Reduction · Reducción de dimens. · Clustering · Agrupamiento

Referencias: Diagrama propio basado en: youtu.be/oT3arRRB2Cw?list=PL-Ogd76BhmcDxef4liOGXGXLL-4h65bs4

---

## 4. 2 · Tareas de aprendizaje

_Modelos y tareas_

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

## 5. Aplicaciones por tipo de aprendizaje

_2 · Tareas de aprendizaje_

Machine LearningAprendizaje automático

Supervised LearningAprendizaje supervisado

ClassificationClasificación

- Detección de fraudes
- Detección de spam
- Diagnósticos
- Clasificación de imágenes
- Clasificación de clientes

RegressionRegresión

- Predicción de scores
- Evaluación de riesgos
- Estimación de precios

Unsupervised LearningAprendizaje no supervisado

ClusteringAgrupamiento

- Marketing dirigido
- Segmentación de clientes
- Sistemas recomendadores

Dimensionality ReductionReducción de dimensionalidad

- Minería de texto
- Reconocimiento de imágenes
- Visualización de Big Data

Reinforcement LearningAprendizaje por refuerzo

- Juegos de IA
- Navegación de robots
- Sector financiero
- Manejo de inventarios

---

## 6. Aprendizaje supervisado y no supervisado

_2 · Tareas de aprendizaje_

Predictivo

Supervisado

Objetivo Crear una función capaz de predecir el valor correspondiente a cualquier objeto de entrada válida, después de haber visto una serie de ejemplos (datos de entrenamiento).

*✓*Existe conocimiento previo: **tiene una variable de salida**.

El resultado puede ser

Un valor numérico · **regresión** Una etiqueta de clase · **clasificación**

VS

Descriptivo

No supervisado

Objetivo Comprender los datos: la relación entre las variables y entre las instancias (ejemplos).

*✓*No hay conocimiento a priori: **no tiene un atributo de salida**. Comúnmente requiere un proceso posterior.

El resultado es

Asociaciones y dependencias · **variables categóricas** Correlaciones · **variables numéricas** Agrupaciones · **entre instancias**

¿Qué variables le aportan al modelo? ¿Qué transformaciones me permiten reducir la dimensionalidad?

---

## 7. Modelos y evaluación de modelos

*[Imagen]*

03

[▶ Video Modelos](https://www.youtube.com/watch?v=Sb8XVheowVQ&list=PL-Ogd76BhmcDxef4liOGXGXLL-4h65bs4&index=5)

---

## 8. Modelos

_3 · Modelos_

Modelo\*

Permiten comprender los datos, sus atributos y relaciones:

> **Gráfico:** Modelo paramétrico: recta

**Paramétricos**

Un **número fijo de parámetros** define la forma del modelo.

`a₀ + a₁x₁ + … + aₙxₙ`

Regresión lineal Regresión logística Naive Bayes (gaussiana) SVM lineal

> **Gráfico:** Modelo no paramétrico: curva flexible

**No paramétricos**

No presuponen una **forma concreta**: se adaptan a los datos.

k-NN Árboles de decisión Random Forest Gradient Boosting (XGBoost, LightGBM) SVM con kernel (RBF, polinomial)

Referencias: * youtube.com/watch?v=Sb8XVheowVQ&list=PL-Ogd76BhmcDxef4liOGXGXLL-4h65bs4&index=5 · youtube.com/watch?v=CELZmc56v4I

---

## 9. Paramétricos y no paramétricos

_3 · Modelos_

**Paramétricos**

Construyen la función que aproxima los datos de entrenamiento a la variable objetivo con un **número fijo de parámetros**.

Por ejemplo, la regresión lineal tiene la forma:

`a₀ + a₁x₁ + a₂x₂ + … + aₙxₙ`

**Ejemplos**

Regresión lineal Regresión logística Naive Bayes (distribución gaussiana) SVM lineal

**Ventajas**

- Fáciles de entender
- Entrenamiento suele ser rápido

**Desventajas**

- Limitan la complejidad del modelo generado

**No paramétricos**

No presuponen una **forma concreta** en el modelo a generar.

**Ejemplos**

k-NN Árboles de decisión Random Forest Gradient Boosting (XGBoost, LightGBM) SVM con kernel (RBF, polinomial)

**Ventajas**

- Más flexibles y dando generalmente mejor resultado

**Desventajas**

- Requieren más datos para su entrenamiento y resultan más lentos
- Más proclives al sobreentrenamiento y más difíciles de interpretar

Referencias: interactivechaos.com/es/manual/tutorial-de-machine-learning/algoritmos-parametricos

---

## 10. Validación de modelos

_4 · Evaluación de modelos_

**Validación de modelos:** miden la eficacia de un modelo.

> **Gráfico:** Holdout y validación cruzada  
> Textos del gráfico: Método de retención · (holdout method) · 80% · 20% · Datos etiquetados conocidos · Datos de entrenamiento · Datos de validación · Validación cruzada (cross validation) · Iter. 1 · Iter. 2 · Iter. 3 · k=4 · Recuadro = datos de prueba de esa iteración; el resto es entrenamiento.

---

## 11. Ajuste de un modelo

_4 · Evaluación de modelos_

**Ajustar un modelo** es calcular sus parámetros con los datos. Por ejemplo, en **y = a + bx**, a y b son los parámetros.

Regresión lineal

> **Gráfico:** Regresión lineal: ventas  
> Textos del gráfico: Ventas · y = 359,62x + 441,67 · R² = 0,9332 · 0 · 1.000 · 2.000 · 3.000 · 4.000 · 5.000 · 6.000 · 0 · 2 · 4 · 6 · 8 · 10 · 12 · 14

**Ajuste de una recta** por mínimos cuadrados. Parámetros: **a** (intercepto) y **b** (pendiente).

Distribución gaussiana

> **Gráfico:** Curvas gaussianas con distintos parámetros  
> Textos del gráfico: 0 · 0,2 · 0,4 · 0,6 · 0,8 · 1 · -5 · -4 · -3 · -2 · -1 · 0 · 1 · 2 · 3 · 4 · 5 · μ=0, σ²=0.2 · μ=0, σ²=1.0 · μ=0, σ²=5.0 · μ=-2, σ²=0.5

**Ajuste de una distribución.** Parámetros: **μ** (media) y **σ²** (varianza) que definen la curva.

Red neuronal

> **Gráfico:** Red neuronal

**Ajuste de una red.** Los parámetros son los **pesos** entre neuronas, calculados con los datos.

---

## 12. Matriz de confusión

_4 · Evaluación de modelos_

PREDICCIÓN

Positivo

Negativo

REAL

Positivo

Negativo

**VP**verdadero positivo

**FN**falso negativo

**FP**falso positivo

**VN**verdadero negativo

Clasificación

**Exactitud**

Proporción de instancias identificadas **correctamente** entre todas las instancias.

`(VP + VN) / (VP + FN + FP + VN)`

**Tasa de errores**

Proporción de instancias identificadas **incorrectamente** entre todas las instancias.

`(FP + FN) / (VP + FN + FP + VN)`

---

## 13. Funciones de valor residual (Regresión)

_4 · Evaluación de modelos_

- **✓** Diferencia entre el valor predicho (o *score*) y el valor real.

Error medio cuadrado (Mean squared error) o MSE

`MSE = *1**N* Σ<sub>i=1</sub><sup>N</sup> (f(xᵢ) − yᵢ)²`

Regresión

> **Gráfico:** Residuales en una regresión: y-intercept, punto (x1, y1) y residual y2 − ŷ2  
> Textos del gráfico: y (dependiente) · x (independiente) · línea: y = a + bx · y-intercept · y1 · x1 · ŷ2 · y2 · y2 − ŷ2 · Minimizar: · Σ (yᵢ − ŷᵢ)² · Método de mínimos · cuadrados

---

## 14. Modelos supervisados

*[Imagen]*

05

---

## 15. Predicción

_5 · Modelos supervisados_

*[Imagen]*

Predecir un valor

- **✓** **Regresión lineal** — Técnica estadística para predecir valores de una variable continua dependiente con base en valores de una variable independiente.
- ? ¿Cuántos? ¿Cuántas personas van a comprar el próximo mes? · ¿Cuántos emails van a abrir?

---

## 16. Predicción: el precio de un diamante

_5 · Modelos supervisados_

*[Imagen]*

| quilates | precio |
| --- | --- |
| 1.01 | $7.366 |
| 0.49 | $985 |
| 0.31 | $544 |
| 1.51 | $9.140 |
| 0.37 | $493 |
| 0.73 | $3.011 |
| 1.53 | $11.413 |
| 0.56 | $1.814 |
| 0.41 | $876 |
| 0.74 | $2.690 |
| 0.63 | $1.991 |
| 0.6 | $4.172 |
| 2.06 | $11.764 |
| 1.1 | $4.682 |
| 1.32 | $6.171 |
| 2.02 | $15.996 |
| 0.34 | $695 |

> **Gráfico:** Regresión lineal: precio de diamantes, con banda de error  
> Textos del gráfico: 0 · 5.000 · 10.000 · 15.000 · 20.000 · 0 · 0.5 · 1 · 1.5 · 2 · peso (quilates) · precio (USD) · 1,4 ct → ≈ $8.700 · ± margen de error (1σ)

**Regresión lineal:** cada punto es un diamante (peso vs. precio). La recta ajustada (precio ≈ -2.338 + 7.854 × quilates) permite predecir el precio de un diamante nuevo.

---

## 17. Predicción: técnicas

_5 · Modelos supervisados_

**Regresión lineal**

- Proceso estadístico para estimar las relaciones entre variables.
- Ayuda a entender cómo el valor de la variable dependiente varía al cambiar el valor de una de las variables independientes.
- Se ve afectado por los valores atípicos.

También se usan para predicción

**Máquinas de vectores de soporte**

> **Gráfico:** SVM: hiperplano que separa las clases con el mayor margen

**Redes neuronales**

> **Gráfico:** Redes neuronales: capas de nodos conectados

**Árboles de decisión**

> **Gráfico:** Árboles de decisión: divide el problema en particiones sucesivas

---

## 18. Clasificación

_5 · Modelos supervisados_

*[Imagen]*

¿A qué clase pertenece?

- **✓** **Técnica que permite identificar a qué clase pertenece una instancia**
- ? ¿Cuál categoría? ¿La imagen es un gato o un perro? · ¿El cliente es de perfil de riesgo alto, medio o bajo? · ¿El twit es positivo, negativo o neutro?

---

## 19. Clasificación: técnicas (1/2)

_5 · Modelos supervisados_

**K-NN: K-vecinos más cercanos**

- Se basa en similitud (distancia).
- Buen desempeño en instancias difíciles de explicar.
- Requiere gran cantidad de memoria.
- Se ve afectado por datos atípicos.

**Regresión logística**

- Probabilidad de que una instancia pertenezca o no a una clase.
- Modelo simple, rápido de entrenar e interpretar.

**Naïve Bayes**

- Se basa en probabilidades.
- Es capaz de tener en cuenta las características que parecen insignificantes (características independientes).
- Permite seleccionar las mejores instancias.
- Poca información de falsos positivos y negativos.
- Usa solo valores categóricos.
- Modelos eficientes y rápidos.

---

## 20. Clasificación: técnicas (2/2)

_5 · Modelos supervisados_

**Árboles de decisión**

- Divide el problema en partes.
- Los modelos son fáciles de comprender.
- Requieren definir criterio de parada (pre-poda, post-poda).
- Si se requiere post-poda, requiere muchos recursos.

**Máquinas de vectores de soporte**

- Buscan un hiperplano que separe lo mejor posible las clases.
- Pueden usar muchos tipos de **funciones del núcleo** que permiten encontrar una separación no lineal de las clases.

**Reglas de clasificación**

- Modelos basados en reglas.
- Fáciles de comprender.
- Características nominales.
- Pueden ser utilizadas para identificar datos atípicos.

**Redes neuronales**

- Gran capacidad de ser utilizadas como mecanismo de función de aproximación arbitraria que “aprende” a partir de datos observados.
- No es fácilmente comprensible el porqué de su respuesta.

---

## 21. Modelos no supervisados

*[Imagen]*

06

---

## 22. Clustering (agrupamiento)

_6 · Modelos no supervisados_

*[Imagen]*

Grupos naturales

- **✓** **Técnica que permite clasificar de acuerdo con propiedades de grupos homogéneos (agrupación natural)**
- ? ¿Cuáles grupos? ¿Cuáles compradores tienen gustos similares? · ¿Cuáles temas se están hablando en redes sociales? · ¿Cuáles tiendas son similares?

---

## 23. Clustering: técnicas

_6 · Modelos no supervisados_

**K-medias**

- Se debe definir el número de grupos (k).
- Se emplea el algoritmo de K-medias.
- Cada grupo debe ser analizado y etiquetado manualmente.

**DBSCAN**

- Agrupamiento basado en densidad: agrupa puntos cercanos y marca como ruido los que quedan aislados.

**Hierarchical clustering**

- Agglomerative (de abajo hacia arriba) o divisivo (de arriba hacia abajo).
- Sus resultados pueden representarse como un árbol en el que las ramas representan la jerarquía con la que se van sucediendo las uniones de *clusters*.

**Spectral clustering**

- Agrupamiento a partir de la estructura de similitud entre los datos, útil cuando los grupos no son esféricos.

---

## 24. Asociaciones, dependencias o correlaciones

_6 · Modelos no supervisados_

*[Imagen]*

Relaciones

- **A** **Correlaciones** — Cómo se relacionan dos variables numéricas.
- **B** **Asociaciones** — Reglas entre variables categóricas (Apriori).
- **C** **Dependencias** — ¿Existe una dependencia entre 2 o más variables?

---

## 25. Correlaciones

_6 · Modelos no supervisados_

*[Imagen]*

Dependencia entre variables

- **✓** **Correlación** — Medida estadística que nos ayuda a entender cómo dos variables se relacionan entre sí.
- ? ¿Existe una dependencia entre 2 o más variables? Correlación entre el consumo de tabaco y el riesgo de cáncer de pulmón · Correlación entre el nivel de educación y el ingreso salarial

---

## 26. Correlaciones: técnicas

_6 · Modelos no supervisados_

**Pearson −1 a +1**

- Mide la relación **lineal** entre dos variables continuas.
- Sensible a los valores atípicos.

> **Gráfico:** Pearson: relación lineal fuerte

**Ejemplo:** gasto en publicidad vs. ventas mensuales.

**Spearman −1 a +1**

- Evalúa la relación entre variables ordinales o no lineales.
- Utiliza rangos en lugar de valores exactos.
- Útil cuando los datos no siguen una distribución normal.

> **Gráfico:** Spearman: relación monótona no lineal

**Ejemplo:** satisfacción del cliente (encuesta) vs. probabilidad de recompra.

**Kendall −1 a +1**

- Mide la concordancia entre los rangos de dos variables (pares concordantes vs. discordantes).
- Más robusta ante valores atípicos que Spearman.

> **Gráfico:** Kendall: pares concordantes (izq.) vs. discordantes (der.)

**Ejemplo:** acuerdo entre dos jueces al ordenar candidatos de un proceso de selección.

---

## 27. Asociaciones: reglas de asociación (Apriori)

_6 · Modelos no supervisados_

*[Imagen]*

Canasta de compra

- **1** **Reglas accionables** — Fáciles de entender y ofrecen conocimiento accionable. {colchón} → {almohada}
- **2** **Reglas triviales** — Son claras, pero dan algo de valor adicional. {zapatos} → {correa}
- **3** **Reglas inexplicables** — No son claras y no ofrecen ningún conocimiento práctico. {pañales} → {cerveza}

---

## 28. Técnicas de reducción de datos

_6 · Modelos no supervisados_

*[Imagen]*

Menos, pero mejor

- **✓** **Reducción de la dimensionalidad**

**Selección de características:**

Selección hacia adelante Eliminación hacia atrás PCA RFE Inducción del árbol de decisión

**Extracción de características**

- **✓** **Discretización de los datos** — Binning Agrupamiento

---

## 29. Otros temas de aprendizaje

*[Imagen]*

07

---

## 30. Series temporales

_7 · Otros temas de aprendizaje_

**Series temporales**

Agrupa una serie de datos recopilados cronológicamente en intervalos de tiempo constantes.

- **Tendencia**
- **Estacionalidad**

> **Gráfico:** Serie de tiempo irregular con tendencia y estacionalidad anual tipo diente de sierra  
> Textos del gráfico: sales time series · serie de ventas · $ · 1M · 2M · 3M · 4M · 5M · 1989 · 1990 · 1991 · 1992 · 1993 · 1994 · 1995 · 1996 · 4.6 M · original · tendencia

*[Imagen: Guepardo corriendo: varios instantes de tiempo capturados en una sola imagen]*

El movimiento es, en el fondo, una serie de posiciones en el tiempo

---

## 31. Minería de texto

_7 · Otros temas de aprendizaje_

*[Imagen]*

Leer entre líneas

- **✓** **Técnicas de minería de texto para:**
- Recuperar información
- Clasificar documentos, según categorías conocidas
- Encontrar grupos de documentos similares
- Análisis de sentimientos

---

## 32. Minería de texto: bolsa de palabras

_7 · Otros temas de aprendizaje_

**Ej:** *Doc 1:* El **carro moderno** rojo es **rápido** y elegante · *Doc 2:* El **carro moderno** azul es **rápido** y económico

|   | carro | moderno | rojo | azul | rápido | elegante | económico |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Doc 1 | 1 | 1 | 1 | 0 | 1 | 1 | 0 |
| Doc 2 | 1 | 1 | 0 | 1 | 1 | 0 | 1 |

**Técnicas**

- Bolsas de palabras
- Frecuencias de términos
- Frecuencia inversa de documento
- Se deben aplicar técnicas de normalización, *stemming* y eliminación de *stopwords*

---

## 33. Minería de texto: n-gramas y entidades

_7 · Otros temas de aprendizaje_

**N-gramas**

| Bi-gramas | Tri-gramas |
| --- | --- |
| smoking_patient | smoking_patient_with |
| patient_with | patient_with_lung |
| with_lung | with_lung_cancer |
| lung_cancer |   |

*[Imagen]*

**Extracción de entidades con nombre reemplazada por IA generativa**

- **Nombre:** personas, lugares, empresas
- **Patrón:** coordenadas, códigos
- **Conceptos:** un automóvil, un humano
- **Hechos:** vínculos entre entidades
- **Sentimientos:** actitudes, gestos o emociones

Hoy, buena parte de esta tarea ha sido reemplazada por la **IA generativa** → siguiente diapositiva.

---

## 34. ¿Minería de texto o IA generativa?

_7 · Otros temas de aprendizaje_

Reglas y estadística

Minería de texto

Úsala cuando Necesitas **explicabilidad** y bajo costo computacional: bolsa de palabras, n-gramas, clasificación por categorías conocidas, análisis de frecuencia.

*✓*Resultados **trazables**: se puede explicar por qué se extrajo cada patrón.

VS

Modelos preentrenados

IA generativa

Úsala cuando La tarea exige **comprender contexto y significado**: resúmenes, respuesta a preguntas abiertas, generación de texto y, hoy, buena parte de la **extracción de entidades con nombre**.

*✓*Mayor **flexibilidad** ante lenguaje variado, a costa de menor trazabilidad y mayor costo computacional.

---

## 35. Detección de datos atípicos (outliers)

_7 · Otros temas de aprendizaje_

*[Imagen]*

¿Cuál es extraño?

- **✓** **Se diferencia del ruido en que este no es suficientemente importante para marcarlo como atípico**
- **✓** **¿Cuál es extraño?** — ¿Un cliente puede registrar tantas facturas en un día? · ¿Un cliente puede comprar tanto en un día?

---

## 36. Detección de datos atípicos: tipos

_7 · Otros temas de aprendizaje_

*[Imagen]*

Tipos

- **1** **Global o puntual** — Un dato suficientemente inconsistente.
- **2** **Contextual** — Es consistente dentro de un contexto.
- **3** **Colectivo** — Es atípico si está combinado con otro dato similar, sin condiciones ni contextos.

---

## 37. Detección de datos atípicos: técnicas

_7 · Otros temas de aprendizaje_

**Estadísticas**

- Operan con base en un ajuste de distribución. Ej.: valores que se encuentren a 3 desviaciones estándar son atípicos.
- Valores que no pertenecen a un bin o pertenecen al bin de puntuación alta.
- Valores que no pertenecen al rango intercuartil.

**Basadas en distancias**

- Agrupamiento K-medias.
- K-NN.

**Supervisadas**

- Con algunos datos de ejemplo, desarrollar un modelo de detección de datos atípicos.

**Semi-supervisadas**

- Primero se realiza un agrupamiento.
- Todos los puntos o clusters individuales que no pertenezcan a un cluster son considerados atípicos.

---

## 38. ¡ Gracias !

_Aprendizaje automático_

Tareas de aprendizaje Modelos Evaluación Supervisado No supervisado Otros temas

github.com/mrbedoya/ml-2026

jorge·ml ANALÍTICA DE DATOS

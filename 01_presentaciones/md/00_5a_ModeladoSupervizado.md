# Métodos supervisados (1/2) · fiel al PDF

> Versión Markdown generada a partir de `00_5a_ModeladoSupervizado.html` · 40 diapositivas. Los gráficos se describen por su texto; las fórmulas están en LaTeX (`$...$`).

---

## 1. Métodos supervisados

_Analítica de datos · Universidad de Antioquia_

Definiciones, preparación de datos y temas preliminares antes de entrar en las técnicas de modelado.

Aprendizaje Automático I Modelado supervisado

UNIVERSIDAD DE ANTIOQUIA JORGE BEDOYA

---

## 2. Temas a tratar

_Contenido_

*[Imagen]*

Aprendizaje

- **01** **Modelado supervisado**
- **02** **Preparación de datos**
- **03** **Sobreajuste y regularización**
- **04** **Evaluación**

---

## 3. Aprendizaje automático: el mapa general

_1 · Modelado supervisado_

> **Gráfico:** Mapa del aprendizaje automático, con la rama de aprendizaje supervisado resaltada  
> Textos del gráfico: ★ Aprendizaje supervisado · este curso · Unsupervised · Learning · No supervisado · Reinforcement · Learning · Por refuerzo · Dimensionality · Reduction · Reducción de dimens. · Clustering · Agrupamiento · Machine · Learning · Aprendizaje automático · Supervised · Learning · Supervisado · Regression · Regresión · Classification · Clasificación

---

## 4. Aplicaciones por tipo de aprendizaje

_1 · Modelado supervisado_

Machine LearningAprendizaje automático

★ Este curso

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

## 5. Modelado supervisado

*[Imagen]*

01

Qué es el aprendizaje supervisado, cómo se diferencia de otros tipos de aprendizaje, y el proceso general para construir un modelo predictivo.

Mapa del aprendizaje automático Regresión y clasificación Proceso de modelado

---

## 6. ¿Cómo es la variable de salida?

_1 · Modelado supervisado_

- **✓** **Existe una variable de salida o una variable a predecir (para uno o varios ejemplos).**
- **✓** **¿Cómo es la variable de salida?**

Continua

Regresión

¿Cuánto?

*✓*¿Cuántos clientes abrirán el correo?

*✓*¿Cuántas personas no pagarán el crédito?

*✓*Etc.

VS

Discreta

Clasificación

¿Cuál categoría?

*✓*¿El cliente abrirá o no el correo?

*✓*¿Es un hongo venenoso o no?

*✓*¿A qué perfil de riesgo está asociado el cliente?

---

## 7. Modelamiento predictivo: proceso

_1 · Modelado supervisado_

**Intención o interés de aprendizaje**

Un banco quiere averiguar cuáles de sus clientes probablemente estarán en mora en el pago de sus deudas.

> **Gráfico:** Proceso de modelado predictivo: de los datos históricos a la predicción  
> Textos del gráfico: 1 · Datos históricos · Dataset con clientes que · han estado en mora, ya · etiquetados como Bueno o · Malo. · 2 · Entrenamiento · Un algoritmo de · clasificación aprende a · distinguir clientes · "Bueno" de "Malo". · 3 · Predicción · Se ingresan datos nuevos, · sin etiquetar, para · predecir la categoría del · cliente. · Variable objetivo: CategoríaCliente → Bueno / Malo (clasificación)

- ? Variable objetivo CategoríaCliente → Bueno / Malo (Clasificación)

---

## 8. Preparación de datos

*[Imagen]*

02

Antes de modelar: codificar, escalar y reducir la información para que los algoritmos puedan aprovecharla al máximo.

Label / One-Hot Encoding Normalización y escalamiento Reducción de dimensionalidad Desbalanceo de clases

---

## 9. Gestión de características categóricas

_2 · Preparación de datos_

La mayor parte de los algoritmos exigen valores numéricos. ¿Cómo convertir estos valores en números? Dos enfoques:

**Label Encoding**

- Identifica los distintos valores existentes.
- Sustituye cada uno por un número entero.

**One-Hot Encoding**

- Crea una columna para cada valor distinto.
- Marca con 1 la columna del registro y 0 en las demás.

Referencias: <https://interactivechaos.com/es/manual/tutorial-de-machine-learning/gestion-de-caracteristicas-categoricas>

---

## 10. Label Encoding: ejemplo (variable ordinal)

_2 · Preparación de datos_

**Úsalo cuando la variable es ordinal**

Label Encoding funciona mejor con variables **ordinales**: categorías que sí tienen un orden natural. Al asignarles enteros crecientes, ese orden queda representado correctamente.

| Cliente | Nivel de satisfacción |
| --- | --- |
| Ana | Bajo |
| Luis | Alto |
| Marta | Medio |
| Carlos | Alto |
| Julia | Bajo |

→

| Cliente | Satisfacción (codificada) |
| --- | --- |
| Ana | 0 |
| Luis | 2 |
| Marta | 1 |
| Carlos | 2 |
| Julia | 0 |

**¿Por qué funciona aquí?** "Bajo" < "Medio" < "Alto" tiene un orden real, y ese orden se conserva en 0 < 1 < 2. Si se aplicara sobre una variable *sin* orden (como una ciudad), el modelo asumiría una relación de magnitud que no existe.

---

## 11. One-Hot Encoding: ejemplo (variable nominal)

_2 · Preparación de datos_

**Úsalo cuando la variable es nominal**

One-Hot Encoding es la opción correcta para variables **nominales**: categorías sin ningún orden natural entre ellas.

| Transacción | Método de pago |
| --- | --- |
| T1 | Efectivo |
| T2 | Tarjeta |
| T3 | Transferencia |
| T4 | Tarjeta |
| T5 | Efectivo |

→

| Transacción | Efectivo | Tarjeta | Transferencia |
| --- | --- | --- | --- |
| T1 | 1 | 0 | 0 |
| T2 | 0 | 1 | 0 |
| T3 | 0 | 0 | 1 |
| T4 | 0 | 1 | 0 |
| T5 | 1 | 0 | 0 |

**¿Por qué no usar Label Encoding aquí?** Si Efectivo=0, Tarjeta=1 y Transferencia=2, el modelo interpretaría que "Transferencia" es el doble de "Tarjeta": una relación numérica que no existe entre métodos de pago.

---

## 12. Normalización y estandarización

_2 · Preparación de datos_

Homogenizadores: transforman variables **numéricas** a una escala común, para que ninguna domine al modelo solo por tener valores más grandes.

**MinMaxScaler**

Escala los valores a un rango fijo, típicamente [0, 1].

**Normalizer**

Divide cada valor por la norma del vector.

**Estandarizador**

Centra los datos en media = 0 y desviación = 1.

Referencias: <https://www.cienciadedatos.net/documentos/py06_machine_learning_python_scikitlearn.html> · <https://www.youtube.com/watch?v=-VuR14Qyl7E>

---

## 13. MinMaxScaler: ejemplo

_2 · Preparación de datos_

Toma los valores mínimo y máximo como referencia y escala linealmente al rango [0, 1].

`MinMaxScaler(xᵢ) = (xᵢ − mín) / (máx − mín)`

| Nombre | Edad | Edad escalada |
| --- | --- | --- |
| Juan | 80 | 1 |
| Pedro | 50 | 0,5 |
| María | 35 | 0,25 |
| Isabel | 65 | 0,75 |
| Camilo | 20 | 0 |

> **Gráfico:** MinMaxScaler: de la escala original a un rango [0, 1]  
> Textos del gráfico: Edad (original) · 20 · 35 · 50 · 65 · 80 · 0 · 0.25 · 0.5 · 0.75 · 1 · Edad escalada [0, 1]

---

## 14. Normalizer: ejemplo

_2 · Preparación de datos_

Utiliza la norma de un vector: cada valor se divide por la norma.

> **Gráfico:** Fórmula de normalización L1 (Normalizer): xᵢ dividido por la norma del vector  
> Textos del gráfico: NormaL1(xᵢ) · = · xᵢ · x₁² + x₂² + ⋯ + xₙ²

| Nombre | Edad | Normalizada |
| --- | --- | --- |
| Juan | 80 | 0,66 |
| Pedro | 50 | 0,41 |
| María | 35 | 0,29 |
| Isabel | 65 | 0,54 |
| Camilo | 20 | 0,16 |

**Notas:** en scikit-learn los datos deben transponerse (`datos.T`) · comúnmente genera valores muy pequeños.

---

## 15. Estandarizador: ejemplo

_2 · Preparación de datos_

Cambia la distribución de los datos para que tengan media = 0 y desviación = 1.

`Estandarizado(xᵢ) = (xᵢ − media) / std`

**EstRobusto** facilita la exclusión de datos atípicos:

`EstRobusto(xᵢ) = (xᵢ − RangoIntercuartílico) / std`

| Nombre | Edad | Estandarizada | EstRobusto |
| --- | --- | --- | --- |
| Juan | 80 | 1,26 | 2,11 |
| Pedro | 50 | 0,00 | 0,84 |
| María | 35 | −0,63 | 0,21 |
| Isabel | 65 | 0,63 | 1,48 |
| Camilo | 20 | −1,26 | −0,42 |

Media = 50 · Std = 23,72 · RangoIntercuartílico (IQR) = Q₃ − Q₁ = 30.

---

## 16. Reducción de la dimensionalidad

_2 · Preparación de datos_

*[Imagen]*

Menos, pero mejor

- **✓** **Selección de características**

Selección hacia adelante Eliminación hacia atrás PCA RFE Inducción del árbol de decisión

- **✓** **Extracción de características**
- **✓** **Discretización de los datos**

Binning Agrupamiento

---

## 17. Desbalanceo de clases

_2 · Preparación de datos_

**¿Por qué es un problema?**

Cuando una clase tiene muchos menos ejemplos que otra (p. ej. 1 % de fraudes), el modelo aprende a favorecer la **clase mayoritaria**: puede lograr una **exactitud alta sin detectar ningún caso** de la clase minoritaria.

> **Gráfico:** Desbalanceo de clases: datos originales, submuestreo de la clase mayoritaria y sobremuestreo sintético de la minoritaria  
> Textos del gráfico: Datos originales · Mayoritaria 24 · Minoritaria 4 · 86 % / 14 % · Submuestreo · (undersampling) · Mayoritaria 4 · Minoritaria 4 · 50 % / 50 % · Sobremuestreo · (SMOTE) · Mayoritaria 24 · Minoritaria 24 · 50 % / 50 % · clase mayoritaria · clase minoritaria · ejemplo sintético

**Submuestreo**

Elimina ejemplos de la clase mayoritaria. Rápido, pero se pierde información.

**Sobremuestreo**

Duplica o genera ejemplos sintéticos de la minoritaria (SMOTE). Riesgo de sobreajuste.

**Otras opciones**

Pesos de clase, ajustar el umbral de decisión y evaluar con recall, precisión, F1 o AUC.

★ Buena práctica: remuestrea **solo el conjunto de entrenamiento** (nunca prueba/validación) y estratifica la partición para conservar la proporción de clases.

---

## 18. Sobreajuste y regularización

*[Imagen]*

03

Cuando un modelo aprende demasiado bien los datos de entrenamiento —incluido el ruido— y deja de generalizar: cómo detectarlo y cómo corregirlo.

Sobreajuste (overfitting) Regularización L1 / L2 Lasso, Ridge, ElasticNet

---

## 19. Sobreajuste (Overfitting)

_3 · Sobreajuste y regularización_

Si un modelo tiene muchos parámetros, puede ajustarse a los datos de muchas formas distintas — incluyendo el ruido, no solo el patrón real.

`h(X) = θ₀ + θ₁X¹ + θ₂X² + θ₃X³ + ⋯ + θₙXⁿ`

Donde **n** es el grado de la ecuación y **θ** son las pendientes: a mayor grado, más "curvas" puede tomar el modelo.

> **Gráfico:** Sobreajuste: datos con ajustes polinómicos de grado 3, 5 y 9 — el de grado 9 memoriza el ruido  
> Textos del gráfico: -1 · 0 · 1 · 2 · 3 · 4 · 5 · 6 · 7 · 8 · 9 · 0 · 50 · 100 · 150 · 200 · 250 · 300 · 350 · X · Y · Raw Data · 3rd Order Polynomial Fit · 5th Order Polynomial Fit · 9th Order Polynomial Fit

---

## 20. Sobreajuste (Overfitting)

_3 · Sobreajuste y regularización_

Los tres escenarios típicos al ajustar un modelo a los datos:

> **Gráfico:** Mismos datos, tres curvas: recta (subajuste), curva suave (buen ajuste) y curva que persigue cada punto (sobreajuste)  
> Textos del gráfico: Valores · Tiempo · Subajuste · Valores · Tiempo · Buen ajuste · Valores · Tiempo · Sobreajuste

---

## 21. Regularización

_3 · Sobreajuste y regularización_

Consiste en añadir una penalización a la función de costo. Esta penalización produce modelos más simples que generalizan mejor.

**Lasso · L1**

Penaliza con la suma de valores absolutos de los coeficientes.

**Ridge · L2**

Penaliza con la suma de los cuadrados de los coeficientes.

**ElasticNet**

Combina Lasso y Ridge mediante un parámetro r.

---

## 22. Regularización: Lasso (L1)

_3 · Sobreajuste y regularización_

> **Gráfico:** Fórmula de Lasso  
> Textos del gráfico: C · = · 1 · N · · · N · Σ · i=1 · |wᵢ|

> **Gráfico:** Efecto de la regularización lasso: ajuste sin regularizar vs. regularizado  
> Textos del gráfico: y · x · sin regularizar · regularizado

**¿Cuándo usar L1?**

Se sospecha que varios atributos son irrelevantes, y no están muy correlacionados entre sí — Lasso puede llevar sus coeficientes exactamente a cero.

Referencias: <https://www.iartificial.net/regularizacion-lasso-l1-ridge-l2-y-elasticnet/>

---

## 23. Regularización: Ridge (L2)

_3 · Sobreajuste y regularización_

> **Gráfico:** Fórmula de Ridge  
> Textos del gráfico: C · = · 1 · 2N · · · N · Σ · i=1 · wᵢ²

> **Gráfico:** Efecto de la regularización ridge: ajuste sin regularizar vs. regularizado  
> Textos del gráfico: y · x · sin regularizar · regularizado

**¿Cuándo usar L2?**

Varios atributos están correlacionados y la mayoría son relevantes — Ridge encoge los coeficientes sin llevarlos a cero.

Referencias: <https://www.iartificial.net/regularizacion-lasso-l1-ridge-l2-y-elasticnet/>

---

## 24. Regularización: ElasticNet (L1 + L2)

_3 · Sobreajuste y regularización_

`C = r · Lasso + (1 − r) · Ridge`

> **Gráfico:** Efecto de la regularización elastic: ajuste sin regularizar vs. regularizado  
> Textos del gráfico: y · x · sin regularizar · regularizado

**¿Cuándo usar ElasticNet?**

Con muchos atributos, donde algunos serán irrelevantes y otros estarán correlacionados entre sí — combina lo mejor de L1 y L2.

Referencias: <https://www.iartificial.net/regularizacion-lasso-l1-ridge-l2-y-elasticnet/>

---

## 25. Evaluación de modelos

*[Imagen]*

04

Cómo medir si un modelo realmente funciona: validación, matrices de confusión, curvas ROC y funciones de error.

Validación de modelos Matriz de confusión y curva ROC Funciones de error residual

---

## 26. Método de retención (Holdout method)

_4 · Evaluación: validación de modelos_

Consiste en separar los datos en dos grupos disjuntos: uno para **entrenamiento** y otro para **prueba (test)**. El modelo nunca ve los datos de prueba durante el entrenamiento.

> **Gráfico:** Método de retención: partición en dos (70/30) o en tres partes (50/30/20)  
> Textos del gráfico: Dos partes: 70% / 30% · 70% · 30% · Entrenamiento · Validación · Tres partes: 50% / 30% / 20% · 50% · 30% · 20% · Entrenamiento · Validación · Prueba

Referencias: <https://www.interactivechaos.com/manual/tutorial-de-machine-learning/metodo-de-retencion>

---

## 27. Validación cruzada (Cross validation)

_4 · Evaluación: validación de modelos_

- **✓** **Los datos de muestra se dividen en K subconjuntos (k-folds).**
- **✓** **Uno de los subconjuntos se usa como datos de prueba y el resto (K−1) como datos de entrenamiento.**
- **✓** **El proceso se repite durante k iteraciones, cada vez con un subconjunto de prueba distinto.**
- **✓** **El resultado final es el promedio aritmético de los resultados de cada iteración.**

> **Gráfico:** Validación cruzada de 4 particiones: en cada iteración una partición distinta es de prueba y el resto de entrenamiento; el resultado final es el promedio  
> Textos del gráfico: Validación cruzada (cross validation) · k = 4 particiones · Datos de entrenamiento · Datos de prueba · Partición 1 · Partición 2 · Partición 3 · Partición 4 · Resultado · Iteración 1 · PRUEBA · Entrenamiento · R1 · Iteración 2 · Entrenamiento · PRUEBA · Entrenamiento · R2 · Iteración 3 · Entrenamiento · PRUEBA · Entrenamiento · R3 · Iteración 4 · Entrenamiento · PRUEBA · R4 · Resultado final = promedio de R1 … R4

---

## 28. Matriz de confusión: Clasificación

_4 · Evaluación: matriz de confusión y curva ROC_

> **Gráfico:** Matriz de confusión: verdaderos/falsos positivos y negativos  
> Textos del gráfico: PREDICCIÓN · Positivo · Negativo · REAL · Positivo · Negativo · VP · Verdadero Positivo · FN · Falso Negativo · FP · Falso Positivo · VN · Verdadero Negativo

- **VP** es la cantidad de *positivos* que fueron clasificados correctamente como positivos por el modelo.
- **VN** es la cantidad de *negativos* que fueron clasificados correctamente como negativos por el modelo.
- **FN** es la cantidad de *positivos* que fueron clasificados incorrectamente como negativos.
- **FP** es la cantidad de *negativos* que fueron clasificados incorrectamente como positivos.

---

## 29. Exactitud (Accuracy)

_4 · Evaluación: matriz de confusión y curva ROC_

Proporción de instancias identificadas **correctamente** entre todas las instancias.

> **Gráfico:** Matriz de confusión: verdaderos/falsos positivos y negativos  
> Textos del gráfico: PREDICCIÓN · Positivo · Negativo · REAL · Positivo · Negativo · VP · Verdadero Positivo · FN · FP · VN · Verdadero Negativo

> **Gráfico:** Fórmula: Exactitud = VP + VN / VP + VN + FP + FN  
> Textos del gráfico: Exactitud · = · VP + VN · VP + VN + FP + FN

★ Especialmente útil cuando las clases están **balanceadas** (proporciones similares de positivos y negativos).

---

## 30. Tasa de error

_4 · Evaluación: matriz de confusión y curva ROC_

Proporción de instancias identificadas **incorrectamente** entre todas las instancias — el complemento de la exactitud.

> **Gráfico:** Matriz de confusión: verdaderos/falsos positivos y negativos  
> Textos del gráfico: PREDICCIÓN · Positivo · Negativo · REAL · Positivo · Negativo · VP · FN · Falso Negativo · FP · Falso Positivo · VN

> **Gráfico:** Fórmula: Tasa de error = FP + FN / VP + VN + FP + FN  
> Textos del gráfico: Tasa de error · = · FP + FN · VP + VN + FP + FN

★ Igual que la exactitud, solo es representativa con clases **balanceadas**.

---

## 31. Recall (Sensibilidad) y Especificidad

_4 · Evaluación: matriz de confusión y curva ROC_

> **Gráfico:** Matriz de confusión: verdaderos/falsos positivos y negativos  
> Textos del gráfico: PREDICCIÓN · Positivo · Negativo · REAL · Positivo · Negativo · VP · Verdadero Positivo · FN · Falso Negativo · FP · VN

> **Gráfico:** Fórmula: Recall (Sensibilidad) = VP / Total Positivos  
> Textos del gráfico: Recall (Sensibilidad) · = · VP · Total Positivos

★ Útil cuando el costo de un **falso negativo** es alto — ej. diagnóstico médico, detección de fraude.

> **Gráfico:** Matriz de confusión: verdaderos/falsos positivos y negativos  
> Textos del gráfico: PREDICCIÓN · Positivo · Negativo · REAL · Positivo · Negativo · VP · FN · FP · Falso Positivo · VN · Verdadero Negativo

> **Gráfico:** Fórmula: Especificidad = VN / Total Negativos  
> Textos del gráfico: Especificidad · = · VN · Total Negativos

★ Útil cuando el costo de un **falso positivo** es alto — ej. evitar alarmas o acusaciones innecesarias.

---

## 32. Precisión y Valor Predictivo Negativo

_4 · Evaluación: matriz de confusión y curva ROC_

> **Gráfico:** Matriz de confusión: verdaderos/falsos positivos y negativos  
> Textos del gráfico: PREDICCIÓN · Positivo · Negativo · REAL · Positivo · Negativo · VP · Verdadero Positivo · FN · FP · Falso Positivo · VN

> **Gráfico:** Fórmula: Precisión = VP / Total clasif. positivos  
> Textos del gráfico: Precisión · = · VP · Total clasif. positivos

★ Útil cuando el costo de un **falso positivo** es alto — ej. filtros de spam, sistemas de recomendación.

> **Gráfico:** Matriz de confusión: verdaderos/falsos positivos y negativos  
> Textos del gráfico: PREDICCIÓN · Positivo · Negativo · REAL · Positivo · Negativo · VP · FN · Falso Negativo · FP · VN · Verdadero Negativo

> **Gráfico:** Fórmula: VPN = VN / Total clasif. negativos  
> Textos del gráfico: VPN · = · VN · Total clasif. negativos

★ Útil cuando se necesita confiar en las predicciones **negativas** — ej. pruebas de descarte (screening).

---

## 33. F1 Score

_4 · Evaluación: matriz de confusión y curva ROC_

**¿Cuándo es especialmente útil?**

Combina la **precisión** y el **recall** en una sola medida de rendimiento — especialmente útil con conjuntos de datos **desbalanceados**, donde la exactitud puede engañar.

> **Gráfico:** Fórmula: F1 = 2 · Precisión · Recall / Precisión + Recall  
> Textos del gráfico: F1 · = · 2 · Precisión · Recall · Precisión + Recall

---

## 34. Curva ROC (Receiver Operating Characteristic)

_4 · Evaluación: matriz de confusión y curva ROC_

Representación gráfica de la **sensibilidad** frente a la **especificidad** para un clasificador binario, a distintos umbrales de decisión.

> **Gráfico:** Curva ROC: sensibilidad vs. 1-especificidad, con el área bajo la curva (AUC)  
> Textos del gráfico: 0.0 · 0.2 · 0.4 · 0.6 · 0.8 · 1.0 · 1 − Especificidad (FPR) · Sensibilidad (TPR) · clasificador aleatorio

---

## 35. AUC: Área bajo la curva

_4 · Evaluación: matriz de confusión y curva ROC_

Entre más cercana a 1, mejor distingue el modelo entre clases positivas y negativas — una curva más arqueada hacia la esquina superior izquierda es mejor.

> **Gráfico:** Curvas ROC de distinta calidad: excelente, bueno, regular y malo, frente al clasificador aleatorio  
> Textos del gráfico: 1 − Especificidad (FPR) · Sensibilidad (TPR) · aleatorio (0,5) · Excelente (0,95) · Bueno (0,82) · Regular (0,68) · Malo (0,55)

- **0,5** **Test aleatorio**
- **0,5–0,6** **Test malo**
- **0,6–0,75** **Test regular**
- **0,75–0,9** **Test bueno**
- **0,9–0,97** **Test muy bueno**
- **0,97–1** **Test excelente**

---

## 36. Funciones de valor residual (Regresión)

_4 · Evaluación: residuales_

El **residual** es la diferencia entre el valor predicho (o score) y el valor real: mientras más pequeño, mejor el ajuste.

> **Gráfico:** Residuales en una regresión: y-intercept, punto (x1, y1) y residual y2 − ŷ2  
> Textos del gráfico: y (dependiente) · x (independiente) · línea: y = a + bx · y-intercept · y1 · x1 · ŷ2 · y2 · y2 − ŷ2 · Minimizar: · Σ (yᵢ − ŷᵢ)² · Método de mínimos · cuadrados

---

## 37. Funciones de error residual

_4 · Evaluación: residuales_

Distintas formas de resumir todos los residuales de un modelo en un único número.

**MSE**

Error medio cuadrado — penaliza fuerte los errores grandes.

> **Gráfico:** Fórmula de MSE  
> Textos del gráfico: MSE · = · 1 · N · · · N · Σ · i=1 · (f(xᵢ) − yᵢ)²

**RMSE**

Raíz del MSE — vuelve a las unidades originales de la variable.

> **Gráfico:** Fórmula de RMSE  
> Textos del gráfico: RMSE · = · 1 · N · · · N · Σ · i=1 · (f(xᵢ) − yᵢ)²

**MAE**

Error absoluto promedio — más robusto ante valores atípicos.

> **Gráfico:** Fórmula de MAE  
> Textos del gráfico: MAE · = · 1 · N · · · N · Σ · i=1 · |f(xᵢ) − yᵢ|

**Median AE**

Mediana del error absoluto — casi insensible a atípicos extremos.

> **Gráfico:** Fórmula de Median Absolute Error  
> Textos del gráfico: MedianAE · = · Mediana · ( · | · f(xᵢ) − yᵢ · | · )

---

## 38. Funciones de valor residual: Ejemplo

_4 · Evaluación: residuales_

Ejemplo de los valores de un modelo de regresión con **muy buen desempeño**: valores bajos en las 4 métricas — nótese que RMSE (misma unidad que la variable) es siempre mayor o igual que MAE.

| Métrica | Valor |
| --- | --- |
| Mean Square Error (MSE) | 0,9553 |
| Root Mean Square Error (RMSE) | 0,9774 |
| Mean Absolute Error (MAE) | 0,7747 |
| Median Absolute Error | 0,6252 |

---

## 39. Coeficiente de determinación (R²)

_4 · Evaluación: residuales_

**¿Cómo interpretarlo?**

Entre más cerca estén los puntos de la recta, **mayor el R²** y mejor el ajuste del modelo — mide qué porcentaje de la variación de la variable de respuesta es explicado por el modelo.

> **Gráfico:** Comparación entre un modelo de regresión con R² bajo y uno con R² alto, con el valor de R² calculado en cada uno  
> Textos del gráfico: 0 · 10 · 20 · 30 · 40 · 50 · 0 · 1 · 2 · 3 · 4 · 5 · 6 · R² ≈ 0.49 · R² bajo · 0 · 10 · 20 · 30 · 40 · 50 · 0 · 1 · 2 · 3 · 4 · 5 · 6 · R² ≈ 0.94 · R² alto

- **R²=1** **El modelo se ajusta perfectamente a los datos.**
- **R²=0** **El modelo no redujo la suma de cuadrados de las etiquetas — es un modelo inútil.**

---

## 40. ¿Preguntas?

_Analítica de datos · Universidad de Antioquia_

Modelado supervisado Preparación de datos Sobreajuste y regularización Evaluación de modelos

Continúa en: Técnicas de modelado (2/2)

UNIVERSIDAD DE ANTIOQUIA JORGE BEDOYA

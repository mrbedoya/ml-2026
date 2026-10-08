# Métodos supervisados: Técnicas (2/2) · fiel al PDF

> Versión Markdown generada a partir de `00_5b_Tecnicas.html` · 58 diapositivas. Los gráficos se describen por su texto; las fórmulas están en LaTeX (`$...$`).

---

## 1. Técnicas de modelado supervisado

_Analítica de datos · Universidad de Antioquia_

Segunda parte: regresión, clasificadores bayesianos, k-NN, SVM, árboles de decisión y los métodos de ensamble (Random Forest, AdaBoost, Gradient Boosting).

Aprendizaje Automático I Continúa de Métodos supervisados (1/2)

UNIVERSIDAD DE ANTIOQUIA JORGE BEDOYA

---

## 2. Temas a tratar

_Contenido_

Cada técnica resuelve problemas de: Regresión *predice un valor numérico continuo* Clasificación *predice una categoría o clase*

01

Regresión lineal

Relación lineal entre variables para predecir un valor continuo.

Regresión

02

Regresión logística

Probabilidad de pertenecer a una clase mediante la curva sigmoide.

Clasificación

03

Clasificador Bayesiano

Probabilidades condicionadas a partir del teorema de Bayes.

Clasificación

04

k-NN

Decide según la clase de los k vecinos más cercanos.

Clasificación

05

Máquinas de soporte vectorial

Hiperplano de máximo margen y funciones del núcleo (kernel).

Regresión Clasificación

06

Árboles de decisión y Random Forest

Particiones sucesivas y ensamble de muchos árboles (bagging).

Regresión Clasificación

07

AdaBoost

Combina clasificadores débiles ponderados según sus errores.

Regresión Clasificación

08

Gradient Boosting

Modelos secuenciales que ajustan los residuos de los anteriores.

Regresión Clasificación

---

## 3. Regresión lineal

_5 · Técnicas: regresión lineal_

_Aplica a: Regresión_

Técnica **paramétrica**: asume una correlación lineal entre la variable de respuesta y la(s) variable(s) explicativa(s). Rápida y requiere pocos recursos. Se busca: **1.** expresar su relación lineal y **2.** estimar los parámetros del modelo por medio del ajuste.

> **Gráfico:** Número de helados vendidos según la temperatura, con la recta de mínimos cuadrados  
> Textos del gráfico: Número de helados vendidos · 200 · 300 · 400 · 500 · 600 · 12 · 14 · 16 · 18 · 20 · 22 · 24 · Temperatura (°C) · Unidades vendidas · observación · mínimos cuadrados lineales

$Y_{t}= \beta_{0}+ \beta_{1}X_{1}+ \beta_{2}X_{2}+ \cdots + \beta_{p}X_{p}+ \varepsilon$

- **Yₜ** **Variable dependiente.**
- **X₁ … Xₚ** **Variables explicativas.**
- **β₀ … βₚ** **Parámetros: miden la influencia que las variables explicativas tienen sobre el regresando.**
- **ε** **Perturbación aleatoria.**

Referencias: <https://www.r-bloggers.com/generalised-linear-models-in-r/>

---

## 4. Regresión lineal simple

_5 · Técnicas: regresión lineal_

_Aplica a: Regresión_

Técnica estadística para predecir los valores de una variable **continua dependiente** con base en los valores de **una** variable independiente.

> **Gráfico:** Regresión lineal simple: recta ajustada y errores verticales de cada observación  
> Textos del gráfico: Ventas según la inversión en publicidad en TV · 5 · 10 · 15 · 20 · 25 · 0 · 100 · 200 · 300 · TV (inversión en publicidad) · Ventas · error eᵢ = yᵢ − ŷᵢ · recta de regresión (ŷ) · errores a minimizar

- **Paramétrico** Su forma queda definida por pocos parámetros: el intercepto β₀ y la pendiente β₁.
- **Correlación lineal** Asume una relación lineal entre la variable de respuesta (ventas) y la variable explicativa (TV).
- **Rápido y liviano** Requiere pocos recursos de cómputo.

**Mínimos cuadrados**

Se deben **minimizar los errores** entre todos los puntos y la recta, representados por la suma de los cuadrados de error.

$ŷ = \beta_{0}+ \beta_{1}x$ · $\text{SSE}= \sum_{i=1}^{n}(y_{i}- ŷ_{i})^{2}$

---

## 5. Regresión lineal múltiple

_5 · Técnicas: regresión lineal_

_Aplica a: Regresión_

Utiliza **varias variables explicativas a la vez** para predecir la variable de respuesta. Con dos variables, la recta se convierte en un **plano**; con más, en un hiperplano.

$ŷ = \beta_{0}+ \beta_{1}x_{1}+ \beta_{2}x_{2}+ \cdots + \beta_{p}x_{p}$

> **Gráfico:** Regresión lineal múltiple: plano de regresión que predice el consumo (MPG) a partir del peso y la potencia  
> Textos del gráfico: Consumo (MPG) según el peso y la potencia del vehículo · 2000 · 3000 · 4000 · 5000 · 50 · 100 · 150 · 200 · 250 · 10 · 20 · 30 · 40 · Peso (lb) · Potencia (hp) · MPG · observaciones · plano de regresión (ajuste) · error (residual)

- **Relevancia de cada variable** Se recomienda hallar la relevancia de cada variable explicativa (coeficientes y valor‑p): no todas aportan al modelo.
- **Multicolinealidad** Variables muy correlacionadas entre sí distorsionan los coeficientes; conviene detectarlas (p. ej., con el VIF).

**Comprobar el coeficiente de determinación R²**

Mide qué parte de la variación explica el modelo. En regresión múltiple conviene el **R² ajustado**, que penaliza las variables que no aportan.

---

## 6. Coeficiente de determinación (R²)

_5 · Técnicas: regresión lineal_

_Aplica a: Regresión_

**¿Cómo interpretarlo?**

Corresponde al porcentaje de variación de la variable de respuesta explicado por la(s) variable(s) explicativa(s); varía entre 0 y 1. Entre más cerca estén los puntos de la recta, **mayor el R²** y mejor el ajuste del modelo.

> **Gráfico:** Comparación entre un modelo de regresión con R² bajo y uno con R² alto, con el valor de R² calculado en cada uno  
> Textos del gráfico: 0 · 10 · 20 · 30 · 40 · 50 · 0 · 1 · 2 · 3 · 4 · 5 · 6 · R² ≈ 0.49 · R² bajo · 0 · 10 · 20 · 30 · 40 · 50 · 0 · 1 · 2 · 3 · 4 · 5 · 6 · R² ≈ 0.94 · R² alto

> **Gráfico:** Coeficiente de determinación R² = 0.87  
> Textos del gráfico: 0 · 0,25 · 0,5 · 0,75 · 1 · R² = 0.87 · Modelo inútil (0) · Ajuste perfecto (1)

- **R²=1** **El modelo se ajusta perfectamente a los datos.**
- **R²=0** **El modelo no redujo la suma de cuadrados de las etiquetas — es un modelo inútil.**

---

## 7. Regresión logística

_5 · Técnicas: regresión logística_

_Aplica a: Clasificación_

Variación de la regresión que se usa para **clasificación binaria**: estima una **probabilidad entre 0 y 1** y, según de qué lado de la frontera cae la instancia, la asigna a una de las dos clases.

> **Gráfico:** Regresión logística: muestras verdaderas y falsas separadas por una frontera con forma de curva sigmoide  
> Textos del gráfico: Ejemplo de regresión logística · 0 · 0,2 · 0,4 · 0,6 · 0,8 · 1 · x · y · Clase 1 · verdaderos · Clase 0 · falsos · Frontera (sigmoide)

- **Clasificación binaria** Predice entre dos clases (0 y 1) usando la función logit.
- **Una recta no sirve** No es práctico usar una línea recta para estimar probabilidades: se sale del rango 0–1.
- **Probabilidad, no valor** Establece la probabilidad de que la instancia pertenezca a la clase objetivo; **no** es el valor de la variable de respuesta, como en la regresión lineal.

**Función logit**

$Y_{t}= \ln \left(\frac{p}{1 - p}\right)$

---

## 8. De la recta a la probabilidad

_5 · Técnicas: regresión logística_

_Aplica a: Clasificación_

¿Cuál es la probabilidad de éxito cuando el valor de la variable predictora es *x*? Se parte de una recta y se transforma con el logit para mantener el resultado entre 0 y 1.

> **Gráfico:** La regresión logística mantiene P(y) entre 0 y 1; la recta de la regresión lineal puede salirse de ese rango  
> Textos del gráfico: Regresión logística vs. regresión lineal · fuera de 0–1 · 0 · 0,2 · 0,4 · 0,6 · 0,8 · 1 · 0 · 1 · 2 · 3 · 4 · x · P(y) · regresión logística · regresión lineal

- *1* $Y_{t}= \beta_{0}+ \beta_{1}X$ Se modela una recta
- *2* $Y_{t}= \ln \left(\frac{p}{1 - p}\right)$ Se define con el logit (log-odds)
- *3* $\ln \left(\frac{p}{1 - p}\right) = \beta_{0}+ \beta_{1}X$ Se igualan ambas expresiones
- *4* $p = \frac{e^{\beta_{0}+ \beta_{1}X}}{1 + e^{\beta_{0}+ \beta_{1}X}}$ Se despeja p — la función sigmoide

| Probabilidad | Log-odds |
| --- | --- |
| 0,5 | 0,0 |
| > 0,5 | > 0,0 |
| < 0,5 | < 0,0 |

Referencias: <https://www.r-bloggers.com/generalised-linear-models-in-r/>

---

## 9. Clasificador Bayesiano: ejemplo

_5 · Técnicas: clasificador Bayesiano_

_Aplica a: Clasificación_

Las máquinas A, B y C fabrican piezas con **1 %, 2 % y 3 %** de defectos. Se mezclan 300 piezas (100 de cada una) y se elige una al azar, que resulta **defectuosa**. ¿Cuál es la probabilidad de que haya sido fabricada en la **máquina A**?

> **Gráfico:** Árbol de probabilidades: tres máquinas, cada una con su proporción de piezas defectuosas  
> Textos del gráfico: Árbol de probabilidades · ¿Qué máquina? · ¿Defectuosa? · P(máquina ∩ defecto) · 1/3 · A · defectuosa 1/100 · buena 99/100 · $\frac{1}{3}\cdot \frac{1}{100}= \frac{1}{300}$ · 1/3 · B · defectuosa 2/100 · buena 98/100 · $\frac{1}{3}\cdot \frac{2}{100}= \frac{2}{300}$ · 1/3 · C · defectuosa 3/100 · buena 97/100 · $\frac{1}{3}\cdot \frac{3}{100}= \frac{3}{300}$ · $P(\text{defecto}) = \frac{6}{300}= 2 \%$

- *1* $P(A) = P(B) = P(C) = \frac{100}{300}= \frac{1}{3}$ A priori: cada máquina aporta igual cantidad de piezas
- *2* $P(D|A) = \frac{1}{100}\cdot P(D|B) = \frac{2}{100}\cdot P(D|C) = \frac{3}{100}$ Verosimilitud: porcentaje de defectos de cada máquina
- *3* $P(D) = \frac{1}{3}\cdot \frac{1}{100}+ \frac{1}{3}\cdot \frac{2}{100}+ \frac{1}{3}\cdot \frac{3}{100}= \frac{6}{300}$ Evidencia: probabilidad total de que una pieza sea defectuosa
- *4* $P(A|D) = \frac{\frac{1}{100}\cdot \frac{1}{3}}{\frac{6}{300}}= \frac{1}{6}$ Teorema de Bayes: se divide la rama de A entre el total

**Resultado**

$P(A | \text{defectuosa}) = \frac{1}{6}\approx 0,1667 = 16,67 \%$

Con el mismo cálculo: $B = \frac{2}{6}\approx 33,3 \% \cdot C = \frac{3}{6}= 50 \%$

Referencias: <https://medium.com/@javierdiazarca/teorema-de-bayes-ejercicios-bases-de-la-ia-678d62ec32f2>

---

## 10. Teorema de Bayes

_5 · Técnicas: clasificador Bayesiano_

_Aplica a: Clasificación_

Vincula la probabilidad del suceso A dado B con la probabilidad del suceso B dado A: permite **seleccionar una clase a partir de probabilidades condicionadas**.

> **Gráfico:** Teorema de Bayes: posterior = verosimilitud por a priori, dividido por la evidencia  
> Textos del gráfico: P(Aᵢ | B) · = · P(B | Aᵢ) · · · P(Aᵢ) · P(B) · Posterior · lo que se busca · Verosimilitud · P(dato | clase) · A priori · P(clase) · Evidencia · P(dato) · normaliza

- **Se basa en probabilidades** Combina lo que ya se sabía (a priori) con lo observado (verosimilitud).
- **Características independientes** Tiene en cuenta características que parecen insignificantes, asumiéndolas independientes entre sí (supuesto “naive”).
- **Selecciona las mejores instancias** Elige la clase con mayor probabilidad posterior.
- **Poca información de errores** Aporta poca información sobre falsos positivos y negativos.
- **Eficiente y rápido** Modelos livianos: entrenan y predicen casi al instante.
- **Caso Monty Hall** Ejemplo clásico donde el teorema corrige la intuición.

Referencias: <https://estadisticaparatodos.es/taller/montyhall/montyhall.html>

---

## 11. Variantes del clasificador Bayesiano

_5 · Técnicas: clasificador Bayesiano_

_Aplica a: Clasificación_

**Multinomial**

> **Gráfico:** Naive Bayes multinomial: frecuencia de cada palabra en correos normales y spam  
> Textos del gráfico: P(palabra | clase) · Dear · Friend · Lunch · Money · normal · spam

Características que describen **frecuencias discretas**, por ejemplo contar palabras.

★ Útil en clasificación de texto y detección de spam.

**Gaussian**

> **Gráfico:** Naive Bayes gaussiano: una curva normal por clase para cada característica continua  
> Textos del gráfico: densidad de cada clase · μ₁, σ₁ · μ₂, σ₂ · característica continua (xᵢ)

Predicciones sobre características **normalmente distribuidas** (continuas): una curva normal por clase.

★ Útil con variables continuas como peso o ingresos.

**Bernoulli**

> **Gráfico:** Naive Bayes de Bernoulli: probabilidad de que cada característica binaria esté presente según la clase  
> Textos del gráfico: P(xᵢ = 1 | clase) · 0 · 0.5 · 1 · "oferta" · adjunto · enlace · características binarias: presente (1) o ausente (0)

Predicciones para **características binarias**: variables categóricas binarias o convertibles a binarias con un umbral.

★ Útil cuando importa si algo está presente o no.

---

## 12. Naive Bayes Multinomial

_5 · Técnicas: clasificador Bayesiano_

_Aplica a: Clasificación_

Adecuado cuando las características son **conteos** o frecuencias: el ejemplo clásico es clasificar texto (¿correo normal o spam?) a partir de **cuántas veces aparece cada palabra**.

> **Gráfico:** Conteo de palabras (Dear, Friend, Lunch, Money) en correos normales y en spam  
> Textos del gráfico: Normal (N) · 8 correos · p(Normal) = 0,67 · 8 · Dear · 5 · Friend · 3 · Lunch · 1 · Money · Spam (S) · 4 correos · p(Spam) = 0,33 · 2 · Dear · 1 · Friend · 0 · Lunch · 4 · Money

| Palabra | P(palabra \| Normal) | P(palabra \| Spam) |
| --- | --- | --- |
| Dear | 9/21 = 0,43 | 3/11 = 0,27 |
| Friend | 6/21 = 0,29 | 2/11 = 0,18 |
| Lunch | 4/21 = 0,19 | 1/11 = 0,09 |
| Money | 2/21 = 0,10 | 5/11 = 0,45 |

**Suavizado de Laplace:** se suma 1 a cada conteo para que una palabra ausente (Lunch en spam = 0) no anule todo el producto.

- *1* $N = 0,67 \cdot 0,19 \cdot 0,10^{4}\approx 0,00001$ Nuevo correo «Lunch Money Money Money Money» como Normal
- *2* $S = 0,33 \cdot 0,09 \cdot 0,45^{4}\approx 0,00122$ El mismo correo como Spam

**0,00122 > 0,00001 → se clasifica como Spam**

Referencias: <https://www.youtube.com/watch?v=O2L2Uv9pdDA>

---

## 13. Naive Bayes Gaussian

_5 · Técnicas: clasificador Bayesiano_

_Aplica a: Clasificación_

Asume que cada característica, dentro de cada clase, sigue una **distribución normal** — útil para variables continuas. Se ajusta una campana (μ, σ) por clase y por característica. Ejemplo: ¿le gustó la película *Troll 2* a quien consume cierta cantidad de popcorn, soda y dulces?

> **Gráfico:** Naive Bayes gaussiano: para cada característica, una curva normal por clase  
> Textos del gráfico: Popcorn (g) · 0 · 10 · 20 · 30 · 40 · Soda Pop (ml) · 0 · 200 · 400 · 600 · 800 · Candy (g) · 0 · 30 · 60 · 90 · 120

| μ; σ | Popcorn (g) | Soda (ml) | Dulces (g) |
| --- | --- | --- | --- |
| ● Le gustó | 26; 7 | 640; 110 | 12; 7 |
| ● No le gustó | 5; 2,5 | 150; 70 | 95; 35 |

$f(x | \mu, \sigma) = \frac{1}{\sigma \sqrt{2\pi}}\cdot e^{-\frac{(x - \mu)^{2}}{2\sigma^{2}}}$

- *1* Nuevo: Popcorn 15 g · Soda 350 ml · Dulces 40 g Se evalúa cada valor en la campana de cada clase
- *2* $\text{Sí}= 0,5 \cdot 1,66\cdot 10^{-2}\cdot 1,12\cdot 10^{-4}\cdot 1,91\cdot 10^{-5}= 1,78\cdot 10^{-11}$ A priori × producto de las tres densidades (le gustó)
- *3* $\text{No}= 0,5 \cdot 5,35\cdot 10^{-5}\cdot 9,62\cdot 10^{-5}\cdot 3,32\cdot 10^{-3}= 8,54\cdot 10^{-12}$ Lo mismo con la clase «No le gustó»

**Se predice «Le gustó» (≈ 67,6 %)** — la clase de mayor valor.

Referencias: <https://www.youtube.com/watch?v=H3EjCKtlVog>

---

## 14. Naive Bayes Bernoulli

_5 · Técnicas: clasificador Bayesiano_

_Aplica a: Clasificación_

Adecuado para **características binarias** (presente / ausente, sí / no) o variables que se convierten a binarias con un **umbral**. Importa si algo ocurre, no cuántas veces: por ejemplo, si un correo contiene o no ciertas características.

> **Gráfico:** Naive Bayes de Bernoulli: probabilidad de que cada característica binaria esté presente en un correo normal y en uno spam  
> Textos del gráfico: P(característica presente | clase) · 0 · 0,25 · 0,5 · 0,75 · 1 · 0,12 · 0,8 · Contiene “oferta” · 0,3 · 0,55 · Trae adjunto · 0,2 · 0,75 · Contiene enlace · Normal · Spam

| Característica | P(sí \| Normal) | P(sí \| Spam) |
| --- | --- | --- |
| Contiene «oferta» | 0,12 | 0,80 |
| Trae adjunto | 0,30 | 0,55 |
| Contiene enlace | 0,20 | 0,75 |

**Nuevo correo:** con «oferta», **sin** adjunto y con enlace. Cada característica aporta P(sí) si está presente o **1 − P(sí)** si está ausente. A priori: Normal 0,6 · Spam 0,4.

- *1* $N = 0,6 \cdot 0,12 \cdot (1 - 0,30) \cdot 0,20 = 0,01008$ Verosimilitud como correo Normal
- *2* $S = 0,4 \cdot 0,80 \cdot (1 - 0,55) \cdot 0,75 = 0,10800$ Verosimilitud como correo Spam

**$P(\text{Spam}) = \frac{0,108}{0,108 + 0,01008}\approx 91,5 \% \to \text{Spam}$**

---

## 15. k-NN (k-Nearest Neighbour)

_5 · Técnicas: k-NN_

_Aplica a: Clasificación_

Se basa en la intuición de que **datos similares tendrán clases similares**. ¿Cómo se mide la similitud? Con una **distancia** (la inversa de la similitud).

> **Gráfico:** Medidas de distancia de k-NN: euclídea, Manhattan, Chebychev y coseno para valores continuos; por diferencia, de edición y específicas para valores discretos  
> Textos del gráfico: DISTANCIA · inversa · SIMILITUD · VALORES CONTINUOS · conviene normalizar entre 0 y 1 antes (salvo el coseno) · Euclídea · $d = \sqrt{\sum_{i=1}^{n}(x_{i}- y_{i})^{2}}$ · distancia en línea recta · Manhattan · $d = \sum_{i=1}^{n}|x_{i}- y_{i}|$ · suma de diferencias absolutas · Chebychev · $d = \max_{i}|x_{i}- y_{i}|$ · mayor diferencia en una variable · Del coseno · $d = 1 - \cos \theta$ · ángulo entre vectores · no requiere normalizar · VALORES DISCRETOS · Por diferencia · $D = 0 \text{si}x = y; \text{si}\text{no}, D = 1$ · coincide o no coincide · De edición · texto y secuencias · Específicas · razonamiento basado en casos

- **Basado en instancias** Compara cada caso nuevo con los ejemplos guardados.
- **No paramétrico** No asume una forma concreta de la relación entre variables.
- **Lazy learning** No construye un modelo previo: calcula todo al predecir.
- **Depende de la distancia** Con valores continuos conviene normalizar entre 0 y 1.
- **Costoso al predecir** Compara contra todos los datos de entrenamiento.

---

## 16. k-NN: procedimiento y elección de k

_5 · Técnicas: k-NN_

_Aplica a: Clasificación_

> **Gráfico:** k-NN con k=5: de los vecinos más cercanos, 3 son de la categoría 1 y 2 de la categoría 2  
> Textos del gráfico: X₁ · X₂ · Nuevo punto · Categoría 1 · Categoría 2 · k = 5 vecinos · Categoría 1: 3 vecinos · Categoría 2: 2 vecinos

- *1* Se buscan los k casos más cercanos Se mide la distancia del nuevo punto a todos los de entrenamiento
- *2* Votación entre los k vecinos Se asigna la clase con más elementos (o la de menor distancia media)

Con k = 5: 3 vecinos de Categoría 1 y 2 de Categoría 2 → **Categoría 1**

Heurística habitual para el valor de k, con *n* ejemplos:

$k = \sqrt{n}$

- **k pequeño** Frontera irregular, sensible al ruido (sobreajuste).
- **k grande** Frontera suave, pero puede ignorar patrones locales.

Referencias: <http://www.aionlinecourse.com/tutorial/machine-learning/k-nearest-neighbor>

---

## 17. Máquinas de soporte vectorial (SVM)

_5 · Técnicas: máquinas de soporte vectorial_

_Aplica a: Regresión, Clasificación_

Buscan un **hiperplano** que separe lo mejor posible las clases. Son versátiles: sirven tanto para clasificación como para regresión. Pero entre todos los hiperplanos posibles… ¿cuál elegir?

> **Gráfico:** Cinco hiperplanos distintos que separan perfectamente las dos clases  
> Textos del gráfico: 5 posibles hiperplanos de separación · 0 · 1 · 2 · 3 · 4 · 5 · 2 · 3 · 4 · 5 · X₁ · X₂

> **Gráfico:** El hiperplano separador es un punto en una dimensión, una recta en dos y un plano en tres  
> Textos del gráfico: R¹ · hiperplano = punto · R² · hiperplano = recta · R³ · hiperplano = plano

- **Hiperplano** Subespacio con una dimensión menos que el espacio de los datos: punto en R¹, recta en R² y plano en R³.
- **Infinitas soluciones** Si las clases son separables, existen muchos hiperplanos que las dividen sin error.

Referencias: <https://rpubs.com/Joaquin_AR/267926> · <https://www.codificandobits.com/blog/maquinas-de-soporte-vectorial/>

---

## 18. Hiperplano óptimo y margen máximo

_5 · Técnicas: máquinas de soporte vectorial_

_Aplica a: Regresión, Clasificación_

El hiperplano óptimo es el que queda **más alejado** de todas las observaciones de entrenamiento: así generaliza mejor con datos nuevos.

> **Gráfico:** Hiperplano óptimo con margen máximo, y los vectores de soporte sobre los bordes del margen  
> Textos del gráfico: Hiperplano óptimo · Margen máximo (M) · Vectores de soporte

- *1* Distancia perpendicular Se mide de cada observación al hiperplano
- *2* Margen = la menor de esas distancias Es la «franja» libre de puntos a cada lado
- *3* Hiperplano óptimo = margen máximo Se elige el que hace más ancha esa franja

**Vectores de soporte**

Las observaciones sobre el borde del margen: son las **únicas** que definen el hiperplano; mover el resto no lo cambia.

Referencias: <https://rpubs.com/Joaquin_AR/267926>

---

## 19. Funciones del núcleo (kernel)

_5 · Técnicas: máquinas de soporte vectorial_

_Aplica a: Regresión, Clasificación_

Cuando las clases **no son separables con una línea recta**, la SVM puede usar distintas funciones del núcleo (kernel) para obtener una frontera curva.

> **Gráfico:** Tipos de núcleo de las SVM: lineal, polinomial de grado 2 y 3, de base radial y sigmoide  
> Textos del gráfico: Lineal · Polinomial (grado 2) · Polinomial (grado 3) · Función de base radial · Sigmoide

- **Lineal** Separación con una recta o hiperplano: el caso más simple.
- **Polinomial** Fronteras curvas según el grado (2, 3…).
- **RBF (Radial Basis Function)** Núcleos locales en forma de Gauss: separación no lineal flexible.
- **Sigmoide** Frontera con forma de S, parecida a una red neuronal.

---

## 20. El truco del kernel

_5 · Técnicas: máquinas de soporte vectorial_

_Aplica a: Regresión, Clasificación_

El truco del kernel proyecta los datos a un espacio de **mayor dimensión**, donde sí existe una separación lineal — **sin calcular explícitamente** esa proyección.

> **Gráfico:** Truco del kernel: los datos no separables se proyectan a un espacio donde un plano los separa, y la frontera vuelve como curva  
> Textos del gráfico: 1 · Datos originales · sin frontera lineal posible · kernel · 2 · Espacio proyectado · un plano separa las dos clases · Clase 1 · cima · Clase 2 · base · plano · volver · 3 · Frontera en el espacio original · curva no lineal

- **Se proyecta** Cada punto se lleva a un espacio con más dimensiones (por ejemplo de 2D a 3D).
- **Se separa con un plano** En ese espacio las clases ya se pueden dividir con un hiperplano.
- **Sin calcular la proyección** El kernel K(x, x′) da el producto interno directamente, ahorrando cómputo.

Referencias: <http://people.ciirc.cvut.cz/~hlavac/TeachPresEn/31PattRecog/35KernelMeth-and-SVM.pdf> · <https://www.youtube.com/watch?v=3lwicUTEgHs>

---

## 21. Efecto del parámetro sigma (RBF)

_5 · Técnicas: máquinas de soporte vectorial_

_Aplica a: Regresión, Clasificación_

El parámetro **sigma (σ)** controla qué tan «local» es cada núcleo gaussiano: σ pequeño genera fronteras muy ajustadas a los datos (riesgo de sobreajuste); σ grande, fronteras más suaves.

> **Gráfico:** Curvas gaussianas con σ = 0,5; 1; 2 y 3: el parámetro sigma controla qué tan local es el núcleo RBF  
> Textos del gráfico: Núcleo RBF: función de densidad gaussiana · 0 · 0,2 · 0,4 · 0,6 · 0,8 · -5 · -4 · -3 · -2 · -1 · 0 · 1 · 2 · 3 · 4 · 5 · σ = 0,5 · σ = 1 · σ = 2 · σ = 3 · σ pequeño = núcleo “local” (curva angosta) · σ grande = núcleo suave

$K(x, x') = e^{-\frac{\Vert x - x'\Vert^{2}}{2\sigma^{2}}}$

*[Imagen: Comparación de fronteras de decisión con sigma=5 y sigma=1]*

Referencias: <https://medium.com/@ashwanibhardwajcodevita16/from-zero-to-hero-in-depth-support-vector-machine-264931a1e135> · <https://wiki.eigenvector.com/index.php?title=Svmda>

---

## 22. SVM multiclase: One vs. All (One-vs-Rest)

_5 · Técnicas: máquinas de soporte vectorial_

_Aplica a: Clasificación_

Una SVM es un clasificador **binario**. Cuando hay **más de dos clases**, el problema se divide en varios problemas binarios. En **One vs. All** se entrena un clasificador por clase: esa clase contra todas las demás.

> **Gráfico:** One-vs-All: tres clasificadores binarios, cada uno separa una clase del resto  
> Textos del gráfico: Datos originales: 3 clases · x₁ · x₂ · Verde vs. resto · Azul vs. resto · Rojo vs. resto

- **N clases → N clasificadores** Con 3 clases (Verde, Azul y Rojo) se entrenan 3 modelos binarios.
- **Una clase contra el resto** Cada modelo trata una clase como positiva (+1) y todas las demás juntas como negativa (−1).
- **Todos los datos en cada modelo** Cada clasificador se entrena con el conjunto completo, solo que con etiquetas distintas.

---

## 23. One vs. All: entrenamiento y predicción

_5 · Técnicas: máquinas de soporte vectorial_

_Aplica a: Clasificación_

A partir del conjunto original se crean **tres conjuntos de entrenamiento**, uno por clase: la clase objetivo recibe **+1** y el resto **−1**.

| Características | Clase | Dataset 1 Verde | Dataset 2 Azul | Dataset 3 Rojo |
| --- | --- | --- | --- | --- |
| x1, x2, x3 | Verde | **+1** | −1 | −1 |
| x4, x5, x6 | Azul | −1 | **+1** | −1 |
| x7, x8, x9 | Rojo | −1 | −1 | **+1** |
| x10, x11, x12 | Verde | **+1** | −1 | −1 |
| x13, x14, x15 | Azul | −1 | **+1** | −1 |
| x16, x17, x18 | Rojo | −1 | −1 | **+1** |

**Predicción** de un dato de prueba con los tres clasificadores:

- *V* Verde → **Positivo** · puntuación 0,9
- *A* Azul → **Positivo** · puntuación 0,4
- *R* Rojo → **Negativo** · puntuación 0,5

Según las respuestas positivas y la mayor puntuación, el dato pertenece a la clase **Verde**.

---

## 24. SVM multiclase: One vs. One (OvO)

_5 · Técnicas: máquinas de soporte vectorial_

_Aplica a: Clasificación_

En **One vs. One** se entrena un clasificador binario por **cada pareja de clases**; cada uno solo ve los datos de esas dos clases.

> **Gráfico:** One-vs-One: tres clasificadores binarios, uno por cada pareja de clases  
> Textos del gráfico: Datos originales: 3 clases · x₁ · x₂ · 1 · Verde vs. Azul · 2 · Verde vs. Rojo · 3 · Azul vs. Rojo

$\frac{N \cdot (N - 1)}{2}= 3$ clasificadores

para N = 3 clases

- *1* Clasificador 1: Verde vs. Azul
- *2* Clasificador 2: Verde vs. Rojo
- *3* Clasificador 3: Azul vs. Rojo

**Predicción:** el dato de prueba pasa por los tres clasificadores y se elige la clase con **mayoría de votos**.

- **One vs. All** N modelos, cada uno con todos los datos.
- **One vs. One** N(N−1)/2 modelos, cada uno con solo dos clases.

---

## 25. Árboles de decisión

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

Un árbol de decisión divide los datos con una secuencia de **pruebas sencillas** sobre las variables (categóricas o numéricas); cada prueba parte el espacio en regiones, y cada región termina en una **hoja** con su clase.

> **Gráfico:** Un árbol de decisión y la partición del espacio que produce con tres pruebas  
> Textos del gráfico: Árbol de decisión · Partición del espacio de características · Sí · No · Sí · No · Sí · No · ≤ x₀ · ≤ y₂ · ≤ y₁ · Nodos de decisión (prueba) y hojas (clase) · x₀ · y₂ · y₁ · Variable X →

- *1* Elegir la mejor variable La que mejor divide los ejemplos según el valor objetivo
- *2* Dividir en dos ramas Cada prueba separa los datos en «Sí» y «No»
- *3* Repetir recursivamente Hasta cumplir los criterios de parada
- **Variables mixtas** Admite valores categóricos y numéricos en los nodos de decisión.

Referencias: <https://bookdown.org/content/2031/arboles-de-decision-parte-i.html#conceptos-introductorios> · <https://www.youtube.com/watch?v=kqaLlte6P6o>

---

## 26. Árboles de decisión: criterios de parada

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

**Ejemplo:** ¿aprobar un crédito? El árbol usa tres variables del cliente: mora previa, ingresos y relación deuda/ingreso. Cada hoja muestra la probabilidad de que el cliente pague y el porcentaje de solicitudes que cae en ella.

> **Gráfico:** Árbol de decisión de aprobación de crédito: mora previa, ingresos y deuda/ingreso, con los criterios de parada señalados  
> Textos del gráfico: Sí · No · Sí · No · Sí · No · ¿Tuvo mora previa? · ¿Ingresos > $2 M? · ¿Deuda/ingreso > 40 %? · Aprobar · 0,91 · 48 % · Aprobar · 0,64 · 20 % · Rechazar · 0,12 · 18 % · Aprobar · 0,55 · 14 % · profundidad máxima: 3 niveles · 1 · 2 · 3 · Ejemplo de recorrido · Cliente con mora previa, ingresos · de $1,5 M y deuda del 55 %: · 1. mora previa → Sí · 2. ingresos > $2 M → No · 3. deuda/ingreso > 40 % → Sí · → Rechazar (P pagar = 0,12) · 0,91 = P(pagar) · 48 % = solicitudes en la hoja

**El árbol deja de crecer cuando…**

- *1* Un grupo es casi puro Una hoja reúne casi solo la misma clase: el 48 % de las solicitudes, con 0,91 de probabilidad de pago.
- *2* Se agotaron las variables Ya se probaron las tres: mora, ingresos y deuda/ingreso.
- *3* Profundidad máxima Se alcanzó el límite de niveles de ramas (aquí, 3).

Referencias: <https://bookdown.org/content/2031/arboles-de-decision-parte-i.html#conceptos-introductorios>

---

## 27. Random Forest y los métodos ensemble

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

A continuación vamos a estudiar **Random Forest**. Pero antes ubiquémoslo dentro de la clasificación de los **métodos ensemble**.

> **Gráfico:** diagrama  
> Textos del gráfico: Nuevo · varios modelos · un solo modelo

**Métodos ensemble**

Combinan **múltiples modelos** en uno nuevo, buscando un equilibrio entre **sesgo** y **varianza** y logrando mejores predicciones que cualquiera de los modelos individuales originales.

→

- 1 **Bagging**
- 2 **Boosting**

Existen **dos** familias de métodos ensemble. En las siguientes diapositivas las comparamos y luego estudiamos Random Forest.

Referencias: <https://www.cienciadedatos.net/documentos/py08_random_forest_python.html>

---

## 28. Ensemble: clasificador único, Bagging y Boosting

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

Un clasificador único aprende una sola vez. **Bagging** entrena varios modelos **en paralelo**, cada uno con una muestra distinta; **Boosting** los entrena **en secuencia**, de modo que cada uno corrige los errores del anterior.

> **Gráfico:** Comparación entre un clasificador único, bagging en paralelo y boosting secuencial  
> Textos del gráfico: Clasificador único · Una sola iteración · Modelo · Bagging · En paralelo · Modelo · Boosting · Secuencial · Modelo

Referencias: <https://www.datacamp.com/tutorial/adaboost-classifier-python>

---

## 29. Bagging: Random Forest

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

En **bagging** se ajustan múltiples modelos **en paralelo**, cada uno con un subconjunto distinto de los datos de entrenamiento. Los modelos **Random Forest** pertenecen a esta categoría: el modelo base es un árbol de decisión.

> **Gráfico:** Bagging: muestras bootstrap, un árbol por muestra y agregación de las predicciones  
> Textos del gráfico: Datos · Muestras bootstrap · Árboles · Agregación · Conjunto de · entrenamiento · Muestra 1 · Árbol 1 · Muestra 2 · Árbol 2 · Muestra 3 · Árbol 3 · Predicción final · Regresión: · media de las predicciones · Clasificación: · clase más frecuente · Cada árbol se entrena con una muestra distinta y todos participan en la predicción

- **Muchos árboles** Cada árbol se ajusta con una muestra distinta de los datos.
- **Todos participan** Para predecir, cada árbol del agregado aporta su predicción.
- **Media o voto** Regresión: media de las predicciones. Clasificación: clase más frecuente.

Referencias: <https://www.cienciadedatos.net/documentos/py08_random_forest_python.html>

---

## 30. Boosting

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

En **boosting** se ajustan **secuencialmente** múltiples modelos sencillos (*weak learners*): cada modelo aprende de los **errores** del anterior.

> **Gráfico:** Boosting: tres modelos débiles entrenados en secuencia, cada uno con más peso en los errores del anterior, combinados al final  
> Textos del gráfico: Modelo débil 1 · todos los datos pesan igual · errores · Modelo débil 2 · más peso a los errores previos · errores · Modelo débil 3 · más peso a los errores previos · = mal clasificado · Modelo final = suma ponderada · de todos los modelos débiles

- **En secuencia** Cada modelo se entrena después del anterior y se concentra en los casos que este falló.
- **Valor final** Igual que en bagging: media de las predicciones o clase más frecuente (ponderadas).

**Los más empleados**

AdaBoost Gradient Boosting Stochastic GB

Referencias: <https://www.cienciadedatos.net/documentos/py08_random_forest_python.html> · <https://www.datacamp.com/tutorial/adaboost-classifier-python>

---

## 31. Random Forest · 1. Bootstrap

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

**Bootstrap** es un método de remuestreo: se obtienen muestras aleatorias **con reemplazamiento** (un mismo dato puede incluirse varias veces), de **igual tamaño N** que el conjunto de datos original.

> **Gráfico:** Bootstrap: de un conjunto original de cuatro filas se obtiene una muestra del mismo tamaño con la fila 4 repetida y la fila 3 fuera  
> Textos del gráfico: Conjunto original · Muestra bootstrap · Dolor de · pecho · Buena · circ. · Arterias · bloq. · Peso · Enfermedad · cardíaca · 1 · No · 125 · No · 2 · Sí · 180 · Sí · 3 · Sí · No · 210 · No · 4 · Sí · No · Sí · 167 · Sí · Dolor de · pecho · Buena · circ. · Arterias · bloq. · Peso · Enfermedad · cardíaca · 2 · Sí · 180 · Sí · 1 · No · 125 · No · 4 · Sí · No · Sí · 167 · Sí · 4 · Sí · No · Sí · 167 · Sí · La fila 3 no fue elegida: queda fuera de la muestra (OOB) · La fila 4 se repitió: el muestreo es con reemplazo

- **Con reemplazo** Cada fila elegida vuelve al conjunto: puede salir varias veces.
- **Mismo tamaño N** La muestra tiene tantas filas como el conjunto original.
- **Una muestra por árbol** Cada árbol del bosque se entrena con su propia muestra; en promedio entra ≈ 63 % de las filas distintas.

Referencias: <https://www.cienciadedatos.net/documentos/py08_random_forest_python.html>

---

## 32. Random Forest · 2. Selección aleatoria de variables

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

En **cada paso** de construcción del árbol no se consideran todas las variables: solo un subconjunto **elegido al azar** como candidatas. Así los árboles resultan distintos entre sí.

> **Gráfico:** Selección aleatoria de variables: en cada nodo solo se consideran dos variables candidatas elegidas al azar  
> Textos del gráfico: 1 · Nodo raíz · ??? · Dolor de pecho · Buena circulación · Arterias bloqueadas · Peso · Se eligen 2 variables al azar · como candidatas (no las 4) · 2 · Siguiente nodo · Buena circ. · ??? · Dolor de pecho · Buena circulación · (ya usada) · Arterias bloqueadas · Peso · Igual que en la raíz: 2 variables · al azar entre las 3 restantes

Referencias: <https://www.cienciadedatos.net/documentos/py08_random_forest_python.html>

---

## 33. Random Forest · 3. Se construyen tantos árboles como se consideren

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

Se repite el proceso (bootstrap + variables al azar) tantas veces como se quiera: el resultado es un **bosque de árboles distintos**.

> **Gráfico:** Seis árboles de un Random Forest, cada uno distinto porque usa su propia muestra y sus propias variables  
> Textos del gráfico: Árbol 1 · muestra 1 · variables al azar · Árbol 2 · muestra 2 · variables al azar · Árbol 3 · muestra 3 · variables al azar · Árbol 4 · muestra 4 · variables al azar · Árbol 5 · muestra 5 · variables al azar · Árbol 6 · muestra 6 · variables al azar

- **Su propia muestra** Cada árbol parte de una muestra bootstrap diferente.
- **Sus propias variables** En cada nodo se sortean las variables candidatas.
- **Más árboles, más estabilidad** El número de árboles es un hiperparámetro del modelo.

Referencias: <https://www.cienciadedatos.net/documentos/py08_random_forest_python.html>

---

## 34. Random Forest: ejemplo de predicción

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

Con los árboles ya construidos, un **nuevo paciente** se pasa por **cada árbol**: cada uno emite su voto y el bosque elige la clase con **mayoría de votos**.

> **Gráfico:** Un bosque de seis árboles vota la clase de un nuevo paciente: cuatro votan sí y dos votan no  
> Textos del gráfico: Árbol 1 · Voto: Sí · Árbol 2 · Voto: Sí · Árbol 3 · Voto: No · Árbol 4 · Voto: Sí · Árbol 5 · Voto: No · Árbol 6 · Voto: Sí · Votación · 4 votos «Sí» · 2 votos «No» · Predicción: Sí

**Nuevo paciente**

| Variable | Valor |
| --- | --- |
| Dolor de pecho | Sí |
| Buena circulación | No |
| Arterias bloqueadas | Sí |
| Peso | 167 |

- *1* Cada árbol recorre sus pruebas Cada uno usa solo sus propias variables y su propia muestra
- *2* 4 votos «Sí» · 2 votos «No» Se cuentan los votos de los seis árboles

Predicción: **tiene enfermedad cardíaca**

Referencias: <https://www.cienciadedatos.net/documentos/py08_random_forest_python.html>

---

## 35. Random Forest: out-of-bag (OOB)

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

Como el bootstrap se hace **con reemplazo**, en promedio cerca de un tercio (≈ 36,8 %) de las filas **queda por fuera** de la muestra de cada árbol. Esas filas son su conjunto **Out-Of-Bag (OOB)** y sirven para evaluar el modelo sin un conjunto de prueba aparte.

Conjunto original

| Fila | Dolor de pecho | Buena circ. | Arterias bloq. | Peso | Enfermedad |
| --- | --- | --- | --- | --- | --- |
| 1 | No | No | No | 125 | No |
| 2 | Sí | Sí | Sí | 180 | Sí |
| 3 | Sí | Sí | No | 210 | No |
| 4 | Sí | No | Sí | 167 | Sí |

Muestra bootstrap de un árbol (con reemplazo, mismo tamaño)

| Fila | Dolor de pecho | Buena circ. | Arterias bloq. | Peso | Enfermedad |
| --- | --- | --- | --- | --- | --- |
| 2 | Sí | Sí | Sí | 180 | Sí |
| 1 | No | No | No | 125 | No |
| 4 | Sí | No | Sí | 167 | Sí |
| 4 (repetida) | Sí | No | Sí | 167 | Sí |

- *1* La fila 3 no entró en la muestra Es una observación OOB de este árbol: Sí · Sí · No · 210 → real: **No**
- *2* Se evalúa con los árboles que no la usaron Árbol 1 → No · Árbol 2 → No · Árbol 3 → Sí
- *3* Voto mayoritario: «No» Coincide con el valor real → **acierto**

**Error OOB**

Se repite para todas las filas: el porcentaje de filas mal clasificadas estima el error del bosque.

Referencias: <https://fhernanb.github.io/libro_mod_pred/rand-forests.html>

---

## 36. Random Forest: resumen

_5 · Técnicas: árboles de decisión y Random Forest_

_Aplica a: Regresión, Clasificación_

**Random Forest** combina bootstrap, selección aleatoria de variables y muchos árboles para **reducir la varianza** de un único árbol de decisión.

1

**Bootstrap**

Una muestra con reemplazo para cada árbol

+

2

**Variables al azar**

Pocas candidatas en cada nodo

+

3

**Muchos árboles**

Tantos como se consideren

=

**Random Forest**

Media o voto mayoritario de todos los árboles

- **Menor varianza** Promediar muchos árboles reduce el riesgo de sobreajuste de un único árbol.
- **Robusto** Menos sensible a datos atípicos y al ruido que un árbol individual.
- **Evaluable con OOB** Las filas fuera de cada muestra permiten estimar el error sin un conjunto de validación aparte.

---

## 37. AdaBoost (Adaptive Boosting)

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

Combina clasificadores **«débiles»** mediante **ponderación**, donde cada uno aprende de los **errores del anterior**.

> **Gráfico:** AdaBoost: muchos stumps, con distinto peso, construidos en secuencia a partir de los errores del anterior  
> Textos del gráfico: 1 · AdaBoost combina muchos · «weak learners»; casi siempre · son stumps · 2 · Algunos stumps tienen · más peso en la · clasificación que otros · 3 · Cada stump se construye · considerando los errores · del stump anterior

- **Clasificadores débiles** Modelos muy simples, casi siempre árboles de profundidad 1.
- **Ponderación** Cada clasificador pesa distinto en la decisión final.
- **Aprende de los errores** Cada nuevo modelo corrige al anterior.

---

## 38. Clasificador débil (weak classifier)

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

El clasificador débil más común es el **Decision Stump**: un árbol de decisión binario de **profundidad 1**, es decir, una sola pregunta f(x) sobre una variable.

> **Gráfico:** Un decision stump: un umbral theta sobre una variable separa los datos en dos clases, menos uno y más uno  
> Textos del gráfico: Datos y umbral θ · Decision stump · predice −1 · predice +1 · θ separa el eje de la variable en dos partes · x · f(x) · < θ · ≥ θ · −1 · +1 · Árbol de profundidad 1: · una sola pregunta sobre una variable

Referencias: <https://www.coursera.org/lecture/deteccion-objetos/l5-4-adaboost-KMPxn>

---

## 39. Definición

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

> **Gráfico:** Tres clasificadores débiles: cada uno agranda los puntos que el anterior clasificó mal; juntos forman un clasificador fuerte  
> Textos del gráfico: Débil 1 · pesos iguales · falla en 3 puntos · + · Débil 2 · más peso a los errores del 1 · + · Débil 3 · más peso a los errores del 2 · = · Clasificador fuerte · todos bien clasificados · Cada clasificador simple da más peso (puntos grandes) a lo que el anterior clasificó mal (círculo amarillo)

- **1 · Débiles → fuerte** Combinación de clasificadores «débiles» en un clasificador global «fuerte».
- **2 · Pesos** Cada clasificador simple da un peso **mayor** a los casos mal clasificados previamente y un peso **menor** a los bien clasificados.

Referencias: <https://www.coursera.org/lecture/deteccion-objetos/l5-4-adaboost-KMPxn>

---

## 40. Algoritmo

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

> **Gráfico:** Los seis pasos del algoritmo AdaBoost con una ilustración por paso  
> Textos del gráfico: 1 · Entrenar un clasificador · 2 · Usar el clasificador · 3 · Identificar los casos · mal clasificados · 4 · Construir un nuevo · clasificador que mejore · esos casos · 5 · Repetir los pasos 2 a 4 · varias veces · ×T · 6 · Asignar un peso a cada · clasificador y · combinarlos · + · Clasificador fuerte

---

## 41. Fórmulas del algoritmo

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

El algoritmo sigue **seis pasos** que se repiten en cada ronda, hasta que el clasificador combinado sea suficientemente bueno.

> **Gráfico:** Diagrama de flujo de AdaBoost: inicializar pesos, calcular errores, elegir el mejor clasificador, calcular su poder de voto, agregarlo y actualizar los pesos  
> Textos del gráfico: 1 · Inicializar los pesos · de todos los puntos · $w = \frac{1}{N}$ · 2 · Calcular la tasa de error · de cada clasificador débil · $\varepsilon = \sum_{\text{mal}\text{clasificados}}^{}w_{i}$ · 3 · Elegir el clasificador · con el menor error · menor ε · 4 · Calcular su poder · de voto · $\alpha = \frac{1}{2}\log \frac{1 - \varepsilon}{\varepsilon}$ · 5 · Agregarlo al conjunto · ¿ya es suficientemente bueno? · $f(x) = \sum_{t=1}^{T}\alpha_{t}h_{t}(x)$ · 6 · Actualizar los pesos · de los puntos mal clasificados · w ↑ si falló · w ↓ si acertó · se repite

Referencias: <https://www.youtube.com/watch?v=9CPsYsB4OLI>

---

## 42. Ejemplo: los datos y los pesos iniciales

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

- *1* w = 1/N
- *2* ε = Σ w (mal clasificados)
- *3* Elegir el de menor error
- *4* α = (1/2)·log((1−ε)/ε)
- *5* f(x) = Σ αₜ·hₜ(x)
- *6* Actualizar los pesos w

> **Gráfico:** Cinco puntos A a E en el plano; el tamaño de cada signo indica su peso y el color de fondo la predicción del clasificador  
> Textos del gráfico: 0 · 1 · 2 · 3 · 4 · 5 · 6 · A · B · C · D · E · Eje X

- **Empezamos con 5 puntos** 4 puntos pertenecen a la **clase 1** (signo +) y 1 punto a la **clase 0** (signo −).
- *1* $w = \frac{1}{N}= \frac{1}{5}$ Todos los puntos parten con el mismo peso

| Punto | Peso |
| --- | --- |
| Wa | 1/5 |
| Wb | 1/5 |
| Wc | 1/5 |
| Wd | 1/5 |
| We | 1/5 |

---

## 43. Ronda 1: error de cada clasificador

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

- *1* w = 1/N
- *2* ε = Σ w (mal clasificados)
- *3* Elegir el de menor error
- *4* α = (1/2)·log((1−ε)/ε)
- *5* f(x) = Σ αₜ·hₜ(x)
- *6* Actualizar los pesos w

> **Gráfico:** Cinco puntos A a E en el plano; el tamaño de cada signo indica su peso y el color de fondo la predicción del clasificador  
> Textos del gráfico: 0 · 1 · 2 · 3 · 4 · 5 · 6 · A · B · C · D · E · Eje X · predice + · predice −

| Clasificador | Mal clasifica | Error |
| --- | --- | --- |
| X < 2 | B y E | 2/5 |
| X < 4 | B, C y E | 3/5 |
| X < 6 | C | 1/5 |
| X > 2 | A, C y D | 3/5 |
| X > 4 | A y D | 2/5 |
| X > 6 | A, B, D y E | 4/5 |

**Error** = suma de los pesos de los puntos mal clasificados.

Menor error: **X < 6** (ε = 1/5). Solo falla en el punto C.

---

## 44. Ronda 1: poder de voto y nuevos pesos

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

- *1* w = 1/N
- *2* ε = Σ w (mal clasificados)
- *3* Elegir el de menor error
- *4* α = (1/2)·log((1−ε)/ε)
- *5* f(x) = Σ αₜ·hₜ(x)
- *6* Actualizar los pesos w

> **Gráfico:** Cinco puntos A a E en el plano; el tamaño de cada signo indica su peso y el color de fondo la predicción del clasificador  
> Textos del gráfico: 0 · 1 · 2 · 3 · 4 · 5 · 6 · A · B · C · D · E · Eje X · predice + · predice −

**Poder de voto**

- *4* $\varepsilon = \frac{1}{5}$ C es el único punto mal clasificado
- *4* $\alpha = \frac{1}{2}\log \frac{1 - \frac{1}{5}}{\frac{1}{5}}$ $= \frac{1}{2}\log 4$
- *5* $h(x) = \frac{1}{2}\log 4 \cdot F(x < 6)$ Primer clasificador del conjunto

**Nuevos pesos** (paso 6)

- *C* mal: $w = \frac{\frac{1}{5}}{2 \cdot \frac{1}{5}}= \frac{1}{2}$
- *✓* bien: $w = \frac{\frac{1}{5}}{2 \cdot \frac{4}{5}}= \frac{1}{8}$

| Punto | Peso |
| --- | --- |
| Wa | 1/8 |
| Wb | 1/8 |
| Wc | 1/2 |
| Wd | 1/8 |
| We | 1/8 |

---

## 45. Ronda 2: error de cada clasificador

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

- *1* w = 1/N
- *2* ε = Σ w (mal clasificados)
- *3* Elegir el de menor error
- *4* α = (1/2)·log((1−ε)/ε)
- *5* f(x) = Σ αₜ·hₜ(x)
- *6* Actualizar los pesos w

> **Gráfico:** Cinco puntos A a E en el plano; el tamaño de cada signo indica su peso y el color de fondo la predicción del clasificador  
> Textos del gráfico: 0 · 1 · 2 · 3 · 4 · 5 · 6 · A · B · C · D · E · Eje X · predice + · predice −

| Clasificador | Mal clasifica | Error |
| --- | --- | --- |
| X < 2 | B y E | 2/8 |
| X < 4 | B, C y E | 6/8 |
| X < 6 | C | 4/8 |
| X > 2 | A, C y D | 6/8 |
| X > 4 | A y D | 2/8 |
| X > 6 | A, B, D y E | 4/8 |

Con los nuevos pesos, **C** pesa mucho más (1/2) y se recalculan los errores.

Empate en el menor error (2/8): **X < 2** y X > 4. Se elige el primero: **X < 2**.

---

## 46. Ronda 2: poder de voto y nuevos pesos

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

- *1* w = 1/N
- *2* ε = Σ w (mal clasificados)
- *3* Elegir el de menor error
- *4* α = (1/2)·log((1−ε)/ε)
- *5* f(x) = Σ αₜ·hₜ(x)
- *6* Actualizar los pesos w

> **Gráfico:** Cinco puntos A a E en el plano; el tamaño de cada signo indica su peso y el color de fondo la predicción del clasificador  
> Textos del gráfico: 0 · 1 · 2 · 3 · 4 · 5 · 6 · A · B · C · D · E · Eje X · predice + · predice −

**Poder de voto**

- *4* $\varepsilon = \frac{2}{8}= \frac{1}{4}$ B y E están mal clasificados
- learning rate *4* $\alpha = \frac{1}{2}\log \frac{1 - \frac{1}{4}}{\frac{1}{4}}$ $= \frac{1}{2}\log 3$
- *5* $h(x) = \frac{1}{2}\log 4 \cdot F(x < 6) + \frac{1}{2}\log 3 \cdot F(x < 2)$

**Nuevos pesos** (paso 6)

- *B* B y E (mal): $\frac{\frac{1}{8}}{2 \cdot \frac{1}{4}}= \frac{3}{12}$
- *✓* A y D: $\frac{\frac{1}{8}}{2 \cdot \frac{3}{4}}= \frac{1}{12}$ · C: $\frac{4}{12}$

| Punto | Peso |
| --- | --- |
| Wa | 1/12 |
| Wb | 3/12 |
| Wc | 4/12 |
| Wd | 1/12 |
| We | 3/12 |

---

## 47. Ronda 3: error de cada clasificador

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

- *1* w = 1/N
- *2* ε = Σ w (mal clasificados)
- *3* Elegir el de menor error
- *4* α = (1/2)·log((1−ε)/ε)
- *5* f(x) = Σ αₜ·hₜ(x)
- *6* Actualizar los pesos w

> **Gráfico:** Cinco puntos A a E en el plano; el tamaño de cada signo indica su peso y el color de fondo la predicción del clasificador  
> Textos del gráfico: 0 · 1 · 2 · 3 · 4 · 5 · 6 · A · B · C · D · E · Eje X · predice + · predice −

| Clasificador | Mal clasifica | Error |
| --- | --- | --- |
| X < 2 | B y E | 1/2 |
| X < 4 | B, C y E | 10/12 |
| X < 6 | C | 4/12 |
| X > 2 | A, C y D | 1/2 |
| X > 4 | A y D | 2/12 |
| X > 6 | A, B, D y E | 8/12 |

Ahora **B, C y E** pesan más (3/12, 4/12 y 3/12) y se recalculan los errores.

Menor error: **X > 4** (2/12). Es el clasificador elegido en esta ronda.

---

## 48. Ronda 3: poder de voto y clasificador final

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

- *1* w = 1/N
- *2* ε = Σ w (mal clasificados)
- *3* Elegir el de menor error
- *4* α = (1/2)·log((1−ε)/ε)
- *5* f(x) = Σ αₜ·hₜ(x)
- *6* Actualizar los pesos w

> **Gráfico:** Poder de voto de los tres clasificadores: mayor cuanto menor es su error  
> Textos del gráfico: Poder de voto α de cada clasificador · Clasificador 1 · x < 6 · α ≈ 0,69 · ε = 1/5 · Clasificador 2 · x < 2 · α ≈ 0,55 · ε = 1/4 · Clasificador 3 · x > 4 · α ≈ 0,80 · ε = 1/6

- *4* $\varepsilon = \frac{2}{12}= \frac{1}{6}$ Solo A y D están mal clasificados
- *4* $\alpha = \frac{1}{2}\log \frac{1 - \frac{1}{6}}{\frac{1}{6}}$ $= \frac{1}{2}\log 5$
- *5* $h(x) = \frac{1}{2}\log 4 \cdot F(x < 6) + \frac{1}{2}\log 3 \cdot F(x < 2)$ $+ \frac{1}{2}\log 5 \cdot F(x > 4)$ Conjunto final con los tres clasificadores débiles

---

## 49. Resultado: combinación de 3 clasificadores débiles

_5 · Técnicas: AdaBoost_

_Aplica a: Regresión, Clasificación_

> **Gráfico:** Los tres clasificadores débiles del ejemplo y la combinación ponderada final  
> Textos del gráfico: Clasificador 1: x < 6 · A · B · C · D · E · falla en C · Clasificador 2: x < 2 · A · B · C · D · E · falla en B y E · Clasificador 3: x > 4 · A · B · C · D · E · falla en A y D · $h(x) = \frac{1}{2}\log 4 \cdot F(x<6) + \frac{1}{2}\log 3 \cdot F(x<2) + \frac{1}{2}\log 5 \cdot F(x>4)$

- **1 · Primer clasificador** Clasifica mal el punto **C**.
- **2 · Segundo clasificador** Clasifica mal los puntos **B** y **E**.
- **3 · Tercer clasificador** Clasifica mal los puntos **A** y **D**.

---

## 50. Gradient Boosting

_5 · Técnicas: Gradient Boosting_

_Aplica a: Regresión, Clasificación_

Es una **generalización** del algoritmo AdaBoost. Su objetivo es crear modelos de forma **secuencial**, donde cada modelo ajusta los **residuos (errores)** de los modelos anteriores.

> **Gráfico:** Gradient Boosting: predicción inicial más tres árboles, cada uno multiplicado por la tasa de aprendizaje 0,1  
> Textos del gráfico: 71,2 · predicción inicial · + · 0,1 · × · Árbol 1 · + · 0,1 · × · Árbol 2 · + · 0,1 · × · Árbol 3 · 0,1 = learning rate (tasa de aprendizaje) · escala cuánto aporta cada árbol nuevo

- **Predicción inicial** Se parte de un valor sencillo, por ejemplo el promedio del objetivo.
- **Un árbol por ronda** Cada árbol nuevo predice los residuos que dejó el modelo anterior.

**Learning rate**

El **0,1** que multiplica a cada árbol: escala cuánto aporta cada árbol nuevo.

Referencias: <https://www.cienciadedatos.net/documentos/py09_gradient_boosting_python.html> · <https://www.youtube.com/watch?v=3CC4N4z3GJc&list=RDCMUCtYLUTtgS3k1Fg4y5tAhLbw&index=1>

---

## 51. Ejemplo: predecir el peso

_5 · Técnicas: Gradient Boosting_

_Aplica a: Regresión, Clasificación_

Queremos **predecir el peso (kg)** de una persona a partir de su altura, su color favorito y su género.

| Altura (m) | Color favorito | Género | Peso (kg) |
| --- | --- | --- | --- |
| 1,6 | Azul | Hombre | **88** |
| 1,6 | Verde | Mujer | **76** |
| 1,5 | Azul | Mujer | **56** |
| 1,8 | Rojo | Hombre | **73** |
| 1,5 | Verde | Hombre | **77** |
| 1,4 | Azul | Mujer | **57** |

- **Variable objetivo** El **peso (kg)**: es lo que se quiere predecir (regresión).
- **Variables predictoras Altura**, **color favorito** y **género**.

Referencias: <https://www.youtube.com/watch?v=3CC4N4z3GJc> · <https://www.youtube.com/watch?v=jxuNLH5dXCs>

---

## 52. Paso 1: predicción inicial y residuales

_5 · Técnicas: Gradient Boosting_

_Aplica a: Regresión, Clasificación_

Se empieza con una **hoja** que predice el **peso promedio** de todos. Luego se calcula el **residual** de cada persona: el error de esa predicción.

Peso promedio

71,2

$\frac{88 + 76 + 56 + 73 + 77 + 57}{6}$

**Residual**

`Peso observado − Peso predicho`

(88 − 71,2) = **16,8**

| Altura (m) | Color | Género | Peso (kg) | Residual |
| --- | --- | --- | --- | --- |
| 1,6 | Azul | Hombre | 88 | **16,8** |
| 1,6 | Verde | Mujer | 76 | 4,8 |
| 1,5 | Azul | Mujer | 56 | −15,2 |
| 1,8 | Rojo | Hombre | 73 | 1,8 |
| 1,5 | Verde | Hombre | 77 | 5,8 |
| 1,4 | Azul | Mujer | 57 | −14,2 |

---

## 53. Paso 2: un árbol para predecir los residuales

_5 · Técnicas: Gradient Boosting_

_Aplica a: Regresión, Clasificación_

Se construye un árbol con **altura, color favorito y género** para **predecir los residuales**. Si una hoja agrupa varios residuales, se reemplaza por su **promedio**.

> **Gráfico:** Árbol de regresión que predice los residuales con las variables género, altura y color favorito  
> Textos del gráfico: Residuales que caen en cada hoja · Sí · No · Sí · No · Sí · No · Género = F · Altura < 1,6 · Color no azul · −14,2; −15,2 · 4,8 · 1,8; 5,8 · 16,8

→

promedio

> **Gráfico:** Árbol de regresión que predice los residuales con las variables género, altura y color favorito  
> Textos del gráfico: Valor de cada hoja (promedio) · Sí · No · Sí · No · Sí · No · Género = F · Altura < 1,6 · Color no azul · −14,7 · 4,8 · 3,8 · 16,8

Referencias: youtube.com/watch?v=3CC4N4z3GJc

---

## 54. Learning rate: la tasa de aprendizaje

_5 · Técnicas: Gradient Boosting_

_Aplica a: Regresión, Clasificación_

**¿A qué se refiere el learning rate?**

Es un valor **entre 0 y 1** que **escala la contribución del árbol nuevo**. En vez de sumar todo el valor de la hoja, se suma solo una fracción (aquí, **0,1**): así se avanza con **pasos pequeños** y el modelo generaliza mejor.

> **Gráfico:** Con un learning rate de 0,1 la predicción avanza un paso pequeño, de 71,2 a 72,9, hacia el peso observado de 88  
> Textos del gráfico: Predicción del peso de la primera persona (kg) · 70 · 75 · 80 · 85 · 90 · learning rate = 1: salto directo hasta el valor observado · (se ajusta demasiado a los datos de entrenamiento) · 71,2 · predicción inicial · 72,9 · 0,1 × 16,8 = paso pequeño · 88 · peso observado

- **Fórmula** Peso predicho = 71,2 + (**0,1** × 16,8)
- **Resultado** 71,2 + 1,68 = **72,9**: un poco más cerca de 88.
- **Por qué** Muchos pasos pequeños dan mejores predicciones que un único salto grande.

Referencias: youtube.com/watch?v=3CC4N4z3GJc

---

## 55. Nuevos residuales tras el primer árbol

_5 · Técnicas: Gradient Boosting_

_Aplica a: Regresión, Clasificación_

Con la predicción actualizada se calculan **nuevos residuales**: son los que quedan después de sumar el árbol nuevo **escalado por el learning rate**.

| Persona | Valor de su hoja | Residual inicial | Residual nuevo |
| --- | --- | --- | --- |
| 1 | 16,8 | 16,8 | **15,1** |
| 2 | 4,8 | 4,8 | **4,3** |
| 3 | −14,7 | −15,2 | **−13,7** |
| 4 | 3,8 | 1,8 | **1,4** |
| 5 | 3,8 | 5,8 | **5,4** |
| 6 | −14,7 | −14,2 | **−12,7** |

- *1* $\text{nuevo}= \text{inicial}- 0,1 \times \text{hoja}$ Se resta la parte que el árbol ya explicó
- *≈* $16,8 - (0,1 \times 16,8) = 15,1$ Ejemplo con la persona 1

Todos los residuales (en valor absoluto) son **menores**: se dio un pequeño paso hacia mejores predicciones.

---

## 56. Paso 3: un segundo árbol sobre los nuevos residuales

_5 · Técnicas: Gradient Boosting_

_Aplica a: Regresión, Clasificación_

Se repite el proceso: **un nuevo árbol** predice los nuevos residuales (de nuevo con altura, color y género), y sus hojas se promedian.

> **Gráfico:** Árbol de regresión que predice los residuales con las variables género, altura y color favorito  
> Textos del gráfico: Nuevos residuales por hoja · Sí · No · Sí · No · Sí · No · Género = F · Altura < 1,6 · Color no azul · −12,7; −13,7 · 4,3 · 1,4; 5,4 · 15,1

→

promedio

> **Gráfico:** Árbol de regresión que predice los residuales con las variables género, altura y color favorito  
> Textos del gráfico: Valor de cada hoja (promedio) · Sí · No · Sí · No · Sí · No · Género = F · Altura < 1,6 · Color no azul · −13,2 · 4,3 · 3,4 · 15,1

$71,2 + (0,1 \times 16,8) + (0,1 \times 15,1) = 74,4$

Predicción de la persona 1 con la base y los dos árboles (peso real: 88)

---

## 57. Los residuales se reducen en cada ronda

_5 · Técnicas: Gradient Boosting_

_Aplica a: Regresión, Clasificación_

En cada ronda el árbol nuevo, escalado por el learning rate (**0,1**), da **otro pequeño paso** hacia mejores predicciones: los residuales (barras) se acortan de una iteración a la siguiente.

| Persona | Inicial | Tras árbol 1 | Tras árbol 2 |
| --- | --- | --- | --- |
| 1 | **16,8** | **15,1** | **13,6** |
| 2 | **4,8** | **4,3** | **3,9** |
| 3 | **−15,2** | **−13,7** | **−12,4** |
| 4 | **1,8** | **1,4** | **1,1** |
| 5 | **5,8** | **5,4** | **5,1** |
| 6 | **−14,2** | **−12,7** | **−11,4** |
| \|resid.\| promedio | **9,8** | **↓ 8,8** | **↓ 7,9** |

**Modelo final**

$F(x) = 71,2 + 0,1\cdot T_{1}(x) + 0,1\cdot T_{2}(x) + \ldots + 0,1\cdot T_{m}(x)$

- **Learning rate** Cada árbol suma solo el 10 % de su valor: pasos pequeños y seguros.
- **Se repite** Se agregan árboles hasta que los residuales son pequeños o se alcanza el máximo de árboles.

---

## 58. ¡ Gracias !

_Aprendizaje automático · Analítica de datos_

Regresión lineal y logística Bayesiano k-NN SVM Árboles y Random Forest AdaBoost Gradient Boosting

¿Preguntas?

UNIVERSIDAD DE ANTIOQUIA JORGE BEDOYA

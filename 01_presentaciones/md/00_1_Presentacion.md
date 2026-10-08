# Aprendizaje Automático I

> Versión Markdown generada a partir de `00_1_Presentacion.html` · 13 diapositivas. Los gráficos se describen por su texto; las fórmulas están en LaTeX (`$...$`).

---

## 1. Aprendizaje Automático I

_Especialización en Analítica y Ciencia de Datos · UdeA_

Fundamentos, modelos y buenas prácticas de Machine Learning aplicado — de la regresión lineal al boosting.

Cohorte 2026 9 sesiones · oct–nov

UNIVERSIDAD DE ANTIOQUIA JORGE BEDOYA

---

## 2. Objetivos

_Presentación del curso_

*[Imagen]*

Enfoque · precisión

Dotar al estudiante de los **elementos teóricos y las capacidades** para diseñar, implementar y evaluar sistemas basados en aprendizaje automático, y usarlos para **solucionar problemas aplicados**.

- **01** **Identificar el tipo de problema** — Clasificar los problemas de aprendizaje y asociarlos con casos de aplicación reales.
- **02** **Seleccionar el modelo adecuado** — Elegir el tipo de modelo más apropiado según las restricciones del problema.
- **03** **Diseñar la solución completa** — Del análisis del problema hasta un modelo entrenado y evaluado.

---

## 3. Unidades de aprendizaje

_Plan del curso · 4 unidades_

*[Imagen]*

Primeros pasos

- **U1** **Introducción y fundamentos** — Definiciones, taller Sklearn · Regresión lineal y logística · dataset grande: limpieza + train/test
- **U2** **Clasificación y selección de modelos** — K-NN vs Gaussian · overfitting y regularización · k-fold, estratificado, por grupos, bootstrapping
- **U3** **Árboles de decisión y SVM** — Bagging + Random Forest · SVM One vs All / All vs All · comparación de modelos
- **U4** **Boosting y selección de características** — AdaBoost, Gradient Boosting (+XGBoost/LightGBM) · importancia de variables

---

## 4. Cronograma

_Vista general · 10 oct – 7 nov 2026_

Unidad 1

Unidad 2

Unidad 3 + 4

Cierre

**10 oct 17 oct 24 oct 31 oct 7 nov**

**Unidad 1**

10, 16 y 17 oct

**Unidad 2**

23 y 24 oct

**Unidad 3 + 4**

30 y 31 oct

**Cierre**

6 y 7 nov

+ 2 asesorías virtuales (20 oct y 3 nov) y una charla invitada (6 nov). Detalle hora por hora en la siguiente diapositiva.

---

## 5. Cronograma detallado

_Detalle hora por hora · por confirmar_

**Semanas 1–2 · Unidades 1–2**

| Fecha y horario | Contenido |
| --- | --- |
| Sáb 10 oct · 8:00–14:00 | U1 · Introducción, definiciones, taller Sklearn |
| Vie 16 oct · 17:00–21:00 | U1 · Regresión lineal y logística |
| Sáb 17 oct · 8:00–14:00 | U1 · Regresión (continuación) · **Taller 0** |
| Mar 20 oct · 18:00–20:00 | Asesoría virtual |
| Vie 23 oct · 17:00–21:00 | U2 · K-NN vs Gaussian |
| Sáb 24 oct · 8:00–14:00 | U2 · Selección de modelos, overfitting · **Taller 1** |

**Semanas 3–4 · Unidades 3–4 y cierre**

| Fecha y horario | Contenido |
| --- | --- |
| Vie 30 oct · 17:00–21:00 | U3 · Máquinas de Vectores de Soporte |
| Sáb 31 oct · 8:00–14:00 | U3 Árboles+RF, U4 Boosting · **Taller 2** |
| Mar 3 nov · 18:00–20:00 | Asesoría virtual |
| Vie 6 nov · 17:00–18:00 | U4 · Selección de características |
| Vie 6 nov · 18:00–21:00 | Charla invitada · Científico de Datos |
| Sáb 7 nov · 8:00–10:00 | Entrega de trabajos y preparación |
| Sáb 7 nov · 10:00–14:00 | Presentaciones finales (4 h) |

Inicia 10 oct · termina 7 nov — sábados 17, 24 y 31 oct: taller de la semana 12:00–14:00.

---

## 6. Sesión de presentaciones finales

_Sábado 7 de noviembre · 8:00–14:00_

8:00 — 10:00 · Entrega y preparación

10:00 — 14:00 · Presentaciones · 4 horas

**8:00 10:00 14:00**

**Entrega y preparación**

Recepción de los trabajos finales y últimos ajustes antes de presentar.

**Presentaciones · 4 h**

`15 min + 5 min preguntas` por equipo ≈ 12 equipos máx. Orden por sorteo.

---

## 7. Metodología

_Cómo trabajamos_

*[Imagen]*

Aprender haciendo

- **A** **Clases magistrales** — Para algunos conceptos y definiciones básicas que sustentan cada técnica.
- **B** **Clases tipo taller** — Los estudiantes aplican técnicas y métodos, guiados por el docente.
- **C** **Talleres de clase + casa** — Se inician en clase y se complementan de forma autónoma.

---

## 8. Herramientas

_Stack del curso · 100% en la nube_

El curso se dicta aquí

*[Imagen]*

Google Colab

Ejecución de notebooks sin instalación local, desde el navegador.

Python

Lenguaje base: pandas, scikit-learn, seaborn.

GitHub

Repositorio oficial: notebooks, datasets y modelos.

IDE de tu preferencia

VS Code, PyCharm, JupyterLab local, etc. — opcional, no es requisito del curso.

---

## 9. Entregables

_Evaluación · parte 1_

*[Imagen]*

15 min · tu turno

Hasta **4 trabajos** comentados y ejecutados. Si un trabajo tiene varios archivos, agrúpalos en una **carpeta** — ej.: `equipo_x/` con *preparación de datos*, *construcción del modelo*, *documentación*, etc.

1. 1 Autores

2. 2 Descripción corta del dataset

3. 3 Objetivo a desarrollar esencial

4. 4 Desarrollo de experimentos: preparación de datos, creación y evaluación de modelos esencial

5. 5 Conclusiones esencial

6. 6 Referencias esencial

+ presentación de 15 min por equipo (sábado 7 nov). Incluir el dataset completo o una muestra según su tamaño.

---

## 10. Tipos de trabajo

_Proyecto final_

*[Imagen]*

Curiosidad ante todo

- **01** **1 dataset y múltiples modelos** — Profundizar en un problema comparando varias técnicas sobre los mismos datos.
- **02** **Varios datasets y varios modelos** — Explorar cómo se comportan las técnicas frente a problemas de distinta naturaleza.

**Objetivo en ambos casos:** identificar y ajustar el "mejor" modelo, e identificar las características propias de cada técnica.

---

## 11. Criterios de valoración

_Evaluación · parte 2_

*[Imagen]*

Detalle y color

- **01** Relación con lo visto en el curso
- **02** Nivel de profundización en los experimentos
- **03** Nivel de investigación
- **04** Cantidad de técnicas vs. nivel de complejidad
- **05** Claridad de conclusiones, descripciones y comentarios
- **06** Ortografía y redacción

---

## 12. Material y contacto

_Recursos del curso_

Entregas · envíos · repos

**Repositorio del curso**

github.com/mrbedoya/ml-2026

**📩 Envío de talleres — aquí**

jabedoyap79@gmail.com

Jorge Bedoya

**Email** mrbedoya@gmail.com

**Cel** 310 503 9131

---

## 13. ¿Pre guntas ?

_Sábado 10 de octubre · 8:00_

Todo el material está en el repositorio del curso. Próxima sesión: Introducción y fundamentos del aprendizaje automático.

jorge·ml APRENDIZAJE AUTOMÁTICO I

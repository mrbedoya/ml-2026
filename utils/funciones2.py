#Librerias
import math
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import (mean_absolute_error, 
                             r2_score,
                             root_mean_squared_error)
from sktime.performance_metrics.forecasting import mean_absolute_scaled_error


def identificar_outliers(df, numCols):
    """
    Identifica los índices de los valores outliers en un DataFrame para una lista de variables numéricas.

    Parámetros:
    df (pd.DataFrame): El DataFrame que contiene los datos.
    numCols (list): Lista de nombres de las columnas numéricas a analizar.

    Retorna:
    list: Lista de índices de los valores outliers.
    """
    # Lista para almacenar los índices de los outliers
    outliers_indices = []

    for var in numCols:
        # Calcular el rango intercuartílico (IQR)
        Q1 = df[var].quantile(0.25)
        Q3 = df[var].quantile(0.75)
        IQR = Q3 - Q1

        # Definir los límites para identificar outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Identificar los índices de los outliers
        outliers = df[(df[var] < lower_bound) | (df[var] > upper_bound)].index.tolist()
        
        # Agregar los índices a la lista de outliers
        outliers_indices.extend(outliers)

    return outliers_indices

def eval_model(model, X_train, y_train):
    """
    Permite evaluar el rendimiento de un modelo de regresión utilizando varias métricas.

    Parámetros:
    model (object): El modelo de regresión que se va a evaluar.
    X_train (array-like): Conjunto de características de entrenamiento.
    y_train (array-like): Valores reales de la variable objetivo para el conjunto de entrenamiento.

    Retorna:
    dict: Un diccionario que contiene las siguientes métricas de evaluación:
        - "mae": Error absoluto medio (Mean Absolute Error).
        - "rmse": Raíz del error cuadrático medio (Root Mean Squared Error).
        - "r2": Coeficiente de determinación (R²).
        - "mase": Error absoluto medio escalado (Mean Absolute Scaled Error).
    """
    y_pred = model.predict(X_train)

    metrics = {
        "mae": round(mean_absolute_error(y_train, y_pred), 5),
        "rmse": round(root_mean_squared_error(y_train, y_pred), 5),
        "r2": round(r2_score(y_train, y_pred), 5),
        "mase": round(mean_absolute_scaled_error(y_train, y_pred, y_train=y_train), 5)
    }

    return metrics

def plot_param_perf(x, y_data, title, x_label, y_label):
    """
    Grafica el rendimiento del modelo en función de un parámetro ajustado.

    Parámetros:
    x (iterable): Valores del parámetro ajustado.
    y_data (dict): Diccionario con las métricas de rendimiento para entrenamiento y prueba.
    title (str): Título del gráfico.
    x_label (str): Etiqueta del eje x.
    y_label (str): Etiqueta del eje y.
    """
    y_train = y_data["train"]
    y_test = y_data["test"]

    # Graficar las métricas de rendimiento para entrenamiento y prueba
    sns.lineplot(x=x, y=y_train, label="train")
    sns.lineplot(x=x, y=y_test, label="test")
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()
    

def search_param(base_model, X_train, y_train, X_test, y_test, base_params, search_param, search_range):
    """
    Busca el mejor valor para un parámetro específico del modelo, evaluando el rendimiento
    en términos de R² y MASE para los conjuntos de entrenamiento y prueba.

    Parámetros:
    base_model (object): El modelo base que se va a ajustar.
    X_train (array-like): Conjunto de características de entrenamiento.
    y_train (array-like): Valores reales de la variable objetivo para el conjunto de entrenamiento.
    X_test (array-like): Conjunto de características de prueba.
    y_test (array-like): Valores reales de la variable objetivo para el conjunto de prueba.
    base_params (dict): Parámetros base del modelo.
    search_param (str): El nombre del parámetro que se va a ajustar.
    search_range (iterable): Rango de valores para el parámetro que se va a buscar.

    Retorna:
    tuple: Dos diccionarios que contienen las métricas R² y MASE para los conjuntos de entrenamiento y prueba.
    """
    r2_train = []
    r2_test = []
    mase_train = []
    mase_test = []

    for param in search_range:
        
        # Actualizar los parámetros del modelo con el valor actual del parámetro en búsqueda
        model_params = base_params
        model_params[search_param] = param
        current_model = base_model.set_params(**model_params)

        print(f"Ajustando para {search_param}={param}")
        current_model.fit(X_train, y_train)

        # Guardar R² para entrenamiento y prueba
        r2_train.append(r2_score(y_train, current_model.predict(X_train)))
        r2_test.append(r2_score(y_test, current_model.predict(X_test)))

        # Guardar MASE para entrenamiento y prueba
        mase_train.append(
            mean_absolute_scaled_error(
                y_train, current_model.predict(X_train), y_train=y_train
            )
        )
        mase_test.append(
            mean_absolute_scaled_error(
                y_test, current_model.predict(X_test), y_train=y_test
            )
        )

    # Guardar métricas en diccionarios
    r2_scores = {"train": r2_train, "test": r2_test}
    mase_scores = {"train": mase_train, "test": mase_test}
    return r2_scores, mase_scores
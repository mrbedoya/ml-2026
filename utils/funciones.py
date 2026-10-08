"""Funciones de apoyo para los notebooks del curso de Aprendizaje Automático.

Este módulo unifica las antiguas ``funciones.py`` y ``funciones2.py`` en un solo archivo (los notebooks siguen usando ``from funciones import …``).

Contenido
---------
Exploración y gráficos
    ``multiple_plot``        gráficos de barras, cajas o matriz de dispersión en una sola llamada.
    ``plot_roc_curve``       curva ROC.
    ``plot_param_perf``      rendimiento de un modelo al variar un hiperparámetro.
Correlación y multicolinealidad
    ``tidy_corr_matrix``     matriz de correlación en formato largo (tidy).
    ``check_vif``            factor de inflación de la varianza (VIF).
Agrupamiento
    ``silhouette_analysis``  gráfico de silueta para varios valores de k (K-Means).
    ``plot_dendrogram``      dendrograma de un modelo ``AgglomerativeClustering``.
Datos atípicos
    ``identificar_outliers`` índices de valores atípicos por la regla del rango intercuartílico.
Evaluación de modelos de regresión
    ``mean_absolute_scaled_error``, ``eval_model``, ``search_param``.

Uso en un notebook
------------------
    import sys
    sys.path.append('utils/')
    from funciones import multiple_plot, plot_roc_curve

Dependencias
------------
Obligatorias: numpy, pandas, matplotlib, seaborn, scikit-learn.
Opcionales (se importan solo cuando se usan): statsmodels (``check_vif``) y scipy
(``plot_dendrogram``). Ya no se requiere ``sktime``: el MASE está implementado aquí.
"""
from __future__ import annotations

import math
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.base import clone
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

__all__ = [
    "multiple_plot",
    "plot_roc_curve",
    "plot_param_perf",
    "tidy_corr_matrix",
    "check_vif",
    "checkVIF",
    "silhouette_analysis",
    "plot_dendrogram",
    "identificar_outliers",
    "mean_absolute_scaled_error",
    "eval_model",
    "search_param",
]

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------
PALETA = "nipy_spectral"
COLOR_PRINCIPAL = "steelblue"
COLOR_SECUNDARIO = "forestgreen"
TIPOS_GRAFICO = ("countplot", "boxplot", "scatterplot")

ColumnasT = Union[str, Sequence[str], None]


def _version_seaborn() -> Tuple[int, int]:
    partes = sns.__version__.split(".")
    return int(partes[0]), int(partes[1])


# A partir de seaborn 0.13 usar ``palette`` sin ``hue`` está obsoleto.
_SEABORN_CON_HUE = _version_seaborn() >= (0, 13)


def _kwargs_paleta(variable: Optional[str]) -> dict:
    """Argumentos de color compatibles con las distintas versiones de seaborn."""
    if _SEABORN_CON_HUE and variable is not None:
        return {"hue": variable, "palette": PALETA, "legend": False}
    return {"palette": PALETA}


def _validar_columnas(data: pd.DataFrame, columnas: Iterable[Optional[str]]) -> None:
    faltantes = [c for c in columnas if c is not None and c not in data.columns]
    if faltantes:
        raise KeyError(f"Columnas no encontradas en el DataFrame: {faltantes}")


# ---------------------------------------------------------------------------
# Exploración y gráficos
# ---------------------------------------------------------------------------
def multiple_plot(
    ncols: int,
    data: pd.DataFrame,
    columns: ColumnasT,
    target_var: Optional[str],
    plot_type: str,
    title: str,
    rot: int = 0,
    figsize: Optional[Tuple[float, float]] = None,
) -> None:
    """Dibuja uno o varios gráficos exploratorios a partir de un DataFrame.

    Parameters
    ----------
    ncols : int
        Número de columnas de la cuadrícula de subgráficos (si ``columns`` es una lista).
    data : pd.DataFrame
        Datos a graficar.
    columns : str | list[str] | None
        Variable(s) a graficar. Una lista genera un subgráfico por variable; un texto
        genera un único gráfico (en ``boxplot`` es la variable del eje x).
    target_var : str | None
        Variable objetivo: en ``countplot`` es la variable cuyas frecuencias se cuentan
        (gráfico único); en ``boxplot`` es la variable numérica del eje y.
    plot_type : {'countplot', 'boxplot', 'scatterplot'}
        Tipo de gráfico. ``scatterplot`` produce una matriz de dispersión (pairplot)
        con las variables de ``columns``.
    title : str
        Título general de la figura.
    rot : int, default 0
        Ángulo de rotación de las etiquetas del eje x.
    figsize : tuple, opcional
        Tamaño de la figura; por defecto se calcula según el número de filas.

    Examples
    --------
    >>> multiple_plot(1, d, None, 'bad_credit', 'countplot', 'Frecuencia de bad_credit')
    >>> multiple_plot(1, d, 'purpose', 'age_yrs', 'boxplot', 'Propósito vs. edad', 90)
    >>> multiple_plot(1, d, numCols, None, 'scatterplot', 'Variables numéricas')
    >>> multiple_plot(3, d, catCols, None, 'countplot', 'Variables categóricas', 30)
    >>> multiple_plot(3, d, catCols, 'age_yrs', 'boxplot', 'Categóricas vs. edad', 30)
    """
    if plot_type not in TIPOS_GRAFICO:
        raise ValueError(f"plot_type debe ser uno de {TIPOS_GRAFICO}; se recibió '{plot_type}'.")
    if ncols < 1:
        raise ValueError("ncols debe ser un entero mayor o igual a 1.")

    # --- Matriz de dispersión -------------------------------------------------
    if plot_type == "scatterplot":
        columnas = [columns] if isinstance(columns, str) else list(columns or [])
        if not columnas:
            raise ValueError("scatterplot requiere una lista de columnas.")
        _validar_columnas(data, columnas)
        grafico = sns.pairplot(
            data[columnas],
            diag_kind="kde",
            diag_kws={"color": COLOR_SECUNDARIO},
            plot_kws={"color": COLOR_PRINCIPAL},
        )
        grafico.fig.set_size_inches(*(figsize or (12, 12)))
        grafico.fig.suptitle(title, fontsize=14, fontweight="bold")
        plt.subplots_adjust(top=0.9)
        plt.show()
        return

    # --- Un único gráfico -----------------------------------------------------
    if not isinstance(columns, (list, tuple)):
        if plot_type == "countplot":
            _validar_columnas(data, [target_var])
            if target_var is None:
                raise ValueError("countplot de un solo gráfico requiere target_var.")
            fig, ax = plt.subplots(figsize=figsize or (6, 4))
            sns.countplot(
                data=data, x=target_var, ax=ax, zorder=1, alpha=0.8,
                order=data[target_var].value_counts().index,
                **_kwargs_paleta(target_var),
            )
        else:  # boxplot
            if columns is None or target_var is None:
                raise ValueError("boxplot de un solo gráfico requiere columns (x) y target_var (y).")
            _validar_columnas(data, [columns, target_var])
            fig, ax = plt.subplots(figsize=figsize or (6, 4))
            sns.boxplot(data=data, x=columns, y=target_var, ax=ax, zorder=1, **_kwargs_paleta(columns))
        ax.tick_params(axis="x", labelrotation=rot)
        ax.set_title(title, fontsize=14, fontweight="bold", y=1.1)
        return

    # --- Varios subgráficos ---------------------------------------------------
    columnas = list(columns)
    if not columnas:
        raise ValueError("La lista de columnas está vacía.")
    _validar_columnas(data, columnas + ([target_var] if plot_type == "boxplot" else []))
    if plot_type == "boxplot" and target_var is None:
        raise ValueError("boxplot requiere target_var (variable del eje y).")

    nrows = math.ceil(len(columnas) / ncols)
    fig, axes = plt.subplots(nrows, ncols, figsize=figsize or (15, nrows * 3 + 1), squeeze=False)
    ejes = axes.ravel()

    for ax, columna in zip(ejes, columnas):
        if plot_type == "countplot":
            sns.countplot(
                data=data, x=columna, ax=ax, zorder=1, edgecolor="black", linewidth=0.5,
                order=data[columna].value_counts().index, **_kwargs_paleta(columna),
            )
        else:
            sns.boxplot(data=data, x=columna, y=target_var, ax=ax, zorder=1, **_kwargs_paleta(columna))
        ax.grid(axis="y", zorder=0)
        ax.tick_params(axis="x", labelrotation=rot, labelsize=8)
        ax.tick_params(axis="y", labelsize=8)
        ax.set_title(columna, fontsize=10)
        ax.set_xlabel("")

    for ax in ejes[len(columnas):]:  # elimina los ejes sobrantes
        fig.delaxes(ax)

    fig.tight_layout()
    fig.suptitle(title, fontsize=14, fontweight="bold", y=0.95)
    fig.subplots_adjust(top=0.9)


def plot_roc_curve(fpr, tpr, auc_score: Optional[float] = None, ax=None) -> None:
    """Dibuja la curva ROC.

    Parameters
    ----------
    fpr, tpr : array-like
        Tasa de falsos positivos y de verdaderos positivos (salida de ``roc_curve``).
    auc_score : float, opcional
        Si se indica, se muestra en la leyenda.
    ax : matplotlib.axes.Axes, opcional
        Eje donde dibujar. Si es ``None`` se usa el eje actual y se muestra la figura.
    """
    mostrar = ax is None
    ax = ax or plt.gca()
    etiqueta = "ROC" if auc_score is None else f"ROC (AUC = {auc_score:.3f})"
    ax.plot(fpr, tpr, color="orange", label=etiqueta)
    ax.plot([0, 1], [0, 1], color="darkblue", linestyle="--")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("Receiver Operating Characteristic (ROC) Curve")
    ax.legend()
    if mostrar:
        plt.show()


def plot_param_perf(
    x: Iterable,
    y_data: Dict[str, Sequence[float]],
    title: str,
    x_label: str,
    y_label: str,
    ax=None,
) -> None:
    """Grafica el rendimiento (entrenamiento y prueba) frente al valor de un hiperparámetro.

    Parameters
    ----------
    x : iterable
        Valores del hiperparámetro.
    y_data : dict
        Diccionario con las claves ``"train"`` y ``"test"`` (salida de ``search_param``).
    title, x_label, y_label : str
        Textos del gráfico.
    ax : matplotlib.axes.Axes, opcional
        Eje donde dibujar. Si es ``None`` se usa el eje actual y se muestra la figura.
    """
    mostrar = ax is None
    ax = ax or plt.gca()
    sns.lineplot(x=list(x), y=list(y_data["train"]), label="train", ax=ax)
    sns.lineplot(x=list(x), y=list(y_data["test"]), label="test", ax=ax)
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    if mostrar:
        plt.show()


# ---------------------------------------------------------------------------
# Correlación y multicolinealidad
# ---------------------------------------------------------------------------
def tidy_corr_matrix(corr_mat: pd.DataFrame) -> pd.DataFrame:
    """Convierte una matriz de correlación en formato largo (tidy).

    Cada par aparece dos veces (A-B y B-A); se excluye la diagonal y se ordena por
    correlación absoluta descendente.

    Returns
    -------
    pd.DataFrame
        Columnas ``variable_1``, ``variable_2``, ``r`` y ``abs_r``.
    """
    tidy = corr_mat.stack().reset_index()
    tidy.columns = ["variable_1", "variable_2", "r"]
    tidy = tidy.loc[tidy["variable_1"] != tidy["variable_2"]].copy()
    tidy["abs_r"] = tidy["r"].abs()
    return tidy.sort_values("abs_r", ascending=False)


def check_vif(X: pd.DataFrame) -> pd.DataFrame:
    """Calcula el factor de inflación de la varianza (VIF) de cada variable.

    El VIF mide cuánto se explica una variable a partir de las demás: valores entre
    5 y 10 suelen tomarse como umbral de multicolinealidad (más exigente cuanto menor).

    Parameters
    ----------
    X : pd.DataFrame
        Variables predictoras numéricas, sin valores nulos.

    Returns
    -------
    pd.DataFrame
        Columnas ``Features`` y ``VIF``, ordenadas de mayor a menor VIF.
    """
    from statsmodels.stats.outliers_influence import variance_inflation_factor

    if not isinstance(X, pd.DataFrame):
        raise TypeError("X debe ser un DataFrame de pandas.")
    if X.isna().any().any():
        raise ValueError("X contiene valores nulos; imputa o elimina antes de calcular el VIF.")

    valores = X.to_numpy(dtype=float)
    vif = pd.DataFrame({
        "Features": X.columns,
        "VIF": [variance_inflation_factor(valores, i) for i in range(X.shape[1])],
    })
    vif["VIF"] = vif["VIF"].round(2)
    return vif.sort_values("VIF", ascending=False).reset_index(drop=True)


checkVIF = check_vif  # alias de compatibilidad con los notebooks anteriores


# ---------------------------------------------------------------------------
# Agrupamiento
# ---------------------------------------------------------------------------
def silhouette_analysis(
    X,
    range_n_clusters: Iterable[int],
    random_state: int = 10,
    figsize: Tuple[float, float] = (19, 4),
) -> Dict[int, float]:
    """Gráfico de silueta de K-Means para varios números de grupos.

    Parameters
    ----------
    X : array-like
        Datos (idealmente escalados).
    range_n_clusters : iterable de int
        Valores de k a evaluar (cada uno debe ser >= 2).
    random_state : int, default 10
        Semilla para reproducibilidad.
    figsize : tuple
        Tamaño de cada figura.

    Returns
    -------
    dict
        Silueta promedio por cada k.
    """
    from sklearn.cluster import KMeans
    from sklearn.metrics import silhouette_samples, silhouette_score

    X = np.asarray(X)
    puntajes: Dict[int, float] = {}

    for k in range_n_clusters:
        etiquetas = KMeans(n_clusters=k, random_state=random_state, n_init=10).fit_predict(X)
        promedio = silhouette_score(X, etiquetas)
        valores = silhouette_samples(X, etiquetas)
        puntajes[k] = float(promedio)

        fig, ax = plt.subplots(figsize=figsize)
        ax.set_xlim([-0.1, 1])
        ax.set_ylim([0, len(X) + (k + 1) * 10])  # espacio en blanco entre grupos

        y_inf = 10
        for i in range(k):
            vals_i = np.sort(valores[etiquetas == i])
            y_sup = y_inf + vals_i.shape[0]
            color = plt.cm.nipy_spectral(i / k)
            ax.fill_betweenx(np.arange(y_inf, y_sup), 0, vals_i, facecolor=color, edgecolor=color, alpha=0.7)
            ax.text(-0.05, y_inf + 0.5 * vals_i.shape[0], str(i))
            y_inf = y_sup + 10

        ax.axvline(x=promedio, color="red", linestyle="--")
        ax.set_title("Gráfico de silueta por grupo")
        ax.set_xlabel("Coeficiente de silueta")
        ax.set_ylabel("Grupo")
        ax.set_yticks([])
        ax.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])
        fig.suptitle(f"Análisis de silueta con K-Means: k = {k}, promedio = {promedio:.3f}",
                     fontsize=14, fontweight="bold")
    return puntajes


def plot_dendrogram(model, **kwargs) -> None:
    """Dibuja el dendrograma de un modelo ``AgglomerativeClustering`` ya ajustado.

    El modelo debe haberse creado con ``distance_threshold=0`` y ``n_clusters=None``
    para que exponga el atributo ``distances_``. Los ``kwargs`` se pasan a
    ``scipy.cluster.hierarchy.dendrogram``.
    """
    from scipy.cluster.hierarchy import dendrogram

    if not hasattr(model, "distances_"):
        raise ValueError("El modelo no tiene 'distances_': ajústalo con distance_threshold=0 y n_clusters=None.")

    n_muestras = len(model.labels_)
    conteos = np.zeros(model.children_.shape[0])
    for i, fusion in enumerate(model.children_):
        conteos[i] = sum(1 if hijo < n_muestras else conteos[hijo - n_muestras] for hijo in fusion)

    matriz_enlace = np.column_stack([model.children_, model.distances_, conteos]).astype(float)
    dendrogram(matriz_enlace, **kwargs)


# ---------------------------------------------------------------------------
# Datos atípicos
# ---------------------------------------------------------------------------
def identificar_outliers(
    df: pd.DataFrame,
    num_cols: Sequence[str],
    factor_iqr: float = 1.5,
    unicos: bool = False,
) -> List:
    """Identifica los índices de los valores atípicos con la regla del rango intercuartílico.

    Un valor es atípico si queda fuera de ``[Q1 - factor*IQR, Q3 + factor*IQR]``.

    Parameters
    ----------
    df : pd.DataFrame
        Datos.
    num_cols : list[str]
        Columnas numéricas a analizar.
    factor_iqr : float, default 1.5
        Multiplicador del rango intercuartílico.
    unicos : bool, default False
        Si es ``True`` devuelve cada índice una sola vez (una fila atípica en varias
        variables no se repite). Con ``False`` se conserva el comportamiento original.

    Returns
    -------
    list
        Índices de las filas atípicas.
    """
    _validar_columnas(df, num_cols)
    indices: List = []
    for var in num_cols:
        q1, q3 = df[var].quantile([0.25, 0.75])
        iqr = q3 - q1
        fuera = (df[var] < q1 - factor_iqr * iqr) | (df[var] > q3 + factor_iqr * iqr)
        indices.extend(df.index[fuera].tolist())
    return list(dict.fromkeys(indices)) if unicos else indices


# ---------------------------------------------------------------------------
# Evaluación de modelos de regresión
# ---------------------------------------------------------------------------
def _rmse(y_true, y_pred) -> float:
    """Raíz del error cuadrático medio (compatible con scikit-learn < 1.4)."""
    return float(np.sqrt(mean_squared_error(y_true, y_pred)))


def mean_absolute_scaled_error(y_true, y_pred, y_train, sp: int = 1) -> float:
    """Error absoluto medio escalado (MASE).

    Es el MAE del modelo dividido por el MAE de un pronóstico ingenuo (el valor anterior,
    o el de ``sp`` periodos atrás) calculado sobre ``y_train``. Un valor menor que 1
    indica que el modelo mejora al pronóstico ingenuo. Equivale a
    ``sktime.performance_metrics.forecasting.mean_absolute_scaled_error``.

    Parameters
    ----------
    y_true, y_pred : array-like
        Valores reales y predichos.
    y_train : array-like
        Serie (ordenada en el tiempo) usada para calcular la escala.
    sp : int, default 1
        Periodo estacional del pronóstico ingenuo.
    """
    serie = np.asarray(y_train, dtype=float)
    if sp < 1 or len(serie) <= sp:
        raise ValueError("y_train debe tener más de 'sp' observaciones.")
    escala = np.mean(np.abs(serie[sp:] - serie[:-sp]))
    if escala == 0:
        raise ValueError("La escala del MASE es 0: la serie y_train es constante.")
    return float(mean_absolute_error(y_true, y_pred) / escala)


def eval_model(model, X, y, y_escala=None, decimales: int = 5) -> Dict[str, float]:
    """Evalúa un modelo de regresión ya ajustado con MAE, RMSE, R² y MASE.

    Parameters
    ----------
    model : estimador
        Modelo con método ``predict``.
    X, y : array-like
        Características y valores reales del conjunto a evaluar (entrenamiento o prueba).
    y_escala : array-like, opcional
        Serie usada para escalar el MASE. Por defecto es ``y`` (comportamiento original);
        para evaluar el conjunto de prueba se recomienda pasar ``y_train``.
    decimales : int, default 5
        Redondeo de las métricas.

    Returns
    -------
    dict
        ``{"mae", "rmse", "r2", "mase"}``.
    """
    y_pred = model.predict(X)
    escala = y if y_escala is None else y_escala
    return {
        "mae": round(float(mean_absolute_error(y, y_pred)), decimales),
        "rmse": round(_rmse(y, y_pred), decimales),
        "r2": round(float(r2_score(y, y_pred)), decimales),
        "mase": round(mean_absolute_scaled_error(y, y_pred, y_train=escala), decimales),
    }


def search_param(
    base_model,
    X_train, y_train,
    X_test, y_test,
    base_params: Dict,
    parametro: str,
    search_range: Iterable,
    escala_mase_test: str = "test",
    verbose: bool = True,
) -> Tuple[Dict[str, List[float]], Dict[str, List[float]]]:
    """Evalúa un hiperparámetro variando su valor y mide R² y MASE en entrenamiento y prueba.

    En cada iteración se clona ``base_model`` y se le asignan ``base_params`` más el valor
    actual de ``parametro``; ni el modelo ni el diccionario ``base_params`` se modifican.

    Parameters
    ----------
    base_model : estimador
        Modelo base (se clona en cada iteración).
    X_train, y_train, X_test, y_test : array-like
        Conjuntos de entrenamiento y prueba.
    base_params : dict
        Hiperparámetros fijos.
    parametro : str
        Nombre del hiperparámetro a variar.
    search_range : iterable
        Valores a probar.
    escala_mase_test : {'test', 'train'}, default 'test'
        Serie que escala el MASE de prueba. ``'test'`` conserva el comportamiento original;
        ``'train'`` es la definición habitual del MASE.
    verbose : bool, default True
        Imprime el valor que se está ajustando.

    Returns
    -------
    (dict, dict)
        ``r2_scores`` y ``mase_scores``, cada uno con listas ``"train"`` y ``"test"``.
    """
    if escala_mase_test not in ("test", "train"):
        raise ValueError("escala_mase_test debe ser 'test' o 'train'.")
    escala_test = y_test if escala_mase_test == "test" else y_train

    r2 = {"train": [], "test": []}
    mase = {"train": [], "test": []}

    for valor in search_range:
        if verbose:
            print(f"Ajustando para {parametro}={valor}")
        modelo = clone(base_model).set_params(**{**base_params, parametro: valor})
        modelo.fit(X_train, y_train)
        pred_train, pred_test = modelo.predict(X_train), modelo.predict(X_test)

        r2["train"].append(r2_score(y_train, pred_train))
        r2["test"].append(r2_score(y_test, pred_test))
        mase["train"].append(mean_absolute_scaled_error(y_train, pred_train, y_train=y_train))
        mase["test"].append(mean_absolute_scaled_error(y_test, pred_test, y_train=escala_test))

    return r2, mase

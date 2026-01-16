# Proyecto 1: Visualización de Regresión con Manim

**Curso:** CS3061 Machine Learning  
**Universidad:** UTEC - Universidad de Ingeniería y Tecnología  
**Grupo:** 3
**Participantes:** Carlos Angel Oriundo
## 📝 Descripción

Este proyecto utiliza la biblioteca de animación matemática **Manim (Community Edition)** para demostrar visualmente los conceptos fundamentales de los modelos de regresión.

El objetivo es desmitificar la "caja negra" del aprendizaje automático, mostrando paso a paso las matemáticas detrás del ajuste de curvas, desde la regresión lineal simple hasta la regularización para evitar el *overfitting*.

### Temas Cubiertos en el Video
1.  **El Modelo Lineal General:** Introducción visual a Bias, Pesos y Características.
2.  **Regresión Lineal Univariable:** Visualización de la función de costo (MSE) y derivadas parciales.
3.  **Regresión Multivariable (Matrices):** Transición a notación matricial ($Y = XW$) y cálculo del gradiente vectorizado.
4.  **Regresión No Lineal (Polinómica):** Expansión de características ($Feature Expansion$) para ajustar datos curvos.
5.  **Regularización:** Visualización del problema de *Overfitting* y su solución mediante **Lasso (L1)**, **Ridge (L2)** y **ElasticNet**.

## 🛠️ Requisitos del Sistema (Software)

Para compilar y ejecutar este proyecto, necesitas tener instalado lo siguiente:

* **Python 3.8+**
* **FFmpeg:** Motor de renderizado de video (Requerido por Manim).
* **LaTeX (MiKTeX o TeX Live):** Necesario para renderizar las ecuaciones matemáticas complejas.

### Dependencias de Python
Las bibliotecas necesarias están listadas en `requirements.txt`:
* `manim`
* `numpy`

## 🚀 Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/first-ot-year/Proyecto1_Regresion.git](https://github.com/first-ot-year/Proyecto1_Regresion.git)
    cd Proyecto1_Regresion
    ```

2.  **Crear un entorno virtual (Opcional pero recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En Linux/Mac:
    source venv/bin/activate
    ```

3.  **Instalar dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

## 🎬 Cómo Compilar y Ejecutar

Para generar el video en alta calidad (1080p, 60fps), ejecuta el siguiente comando en tu terminal:

```bash
manim -pqh proyecto1_regresion.py ProyectoRegresionFinalCompleto




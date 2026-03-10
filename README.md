# Parcial 1 - Lenguajes de Programación
**Autor:** Julián David Cristancho Bustos  
**Programa:** Ciencias de la Computación e Inteligencia Artificial - Universidad Sergio Arboleda  

Este repositorio contiene la solución completa a los 5 puntos del parcial práctico. A continuación se detalla la estructura y cómo ejecutar cada punto.

## Estructura del Repositorio

### 📁 Punto 1 y 📁 Punto 2 (Autómatas Finitos Deterministas)
Implementación en Python puro de autómatas mediante matrices de transición (sin utilizar condicionales de flujo en la validación).
* **Ejecución:** `python3 Punto1/Punto1.py` y `python3 Punto2/Punto2.py`

### 📁 Punto 3 (Flex, Bison y C)
Calculadora capaz de resolver sumas, restas, multiplicaciones, divisiones y raíces cuadradas leyendo desde un archivo de texto. La raíz cuadrada no usa librerías nativas, sino el método numérico de Newton-Raphson.
* **Ejecución:** `./Punto3/calculadora Punto3/prueba.txt`

### 📁 Punto 4 (C vs Haskell)
Comparación de rendimiento del algoritmo recursivo de Euclides para calcular el Máximo Común Divisor (MCD) ejecutado 50 millones de veces.
* **Ejecución C:** `./Punto4/euclides_c`
* **Ejecución Haskell:** `./Punto4/euclides_hs`

### 📁 Punto 5 (ANTLR4 y Python)
Implementación de la serie de Maclaurin para aproximar la función exponencial $e^x$. Se desarrolló la gramática, se generó el árbol sintáctico (ATN) y se resolvió a través de un *Visitor* en Python3.
* **Ejecución:** `python3 Punto5/resolver.py` (Lanzará un prompt esperando una entrada como `calcular(2, 10)`).

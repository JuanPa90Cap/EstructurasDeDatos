# Estructuras de Datos en Python

Este repositorio contiene ejemplos de implementación de listas enlazadas simples, dobles, circulares, colas y pilas en Python. Además de los ejemplos de código, este documento proporciona una explicación detallada de cada estructura de datos, incluyendo gráficos y tablas comparativas.

## Contenido

- [Listas Enlazadas](#listas-enlazadas)
  - Listas Enlazadas Simples
  - Listas Doblemente Enlazadas
  - Listas Circulares
- [Colas](#colas)
  - Cola Simple
  - Cola Circular
- [Pilas](#pilas)
- [Comparación de Estructuras de Datos](#comparación-de-estructuras-de-datos)

## Listas Enlazadas

### ¿Qué son las Listas Enlazadas?

Las listas enlazadas son estructuras de datos lineales en las que los elementos están enlazados mediante nodos. Cada nodo contiene un valor y una referencia al siguiente nodo.

### 1. Lista Enlazada Simple

- **Definición**: Una lista enlazada simple contiene nodos donde cada nodo apunta al siguiente.
- **Uso Común**: Almacenamiento de datos dinámico donde el acceso secuencial es necesario.

#### Diagrama de Lista Enlazada Simple:

```
[10] -> [20] -> [30] -> None
```

#### Características:

| Operación         | Complejidad |
|-------------------|-------------|
| Inserción al inicio | O(1)        |
| Inserción al final  | O(n)        |
| Eliminación al inicio | O(1)      |
| Eliminación al final | O(n)      |
| Acceso aleatorio   | O(n)        |

### 2. Lista Doblemente Enlazada

- **Definición**: Cada nodo tiene un puntero al nodo siguiente y al anterior.
- **Uso Común**: Navegación bidireccional como en aplicaciones de backtracking o navegadores.

#### Diagrama de Lista Doblemente Enlazada:

```
None <- [1] <-> [2] <-> [3] -> None
```

#### Características:

| Operación             | Complejidad |
|-----------------------|-------------|
| Inserción al inicio   | O(1)        |
| Inserción al final    | O(1)        |
| Eliminación al inicio | O(1)        |
| Eliminación al final  | O(1)        |
| Acceso aleatorio      | O(n)        |

### 3. Lista Circular

- **Definición**: La última posición apunta al primer nodo, formando un ciclo.
- **Uso Común**: Implementaciones de juegos y algoritmos de buffer circular.

#### Diagrama de Lista Circular:

```
[5] -> [10] -> [15] -> (retorna a 5)
```

#### Características:

| Operación         | Complejidad |
|-------------------|-------------|
| Inserción         | O(n)        |
| Eliminación       | O(n)        |
| Acceso aleatorio  | O(n)        |

---

## Colas

### ¿Qué son las Colas?

Las colas son estructuras de datos que siguen el principio FIFO (First In, First Out), donde el primer elemento en ser añadido es el primero en ser eliminado.

### 1. Cola Simple

- **Definición**: Los elementos se añaden al final y se eliminan desde el frente.
- **Uso Común**: Sistemas de impresión, procesamiento de tareas en serie.

#### Diagrama de Cola Simple:

```
Front -> [1] -> [2] -> [3] -> Rear
```

#### Características:

| Operación    | Complejidad |
|--------------|-------------|
| Encolar      | O(1)        |
| Desencolar   | O(1)        |
| Acceso       | O(n)        |


## Pilas

### ¿Qué son las Pilas?

Las pilas son estructuras de datos que siguen el principio LIFO (Last In, First Out), donde el último elemento añadido es el primero en ser eliminado.

#### Diagrama de una Pila:

```
Top
 |
[V]
[W]
[X]
[Y]
[Z] <- Base
```

### Características:

| Operación     | Complejidad |
|---------------|-------------|
| Apilar        | O(1)        |
| Desapilar     | O(1)        |
| Acceso        | O(n)        |

---

## Comparación de Estructuras de Datos

| Estructura        | Inserción | Eliminación | Acceso aleatorio | Usos comunes                     |
|-------------------|-----------|-------------|------------------|----------------------------------|
| Lista Enlazada    | O(1)/O(n) | O(1)/O(n)   | O(n)             | Almacenamiento dinámico         |
| Lista Doble       | O(1)      | O(1)        | O(n)             | Navegación bidireccional        |
| Lista Circular    | O(n)      | O(n)        | O(n)             | Juegos, buffer circular         |
| Cola              | O(1)      | O(1)        | O(n)             | Procesamiento en serie          |
| Pila              | O(1)      | O(1)        | O(n)             | Recursividad, manejo de estados |

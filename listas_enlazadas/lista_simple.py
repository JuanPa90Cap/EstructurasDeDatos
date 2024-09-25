# Implementación de una Lista Enlazada Simple en Python

class Nodo:
    def __init__(self, dato):
        self.dato = dato  # Dato almacenado en el nodo
        self.siguiente = None  # Puntero al siguiente nodo

class ListaEnlazadaSimple:
    def __init__(self):
        self.cabeza = None  # Inicio de la lista

    def insertar(self, dato):
        """Inserta un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        """Muestra todos los elementos de la lista."""
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaEnlazadaSimple()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
lista.mostrar()  # Output: 10 -> 20 -> 30 -> None

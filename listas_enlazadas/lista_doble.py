# Implementación de una Lista Doblemente Enlazada en Python

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoble:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        """Inserta un nuevo nodo al final de la lista doble."""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = actual

    def mostrar(self):
        """Muestra los elementos de la lista de inicio a fin."""
        actual = self.cabeza
        while actual:
            print(actual.dato, end=" <-> ")
            actual = actual.siguiente
        print("None")

# Ejemplo de uso
lista = ListaDoble()
lista.insertar(1)
lista.insertar(2)
lista.insertar(3)
lista.mostrar()  # Output: 1 <-> 2 <-> 3 <-> None

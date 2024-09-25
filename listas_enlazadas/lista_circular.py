# Implementación de una Lista Enlazada Circular en Python

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def insertar(self, dato):
        """Inserta un nuevo nodo en la lista circular."""
        nuevo_nodo = Nodo(dato)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
        else:
            actual = self.cabeza
            while actual.siguiente != self.cabeza:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza

    def mostrar(self):
        """Muestra los elementos de la lista circular."""
        if not self.cabeza:
            return
        actual = self.cabeza
        while True:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
            if actual == self.cabeza:
                break
        print("CABEZA")

# Ejemplo de uso
lista = ListaCircular()
lista.insertar(5)
lista.insertar(10)
lista.insertar(15)
lista.mostrar()  # Output: 5 -> 10 -> 15 -> CABEZA

# Implementación de una Pila en Python

class Pila:
    def __init__(self):
        self.items = []

    def apilar(self, item):
        """Añade un elemento a la cima de la pila."""
        self.items.append(item)

    def desapilar(self):
        """Elimina y devuelve el elemento de la cima de la pila."""
        if not self.esta_vacia():
            return self.items.pop()

    def esta_vacia(self):
        """Verifica si la pila está vacía."""
        return len(self.items) == 0

    def mostrar(self):
        """Muestra los elementos de la pila."""
        print("Pila:", self.items)

# Ejemplo de uso
pila = Pila()
pila.apilar('a')
pila.apilar('b')
pila.desapilar()
pila.mostrar()  # Output: Pila: ['a']

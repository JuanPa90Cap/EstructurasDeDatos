# Implementación de una Cola en Python

class Cola:
    def __init__(self):
        self.items = []

    def encolar(self, item):
        """Añade un elemento al final de la cola."""
        self.items.append(item)

    def desencolar(self):
        """Elimina y devuelve el elemento del frente de la cola."""
        if not self.esta_vacia():
            return self.items.pop(0)

    def esta_vacia(self):
        """Verifica si la cola está vacía."""
        return len(self.items) == 0

    def mostrar(self):
        """Muestra los elementos de la cola."""
        print("Cola:", self.items)

# Ejemplo de uso
cola = Cola()
cola.encolar(1)
cola.encolar(2)
cola.desencolar()
cola.mostrar()  # Output: Cola: [2]

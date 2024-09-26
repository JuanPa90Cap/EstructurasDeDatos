#Ejercicio: Implementar una función que invierta el contenido de una cola.

def invertir(self):
        """Invierte la cola."""
        self.items = deque(reversed(self.items))


cola.invertir()
#Ejercicio : Implementar una función que cuente el número de nodos en una lista circular.

def contar_nodos(self):
        """Cuenta el número de nodos en la lista circular."""
        if not self.cabeza:
            return 0
        contador = 1
        actual = self.cabeza
        while actual.siguiente != self.cabeza:
            actual = actual.siguiente
            contador += 1
        return contador


# Ejemplo de uso
lista = ListaCircular()
lista.insertar(5)
lista.insertar(10)
lista.insertar(15)
print(lista.contar_nodos())  # Output: 3
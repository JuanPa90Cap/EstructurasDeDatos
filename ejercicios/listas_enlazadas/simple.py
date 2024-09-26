#Implementar una función que busque un valor específico en una lista enlazada simple.


def buscar(self, valor):
        """Busca un valor en la lista y retorna True si lo encuentra."""
        actual = self.cabeza
        while actual:
            if actual.dato == valor:
                return True
            actual = actual.siguiente
        return False



lista = ListaEnlazadaSimple()
lista.insertar(10)
lista.insertar(20)
lista.insertar(30)
print(lista.buscar(20))  # Output: True
print(lista.buscar(40))  # Output: False
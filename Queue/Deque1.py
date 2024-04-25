class Deque:
    def _init_(self):
        # Inicializacion de la clase Deque
        # Se crea una lista vacia para almacenar los elementos del Deque
        self.items = []

    def is_empty(self):
        # Metodo para verificar si el Deque esta vacio
        # Retorna True si el Deque esta vacio, False de lo contrario
        return len(self.items) == 0

    def add_first(self, element):
        # Metodo para agregar un elemento al principio del Deque
        # Se inserta el elemento en la posición 0 de la lista
        self.items.insert(0, element)

    def add_last(self, element):
        # Agregar un elemento al final del Deque
        # Se añade el elemento al final de la lista
        self.items.append(element)

    def delete_first(self):
        # Para eliminar y devolver el primer elemento del Deque
        if not self.is_empty():
            # Si el Deque no esta vacio, se elimina y devuelve el primer elemento de la lista
            return self.items.pop(0)
        else:
            # Si el Deque esta vacio, se lanza una excepcion IndexError
            raise IndexError("Deque is empty")

    def delete_last(self):
        # Metodo para eliminar y devolver el ultimo elemento del Deque
        if not self.is_empty():
            # Si el Deque no está vacio, se elimina y devuelve el ultimo elemento de la lista
            return self.items.pop()
        else:
            # Si el Deque esta vacio, se lanza una excepcion IndexError
            raise IndexError("Deque is empty")

    def first(self):
        # Metodo para obtener el primer elemento del Deque sin eliminarlo
        if not self.is_empty():
            # Si el Deque no esta vacio, se devuelve el primer elemento de la lista
            return self.items[0]
        else:
            # Si el Deque esta vacio, se lanza una excepción IndexError
            raise IndexError("Deque is empty")

    def last(self):
        # obtener el ultimo elemento del Deque sin eliminarlo
        if not self.is_empty():
            # Si el Deque no esta vacio, se devuelve el ultimo elemento de la lista
            return self.items[-1]
        else:
            # Si el Deque esta vacio, se lanza una excepcion IndexError
            raise IndexError("Deque is empty")

    def _len_(self):
        # Metodo especial para obtener la longitud del Deque utilizando la funcion len()
        return len(self.items)

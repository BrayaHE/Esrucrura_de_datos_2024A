''' Implementación de lista doblemente ligada '''
from node import Node

class DoubleLinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def isEmpty(self) -> bool:
        ''' Mostrar si la lista está vacía '''
        return self.counter == 0

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        new_node = Node(val)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
        self.counter += 1 
    
    def insertBetween(self, prev, val) -> None:
        ''' Insertar elemento entre dos nodos '''
        if not prev:
            print("Error Nodo no proporcionado")
        new_node = Node(val)
        new_node.prev = prev
        new_node.next = prev.next
        
        if prev.next:
            prev.next.prev = new_node
        else:
            self.tail = new_node
            
        prev.next = new_node
        self.counter += 1
        
    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        new_node = Node(val)
        if self.isEmpty():
            # Si está vacía, el nuevo nodo se convierte tanto en la cabeza como en la cola
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
        self.counter += 1
    
    def headDelete(self) -> None:
        ''' Eliminar el primer elemento de la lista '''
        if self.isEmpty():
            print("La lista está vacía, no se puede eliminar.")
            return
        
        if self.counter == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.counter -= 1 
    
    def tailDelete(self) -> None:
        ''' Eliminar el último elemento de la lista '''
        if self.isEmpty():
            print("La lista está vacía, no se puede eliminar.")
            return
        if self.counter == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        self.counter -= 1 

    def deleteBetween(self, val) -> None:
        ''' Eliminar elemento entre dos nodos '''
        current = self.head
        while current:
            if current.val == val:
                if current.prev:
                    current.prev.next = current.next
                else:
                     self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    # Si no hay un nodo siguiente, significa que es la cola, entonces actualiza la cola
                    self.tail = current.prev
                self.counter -= 1
                return
            current = current.next
        print(f"No se encontró el valor {val} en la lista.")
        
    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        current = self.head
        while current:
            print(current)
            current = current.next

if __name__ == '__main__':
    lista_doblemente_ligada = DoubleLinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

   # Llenado de la lista
    for item in lista_tradicional:
        lista_doblemente_ligada.tailInsert(item)

    # Impresión de la lista
    print('Impresión #1 -> Llenado de lista')
    lista_doblemente_ligada.traverse()

    # Adición de un nuevo elemento al final
    print('\nImpresión #2 -> Nuevo elemento al final')
    n = False
    lista_doblemente_ligada.tailInsert(n)
    lista_doblemente_ligada.traverse()

    # Adición de un nuevo elemento al inicio
    print('\nImpresión #3 -> Nuevo elemento al inicio')
    n = 'Estructuras'
    lista_doblemente_ligada.headInsert(n)
    lista_doblemente_ligada.traverse()

    # Adición de elemento entre dos nodos
    print('\nImpresión #4 -> Nuevo elemento entre dos nodos')
    prev, n = lista_doblemente_ligada.head, False  
    lista_doblemente_ligada.insertBetween(prev, n)
    lista_doblemente_ligada.traverse()

    # Eliminación del primer elemento e impresión
    print('\nImpresión #5 -> Eliminación del primer elemento')
    lista_doblemente_ligada.headDelete()
    lista_doblemente_ligada.traverse()
    
    # Eliminación del último elemento e impresión
    print('\nImpresión #6 -> Eliminación del último elemento')
    lista_doblemente_ligada.tailDelete()
    lista_doblemente_ligada.traverse()
    
    # Eliminación del primer elemento e impresión
    print('\nImpresión #7 -> Eliminación de elemento en la lista')
    n = 3
    lista_doblemente_ligada.deleteBetween(n)
    lista_doblemente_ligada.traverse()






















# '''Codigo comentado'''
# ''' Implementación de nodo versátil para listas doblemente ligadas '''
# ''' Implementación de nodo versátil para listas doblemente ligadas '''

# # Definición de la clase Node, que representa un nodo en la lista
# class Node:
#     def __init__(self, val=None):
#         ''' Inicializador '''
#         self.val = val          # Valor del nodo
#         self.next = None         # Referencia al siguiente nodo
#         self.prev = None         # Referencia al nodo anterior

#     def __str__(self) -> str:
#         return f'Nodo con valor {self.val}\nAnterior {self.prev}\nSiguiente {self.next}'

# ''' Implementación de lista doblemente ligada '''

# # Importar la clase Node desde el archivo node.py
# from node import Node

# # Definición de la clase DoubleLinkedList, que representa la lista doblemente ligada
# class DoubleLinkedList:
#     def __init__(self) -> None:
#         ''' Inicializador '''
#         self.counter:int = 0     # Contador de elementos en la lista
#         self.head:Node|None = None  # Referencia al primer nodo de la lista
#         self.tail:Node|None = None  # Referencia al último nodo de la lista

#     def isEmpty(self) -> bool:
#         ''' Mostrar si la lista está vacía '''
#         return self.counter == 0

#     def headInsert(self, val) -> None:
#         ''' Insertar elemento al inicio de la lista '''
#         new_node = Node(val)     # Crear un nuevo nodo con el valor dado
#         if self.isEmpty():
#             # Si la lista está vacía, el nuevo nodo se convierte tanto en la cabeza como en la cola
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # Si la lista no está vacía, ajustar las referencias para insertar el nuevo nodo al inicio
#             new_node.next = self.head
#             self.head.prev = new_node
#             self.head = new_node
#         self.counter += 1  # Incrementar el contador de elementos

#     def insertBetween(self, prev, val) -> None:
#         ''' Insertar elemento entre dos nodos '''
#         if not prev:
#             print("Error: Nodo previo no proporcionado.")
#             return

#         new_node = Node(val)   # Crear un nuevo nodo con el valor dado
#         new_node.prev = prev
#         new_node.next = prev.next

#         if prev.next:
#             prev.next.prev = new_node
#         else:
#             self.tail = new_node

#         prev.next = new_node
#         self.counter += 1

#     def tailInsert(self, val) -> None:
#         ''' Insertar elemento al final de la lista '''
#         new_node = Node(val)    # Crear un nuevo nodo con el valor dado
#         if self.isEmpty():
#             # Si la lista está vacía, el nuevo nodo se convierte tanto en la cabeza como en la cola
#             self.head = new_node
#             self.tail = new_node
#         else:
#             # Si la lista no está vacía, ajustar las referencias para insertar el nuevo nodo al final
#             new_node.prev = self.tail
#             self.tail.next = new_node
#             self.tail = new_node
#         self.counter += 1

#     def headDelete(self) -> None:
#         ''' Eliminar el primer elemento de la lista '''
#         if self.isEmpty():
#             print("La lista está vacía, no se puede eliminar.")
#             return

#         if self.counter == 1:
#             # Si hay un solo elemento, vaciar la lista
#             self.head = None
#             self.tail = None
#         else:
#             # Si hay más de un elemento, ajustar las referencias para eliminar el primer nodo
#             self.head = self.head.next
#             self.head.prev = None

#         self.counter -= 1

#     def tailDelete(self) -> None:
#         ''' Eliminar el último elemento de la lista '''
#         if self.isEmpty():
#             print("La lista está vacía, no se puede eliminar.")
#             return

#         if self.counter == 1:
#             # Si hay un solo elemento, vaciar la lista
#             self.head = None
#             self.tail = None
#         else:
#             # Si hay más de un elemento, ajustar las referencias para eliminar el último nodo
#             self.tail = self.tail.prev
#             self.tail.next = None

#         self.counter -= 1

#     def deleteBetween(self, val) -> None:
#         ''' Eliminar elemento entre dos nodos '''
#         current = self.head
#         while current:
#             if current.val == val:
#                 # Si se encuentra el valor, ajustar las referencias para eliminar el nodo correspondiente
#                 if current.prev:
#                     current.prev.next = current.next
#                 else:
#                     self.head = current.next

#                 if current.next:
#                     current.next.prev = current.prev
#                 else:
#                     self.tail = current.prev

#                 self.counter -= 1
#                 return
#             current = current.next

#         print(f"No se encontró el valor {val} en la lista.")

#     def traverse(self) -> None:
#         ''' Recorrer la lista (imprimir) '''
#         current = self.head
#         while current:
#             print(current)
#             current = current.next

# if __name__ == '__main__':
#     # Bloque de código que se ejecuta solo si el script se ejecuta directamente y no se importa como módulo

#     # Crear una instancia de la clase DoubleLinkedList
#     lista_doblemente_ligada = DoubleLinkedList()

#     # Generar casos de prueba con la siguiente lista
#     lista_tradicional = [1, 2, -212, True, 'UNE', 3]

#     # Llenado de la lista utilizando el método tailInsert para insertar elementos al final
#     for item in lista_tradicional:
#         lista_doblemente_ligada.tailInsert(item)

#     # Impresión de la lista después del llenado
#     print('Impresión #1 -> Llenado de lista')
#     lista_doblemente_ligada.traverse()

#     # Adición de un nuevo elemento al final utilizando el método tailInsert
#     print('\nImpresión #2 -> Nuevo elemento al final')
#     n = False
#     lista_doblemente_ligada.tailInsert(n)
#     lista_doblemente_ligada.traverse()

#     # Adición de un nuevo elemento al inicio utilizando el método headInsert
#     print('\nImpresión #3 -> Nuevo elemento al inicio')
#     n = 'Estructuras'
#     lista_doblemente_ligada.headInsert(n)
#     lista_doblemente_ligada.traverse()

#     # Adición de un elemento entre dos nodos utilizando el método insertBetween
#     print('\nImpresión #4 -> Nuevo elemento entre dos nodos')
#     prev, n = lista_doblemente_ligada.head, False  
#     lista_doblemente_ligada.insertBetween(prev, n)
#     lista_doblemente_ligada.traverse()

#     # Eliminación del primer elemento e impresión utilizando el método headDelete
#     print('\nImpresión #5 -> Eliminación del primer elemento')
#     lista_doblemente_ligada.headDelete()
#     lista_doblemente_ligada.traverse()
    
#     # Eliminación del último elemento e impresión utilizando el método tailDelete
#     print('\nImpresión #6 -> Eliminación del último elemento')
#     lista_doblemente_ligada.tailDelete()
#     lista_doblemente_ligada.traverse()
    
#     # Eliminación de un elemento en la lista utilizando el método deleteBetween
#     print('\nImpresión #7 -> Eliminación de elemento en la lista')
#     n = 3
#     lista_doblemente_ligada.deleteBetween(n)
#     lista_doblemente_ligada.traverse()


''' Implementación de lista ligada '''
from node import Node

class LinkedList:
    def __init__(self) -> None:
        ''' Inicializador '''  
        self.counter:int = 0
        self.head:Node|None = None
        self.tail:Node|None = None

    def headInsert(self, val) -> None:
        ''' Insertar elemento al inicio de la lista '''
        nuevo_nodo = Node(val)
        nuevo_nodo.next = self.head
        self.head = nuevo_nodo
        
        if (not self.counter):
            self.tail = self.head
        
        self.counter += 1
        
    def tailInsert(self, val) -> None:
        ''' Insertar elemento al final de la lista '''
        if self.tail == None:
            self.headInsert(val)
            self.tail = self.head
            return
        self.tail.next = Node(val)
        self.tail = self.tail.next
        self.counter +=1
    # '''+1'''
    
    def headRemove(self) -> None:
        ''' Remover el elemento al inicio de la lista '''
        if self.head is None:
            raise ValueError("La lista esta vacia")
        
        self.head = self.head.next
        if self.head is None:
            self.tail = None
            
        self.counter -= 1
        
    '''-1'''
    def traverse(self) -> None:
        ''' Recorrer la lista (imprimir) '''
        if not self.head:
            print("La lista esta vacia")
            return
        
        nuevo_nodo = self.head
        cnt= 1
        
        while nuevo_nodo is not None:
            print(f'Nodo #{cnt} -> {nuevo_nodo.val}')
            nuevo_nodo = nuevo_nodo.next
            cnt += 1
    
if __name__ == '__main__':
    lista_ligada = LinkedList()

    # Genera tus casos de prueba con la siguiente lista
    lista_tradicional = [1, 2, -212, True, 'UNE', 3]

    # Llenado de la lista
    
    for i in lista_tradicional:
        lista_ligada.tailInsert(i)
   
    # Impresión de la lista
    print('Impresión #1')
    lista_ligada.traverse()    

    # Adición de un nuevo elemento al final
    print('\nImpresión #2')
    n = False
    lista_ligada.tailInsert(n)
    lista_ligada.traverse()

    # Adición de un nuevo elemento al inicio
    print('\nImpresión #3')
    n = 'Estructuras'
    lista_ligada.headInsert(n)
    lista_ligada.traverse()

    # Eliminación del primer elemento e impresión
    print('\nImpresión #4')
    lista_ligada.headRemove()
    lista_ligada.traverse()
 
    # Eliminación del último elemento (o explica por qué no es posible en un comentario multilínea)
    '''
    Solo se puede eliminar el ultimo elemento si la lista ligada es doblemente ligada, es decir, cada nodo tiene una referencia al nodo anterior y al siguiente. 
    Si la lista ligada es simplemente ligada, cada nodo solo tiene una referencia al siguiente nodo.
    '''
    
    
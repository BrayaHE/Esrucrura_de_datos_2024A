''' Implementación de nodo versátil para listas doblemente ligadas '''

# class Node:
#     def __init__(self, val = None):
#         ''' Inicializador '''
#         self.val = val
#         self.next = None
#         self.prev = None

#     def __str__(self) -> str:
#         return f'Nodo con valor {self.val}\nAnterior {self.prev}\nSiguiente {self.next}'
class Node:
    def __init__(self, val=None):
        ''' Inicializador '''
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f'Nodo con valor {self.val}'
    
    
    
    
    
    
    
    
    
    
    
    
    '''Codigo comentado'''
    # class Node:
    # def __init__(self, val=None):
    #     ''' Inicializador '''
    #     # Constructor de la clase Node que inicializa un nodo con un valor dado
    #     self.val = val  # Asignar el valor proporcionado al atributo 'val' del nodo
    #     self.next = None  # Inicializar el puntero al siguiente nodo como None (vacío)
    #     self.prev = None  # Inicializar el puntero al nodo anterior como None (vacío)

    # def __str__(self) -> str:
    #     # Método especial para representar el nodo como una cadena
    #     return f'Nodo con valor {self.val}'
    #     # Devuelve una cadena que indica que es un nodo y muestra su valor

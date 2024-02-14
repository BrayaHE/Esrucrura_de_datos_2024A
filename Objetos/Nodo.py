''' Modulo de contenedor de clase Nodo para listas ligadas '''

class Nodo:
    '''Creacion de Nodo'''

    def __init__(self, val: int = None):
        '''Inicializacion de clase'''
        self.val = val
        self.next = None

    def __str__(self) -> str:
        if self.val:
            return f'Valor del Nodo = {self.val}'
        return f'El nodo no tiene valor'

# '''Lista doblemente ligadas'''


# '''modulo contenedor de clase '''

# class nodo:
#     def _init_(self,  val:int = None ):
#         '''iniciliciador de clase'''
        
#         self.val = val
#         self.nextn = None 

#         def _str_(self)-> str :
#             if self.val:
#                 return f'valor de nodo = {self.val}:'
#                 return f' el nodo no tiene valor'








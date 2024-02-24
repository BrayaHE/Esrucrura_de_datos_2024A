''' Implementación de lista dinámica '''
from __future__ import annotations
import ctypes

'''
    Considerar el caso de múltiples remociones

    Decrementar el tamaño del arreglo a la mitad
    cada que la cantidad de elementos en el arreglo
    sea 1/4 de la capacidad actual
'''

class ListaDinamica:
    def __init__(self) -> None:
        ''' Inicializar un arreglo vacío '''
        self.__n = 0                          # Elementos actuales
        self.__c = 1                          # Capacidad inicial por defecto
        self.__A = self.__init_arr(self.__c)  # Arreglo contenedor
    
    def __Check_resize(decrease_func):
        ''' Decorador para revisar relación elementos/capacidad '''
        def inner(self, *args):
            val = decrease_func(self, *args)

            ''' Manejar resize aquí '''
            
            return val

        return inner

    def __len__(self) -> int:
        ''' Regresa la cantidad de elementos almacenados en la lista '''
        return self.__n

    def __getitem__(self, k) -> object:
        ''' Regresa un elemento en una posición k '''
        if k < 0:
            if abs(k) > self.__n:
                raise IndexError(f'Índice inválido ({k})')
            k = self.__n + k
        elif k >= self.__n:
            raise IndexError(f'Índice inválido ({k})')
        
        return self.__A[k]
    
    def __contains__(self, obj) -> bool:
        ''' Revisa si la lista contiene a un objeto '''
    
    def __eq__(self, l:ListaDinamica) -> bool:
        ''' Revisa si dos listas son iguales '''
    
    def __ne__(self, l:ListaDinamica) -> bool:
        ''' Revisa si dos listas no son iguales '''
    
    @__Check_resize
    def __delitem__(self, k) -> None:
        ''' Elimina un elemento de la lista '''

    def __add__(self, l:ListaDinamica) -> ListaDinamica:
        ''' Agrega elementos al final de la lista y retorna una nueva '''
    
    def __iadd__(self, l:ListaDinamica) -> ListaDinamica:
        ''' Agrega elementos al final de la lista (in-place) '''
    
    def __str__(self) -> str:
        ''' Retorna la representación en cadena de la lista '''

    def append(self, obj) -> None:
        ''' Añade un elemento al final de la lista '''
        if self.__n == self.__c:
            self.__resize(2 * self.__c)
        
        self.__A[self.__n] = obj
        self.__n += 1
    
    def count(self, obj) -> None:
        ''' Cuenta las instancias de un objeto dentro de la lista '''
    
    def index(self, obj) -> int:
        ''' Regresa la posición de la primera instancia de un
        objeto en una lista '''

    def insert(self, k, obj) -> None:
        ''' Inserta un objeto en la posición k de la lista '''
    
    @__Check_resize
    def pop(self, k=None) -> object:
        ''' Retorna el elemento k de una lista y lo elimina de la misma '''

    def remove(self, obj) -> None:
        ''' Elimina la primera instancia de un objeto en la lista 
        Nota: depende de la implementación de == de cada elemento '''

    def extend(self, l:ListaDinamica) -> None:
        ''' Agrega elementos al final de la lista '''

    def reverse(self) -> None:
        ''' Invierte los elementos de la lista '''
    
    def sort(self) -> None:
        ''' Ordena los elementos de la lista en forma ascendente (InsertionSort)'''

    def __resize(self, c) -> None:
        ''' Modifica el tamaño de la lista interna '''
        B = self.__init_arr(c)

        for k in range(self.__n):
            B[k] = self.__A[k]

        self.__A = B
        self.__c = c

    def __init_arr(self, capacidad):
        ''' Regresa un nuevo arreglo con capacidad determinada '''
        return (capacidad * ctypes.py_object)()     # Magia

if __name__ == '__main__':
    ''' Pruebas de la clase '''

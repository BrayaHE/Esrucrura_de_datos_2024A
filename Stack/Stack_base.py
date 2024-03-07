''' Implementación de Stack (Pila) '''
from ListaDinamica import ListaDinamica

class EmptyStack(Exception):
    ''' Error personalizado para stack vacío '''

class Stack:
    ''' Clase implementadora de stack '''

    def __init__(self) -> None:
        self.__S = ListaDinamica()
    
    def __len__(self) -> int:
        ''' Regresa el número de elementos dentro del stack '''
        return len(self.__S)
    def __str__(self) -> str:
        return str(self.__S)

    def is_empty(self) -> bool:
        ''' Indica si el stack está vacío '''
        return len(self) == 0
    
    def push(self, e) -> None:
        ''' Agregar un elemento al stack '''
        self.__S.append(e)

    def top(self) -> object:
        ''' Regresa el elemento hasta el tope del stack sin eliminarlo '''
        if self.is_empty():
            raise EmptyStack("No se puede obtener el tope de un stack vacío")
        return self.__S[-1]

    def pop(self) -> object:
        ''' Elimina el elemento hasta el tope del stack y lo regresa '''
        if self.is_empty():
            raise EmptyStack("No se puede hacer pop en un stack vacío")
        return self.__S.pop()
    
if __name__ == '__main__':
    ''' Pruebas de la implementación '''
    
    S = Stack()
    secuencia= [1, 2, 3, 'A', 'B', False, True]
    
    for elem in secuencia:
        s.push(elem)
    
    print(f'Stack resultante > (s)')
    print(f'LEl stack está vacio? -> {"si" if S.is_empty() else "no"}')
    print(f'Elemento hasta arriba -> {s.top()}')
    print(f'Longitud original -> {len(s)}')
    print(f'Eliminación del elemento hasta arriba -> {s.pop()}')
    print(f'Nueva longitud -> {len(s)}')
    print(f'Nueva Representacion -> {S}\n')
    
    s_empty =Stack()
    print(f'Stack resultante -> {s_empty}')
    print(f'Longitud del segundo stack -> {len(s_empty)}')
    
    try:
        print(f'Elemento hasta arriba -> {s_empty.pop()}')
    except EmptyStack as e:
        print(f'El stack está vacio ({e}) ({e}) ({e}) (Creo que el stack está vacio))))')
    except:
        print('Un error inesperado ocurrió...')
    
  
    
  
    

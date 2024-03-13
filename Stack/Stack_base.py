''' Implementación de Stack (Pila) '''
from ListaDinamica import ListaDinamica

class EmptyStack(Exception):
    ''' Error personalizado para stack vacío '''

class Stack:
    ''' Clase implementadora de stack '''

    def __init__(self) -> None:
        self.__data = ListaDinamica()
    
    def __len__(self) -> int:
        ''' Regresa el número de elementos dentro del stack '''
        return len(self.__data)
    
    def __str__(self) -> str:
        return str(self.__data)

    def is_empty(self) -> bool:
        ''' Indica si el stack está vacío '''
        return self.__len__() == 0
    
    def push(self, e) -> None:
        ''' Agregar un elemento al stack '''
        self.__data.append(e)

    def top(self) -> object:
        ''' Regresa el elemento hasta el tope del stack sin eliminarlo '''
        if self.is_empty():
            raise EmptyStack('El stack está vacío')
        
        return self.__data[-1]

    def pop(self) -> object:
        ''' Elimina el elemento hasta el tope del stack y lo regresa '''
        if self.is_empty():
            raise EmptyStack('El stack está vacío')
        
        return self.__data.pop()

if __name__ == '__main__':
    s = Stack()

    secuencia = [1, 2, 3, 'A', 'B', False, True]

    for elem in secuencia:
        s.push(elem)

    print(f'Stack resultante -> {s}')
    print(f'¿El stack está vacío? -> {"SÍ" if s.is_empty() else "NO"}')
    print(f'Elemento hasta arriba -> {s.top()}')
    print(f'Longitud original -> {len(s)}')
    print(f'Eliminación del elemento hasta arriba -> {s.pop()}')
    print(f'Nueva longitud -> {len(s)}')
    print(f'Nueva representación -> {s}\n')

    s_empty = Stack()
    print(f'Stack resultante -> {s_empty}')
    print(f'Longitud del segundo stack -> {len(s_empty)}')
    
    try:
        print(f'Elemento hasta arriba -> {s_empty.pop()}')
    except EmptyStack as e:
        print(f'El stack está vacío ({e} ({e} ({e} (Creo que el stack está vacío))))')
    except:
        print('Un error inesperado ocurrió...')
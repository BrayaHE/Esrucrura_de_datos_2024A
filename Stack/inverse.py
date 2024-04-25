# Importa la clase ListaDinamica desde el módulo ListaDinamica
from ListaDinamica import ListaDinamica

# Define una excepción personalizada para cuando el stack esté vacío
class EmptyStack(Exception):
    ''' Error personalizado para stack vacío '''

# Define la clase Stack para implementar una estructura de datos de pila
class Stack:
    ''' Clase implementadora de stack '''

    def __init__(self) -> None:
        # Inicializa la pila utilizando una ListaDinamica
        self.__data = ListaDinamica()
    
    def __len__(self) -> int:
        ''' Regresa el numero de elementos dentro del stack '''
        return len(self.__data)
    
    def __str__(self) -> str:
        # Representación en cadena del contenido de la pila
        return str(self.__data)

    def is_empty(self) -> bool:
        ''' Indica si el stack esta vacio '''
        return self.__len__() == 0
    
    def push(self, e) -> None:
        ''' Agregar un elemento al stack '''
        # Agrega un elemento a la parte superior de la pila
        self.__data.append(e)

    def top(self) -> object:
        ''' Regresa el elemento hasta el tope del stack sin eliminarlo '''
        # Regresa el elemento en la parte superior de la pila
        if self.is_empty():
            raise EmptyStack('El stack esta vacio')
        
        return self.__data[-1]

    def pop(self) -> object:
        ''' Elimina el elemento hasta el tope del stack y lo regresa '''
        # Elimina y regresa el elemento en la parte superior de la pila
        if self.is_empty():
            raise EmptyStack('El stack está vacío')
        
        return self.__data.pop()

# Funcion para verificar si una cadena está balanceada con parentesis, llaves y corchetes
def balanceada(s: str) -> bool:
    # Crea una instancia de la clase Stack
    stack = Stack()
    # Define los caracteres de apertura y cierre para parentesis, llaves y corchetes
    abre = "({["
    cierra = ")}]"
    # Itera sobre cada caracter en la cadena s
    for char in s:
        # Si el caracter es de apertura, lo agrega al stack
        if char in abre:
            stack.push(char)
        # Si el caracter es de cierre
        elif char in cierra:
            # Si el stack está vacio, la cadena está desbalanceada
            if stack.is_empty():
                return False
            # Si el ultimo carácter abierto en el stack no coincide con el tipo de cierre, la cadena esta desbalanceada
            if abre.index(stack.pop()) != cierra.index(char):
                return False
    # Si el stack esta vacío al final, la cadena esta balanceada
    return stack.is_empty()

# Casos de prueba
test_cases = [
    "(6a*89 - [7x+2] / {25z - 33.4p})",
    "[12+1+(84-23*[54d])}",
    "()",
    ")(",
    "(((((((()))))))",
    "[{({)})]",
    "Hola",
    "",
    "[e,s,t,r,u,c,t,u,r,a,(d,e[da,to,s])]"
]

# Itera sobre cada caso de prueba e imprime si esta correcto o incorrecto
for case in test_cases:
    print(f"{case} -> {'Correcta' if balanceada(case) else 'Incorrecta'}")




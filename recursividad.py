#Usamos la palabra reservada def para definir la secuencia de fibonacci y entre parentesis una variable llamada "n" para hacer la sucesion hasta el enecimo termino.
def fibonacci(n):
     #Con la sentencia if hacemos una condicion si el valor en la variable "n" es menor o igual a 0. 
    if n <= 0:
         #Con la funcion return retornamos la seuencia del if en una lista vacia.
         return []
     #Con la sentencia else if hacemos una condicion donde indicamos si el valor de n es igual a 1. 
    elif n == 1:
        #Con la funcion return retornamos una lista con el primer término de la sucesión de Fibonacci que es 0. 
        return [0]
     #Con la sentencia else if hacemos una condicion si el valor n es igual a 2. 
    elif n == 2:
         #Con la funcion return retornamos una lista con los primeros dos terminos de la sucesion de Fibonacci, que son 0 y 1.
         return [0, 1]
     #Con la sentencia else realicamos otra condicion donde si n es mayor que 2 primero genera la sucesión de Fibonacci 
    else:
         #Creamos con un nombre para hacer el formato de la lista para definir la secuensia fibonacci para genera la sucesión hasta que el (n-1) enecimo término.
         fi_lista = fibonacci(n-1) 
         #Usamos el comando append para agregar el elemento final de la lista para hacer la sucesion de fibonacci
         fi_lista.append(fi_lista[-1] + fi_lista[-2])
         #Con la funcion return  retornamos la secuencia en la lista
         return fi_lista
#Usamos el comando print para que imprima la sucecion fibonacci dentro de la lista 
print(fibonacci(30))


# 
'''Otro metodo'''
# import tkinter as tk

# class Nodo:
#     def __init__(self, valor):
#         self.valor = valor
#         self.izquierda = None
#         self.derecha = None

# class ArbolBinarioVisual:
#     def __init__(self, master, lista_numeros, numero_a_buscar):
#         self.master = master
#         self.numero_a_buscar = numero_a_buscar
#         self.resultado_label = tk.Label(master, text="")
#         self.resultado_label.pack()

#         self.raiz = self.construir_arbol(lista_numeros)
#         self.buscar_numero(self.raiz)

#     def construir_arbol(self, lista_numeros):
#         raiz = None
#         for numero in lista_numeros:
#             raiz = self.insertar(raiz, numero)
#         return raiz

#     def insertar(self, raiz, valor):
#         if raiz is None:
#             return Nodo(valor)
#         if valor < raiz.valor:
#             raiz.izquierda = self.insertar(raiz.izquierda, valor)
#         else:
#             raiz.derecha = self.insertar(raiz.derecha, valor)
#         return raiz

#     def buscar_numero(self, raiz):
#         if raiz is None:
#             self.resultado_label.config(text=f"{self.numero_a_buscar} no encontrado en el árbol.")
#             return
#         if raiz.valor == self.numero_a_buscar:
#             self.resultado_label.config(text=f"{self.numero_a_buscar} encontrado en el árbol.")
#             return
#         elif self.numero_a_buscar < raiz.valor:
#             self.resultado_label.config(text=f"Buscando en la rama izquierda: {raiz.valor}.")
#             self.master.after(1000, self.buscar_numero, raiz.izquierda)
#         else:
#             self.resultado_label.config(text=f"Buscando en la rama derecha: {raiz.valor}.")
#             self.master.after(1000, self.buscar_numero, raiz.derecha)

# def main():
#     lista_numeros = [10, 5, 15, 3, 7, 12, 18]  # Lista de números para construir el árbol
#     numero_a_buscar = 12

#     root = tk.Tk()
#     root.title("Búsqueda Binaria en Árbol Visual")
#     root.geometry("400x100")

#     app = ArbolBinarioVisual(root, lista_numeros, numero_a_buscar)

#     root.mainloop()

# if __name__ == "__main__":
#     main()

'''Metodo 3'''
import tkinter as tk
import time

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinarioVisual:
    def __init__(self, master, lista_numeros, numero_a_buscar):
        self.master = master
        self.numero_a_buscar = numero_a_buscar
        self.resultado_label = tk.Label(master, text="")
        self.resultado_label.pack()

        self.raiz = self.construir_arbol(lista_numeros)
        self.arbol_canvas = tk.Canvas(master, width=800, height=400)
        self.arbol_canvas.pack()
        self.dibujar_arbol(self.raiz, 400, 50, 200)

    def construir_arbol(self, lista_numeros):
        raiz = None
        for numero in lista_numeros:
            raiz = self.insertar(raiz, numero)
        return raiz

    def insertar(self, raiz, valor):
        if raiz is None:
            return Nodo(valor)
        if valor < raiz.valor:
            raiz.izquierda = self.insertar(raiz.izquierda, valor)
        else:
            raiz.derecha = self.insertar(raiz.derecha, valor)
        return raiz

    def dibujar_arbol(self, raiz, x, y, espacio):
        if raiz is not None:
            self.arbol_canvas.create_oval(x-20, y-20, x+20, y+20, fill="white")
            self.arbol_canvas.create_text(x, y, text=str(raiz.valor))
            if raiz.izquierda is not None:
                self.arbol_canvas.create_line(x, y, x - espacio, y + 50, width=2)
                self.dibujar_arbol(raiz.izquierda, x - espacio, y + 50, espacio // 2)
            if raiz.derecha is not None:
                self.arbol_canvas.create_line(x, y, x + espacio, y + 50, width=2)
                self.dibujar_arbol(raiz.derecha, x + espacio, y + 50, espacio // 2)

    def buscar_numero(self, raiz):
        if raiz is None:
            self.resultado_label.config(text=f"{self.numero_a_buscar} no encontrado en el árbol.")
            return
        if raiz.valor == self.numero_a_buscar:
            self.resultado_label.config(text=f"{self.numero_a_buscar} encontrado en el árbol.")
            return
        elif self.numero_a_buscar < raiz.valor:
            self.resultado_label.config(text=f"Buscando en la rama izquierda: {raiz.valor}.")
            self.master.after(1000, self.buscar_numero, raiz.izquierda)
        else:
            self.resultado_label.config(text=f"Buscando en la rama derecha: {raiz.valor}.")
            self.master.after(1000, self.buscar_numero, raiz.derecha)

def main():
    lista_numeros = [10, 5, 15, 3, 7, 12, 18]  # Lista de números para construir el árbol
    numero_a_buscar = 12

    root = tk.Tk()
    root.title("Visualización de Búsqueda Binaria y Árbol Binario")
    root.geometry("800x450")

    app = ArbolBinarioVisual(root, lista_numeros, numero_a_buscar)
    app.buscar_numero(app.raiz)

    root.mainloop()

if __name__ == "__main__":
    main()

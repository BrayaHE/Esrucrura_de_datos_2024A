import tkinter as tk

class MiVentana:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Ventana")
        
        # Crear un label
        self.label = tk.Label(root, text="¡Hola Mundo!")
        self.label.pack(pady=10, padx=10)
        
        # Crear un botón
        self.button = tk.Button(root, text="Click Me", command=self.saludar)
        self.button.pack(pady=5, padx=5)
        
    def saludar(self):
        print("¡Hola! Has hecho clic en el botón.")

def main():
    root = tk.Tk()
    app = MiVentana(root)
    root.mainloop()

if __name__ == "__main__":
    main()

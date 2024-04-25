import turtle

def dibujar_flor():
    window = turtle.Screen()
    window.bgcolor("black")  # Cambiado a negro

    flor = turtle.Turtle()
    flor.shape("turtle")
    flor.speed(10)

    flor.color("yellow")

    for _ in range(36):
        dibujar_petalos(flor)
        flor.right(10)

    flor.right(90)
    flor.forward(200)

    window.exitonclick()

def dibujar_petalos(turtle):
    for _ in range(2):
        turtle.forward(100)
        turtle.right(60)
        turtle.forward(100)
        turtle.right(120)

dibujar_flor()
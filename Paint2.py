"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *
from freegames import vector   

def info_alumno():
    t = Turtle()
    t.up()
    t.goto(0,190)
    t.color("blue")
    t.write("César Antonio Martínez Vilchis A01236306", align='left', font=('Arial',10,'normal'))
    t.goto(0,170)
    t.color("black")
    t.write("Oscar Ariel Ortega Franco A00833051", align='left', font=('Arial',10,'normal'))
    t.goto(0,150)
    t.color("red")
    t.write("Nombre 3", align='left', font=('Arial',10,'normal'))

def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def circle(radio):
    # Crear un objeto Turtle para dibujar
    t = Turtle()
    t.speed(1)  # Velocidad de dibujo

    # Configurar el color del círculo
    t.fillcolor("red")
    t.begin_fill()

    # Dibujar el círculo
    t.circle(radio)

    t.end_fill()


def rectangle(largo, ancho):
    # Crear un objeto Turtle para dibujar
    t = Turtle()
    t.speed(1)  # Velocidad de dibujo

    # Configurar el color del rectángulo
    t.fillcolor("purple")
    t.begin_fill()

    # Dibujar el rectángulo
    for _ in range(2):
        t.forward(largo)
        t.right(90)
        t.forward(ancho)
        t.right(90)

    t.end_fill()

def square(medida):
    # Crear un objeto Turtle para dibujar
    t = Turtle()
    t.speed(1)  # Velocidad de dibujo

    # Configurar el color del rectángulo
    t.fillcolor("pink")
    t.begin_fill()

    # Dibujar el rectángulo
    for _ in range(2):
        t.forward(medida)
        t.right(90)
        t.forward(medida)
        t.right(90)

    t.end_fill()

def triangulo(lado):
    # Inicializar la ventana de dibujo
    ventana = Screen()
    ventana.bgcolor("white")

    # Crear un objeto Turtle para dibujar
    t = Turtle()
    t.speed(1)  # Velocidad de dibujo

    # Configurar el color del triángulo
    t.fillcolor("green")
    t.begin_fill()

    # Dibujar el triángulo equilátero
    for _ in range(3):
        t.forward(lado)
        t.left(120)

    t.end_fill()

def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    if key == 'shape':
        if value == 'line':
            state[key] = line
        elif value == 'square':
            state[key] = square
        elif value == 'circle':
            state[key] = circle
        elif value == 'rectangle':
            state[key] = rectangle
        elif value == 'triangle':
            state[key] = triangulo
    else:
        state[key] = value

state = {'start': None, 'shape': line}

info_alumno()
'''
rectangle(10,10) # Cuadrado
rectangle(10,5) # Rectángulo
circle(10) # Círculo
triangulo(10) # Triángulo
'''

setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square(100)), 's')
onkey(lambda: store('shape', circle(50)), 'c')
onkey(lambda: store('shape', rectangle(100,50)), 'r')
onkey(lambda: store('shape', triangulo(100)), 't')
done()
  
'''
Logo
Free Python Games

Donate

If you or your organization uses Free Games, consider donating:

Donate to Free Python Games
Related Topics

    Documentation overview
        Previous: Illusion
        Next: Maze

Quick search
'''
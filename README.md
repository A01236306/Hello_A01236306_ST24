# - Hello_Guadalupe_ST24
# - Ma. Guadalupe Roque Díaz de Leó
# - Carrera
# Lugar de Origen
## - Equipo -

# ❤️
# 💡
# 👍
# 💀
# 😈
# 🍳
# 👽


# **SemanaTec**

| Syntax | Description |
| ----------- | ----------- |
| Header | Title |
| Paragraph | Text |

# 2. Tipos de Letra
**Bold**
*Italic*
>Block

>Hola
>Adiós
>

# 3. Lista Enumerada
1. Gorditas Doña Tota Cd. Victoria
2. Corundas de Morelia
3. Tortas de la Barda, Tampico
4. La parroquia, Veracruz
5. Tacos Alfaro, Centrito Valle
6. Tacos de Villa de Santiago, Garza Sada
7. Tacos atarantados - vasconcelos
8. Chilaquiles Tec - ITESM

# 4. LISTA CON VIÑETAS
- Tacos Güero
- Tacos la Morelense
- Tacos el Portón

# 5. Código
'''

"""Connect Four

Exercises

1. Change the colors.
2. Draw squares instead of circles for open spaces.
3. Add logic to detect a full row.
4. Create a random computer player.
5. How would you detect a winner?
"""

from turtle import *

from freegames import line

turns = {'red': 'yellow', 'yellow': 'red'}
state = {'player': 'yellow', 'rows': [0] * 8}


def grid():
    """Draw Connect Four grid."""
    bgcolor('light blue')

    for x in range(-150, 200, 50):
        line(x, -200, x, 200)

    for x in range(-175, 200, 50):
        for y in range(-175, 200, 50):
            up()
            goto(x, y)
            dot(40, 'white')

    update()


def tap(x, y):
    """Draw red or yellow circle in tapped row."""
    player = state['player']
    rows = state['rows']

    row = int((x + 200) // 50)
    count = rows[row]

    x = ((x + 200) // 50) * 50 - 200 + 25
    y = count * 50 - 200 + 25

    up()
    goto(x, y)
    dot(40, player)
    update()

    rows[row] = count + 1
    state['player'] = turns[player]


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
onscreenclick(tap)
done()

'''

# 6. Regla

---

# 7. Link
- [freeGames](http://grantjenks.com/docs/freegames/)
- [Markdown](https://www.markdownguide.org/cheat-sheet/)

# 8. Imagenes

![Jeffrey](https://uploads.dailydot.com/bfc/cc/836ca6a6bd93893d5659d56be6719007.jpg?auto=compress%2Cformat&fit=scale&h=700&ixlib=php-3.3.0&w=1400&wpsize=fp_1600_700)

# 9. Tabla
| Partida Rápida | Victoria | Derrota | Tiempo |
|----------------|----------|---------|--------|
|                | 153      | 26      |        |
|                | 125      | 17      |        |
|                | 149      | 22      | 301    |
|                | 195      | 28      | 129    |
|                | 127      | 21      | 157    |
|                | 214      | 31      | 202    |
|                | 72       | 9       | 118    |
|                | 209      | 31      | 198    |
|                | 86       | 15      | 204    |
|                | 162      | 29      |        |
|                | 136      | 24      |        |
|                | 239      | 35      |        |
|                | 196      | 28      |        |
|                | 103      | 15      |        |
|                | 117      | 17      |        |
|                | 242      | 36      |        |
|                | 277      | 41      |        |
|                | 299      | 44      |        |
|                | 208      | 31      |        |
|                | 136      | 24      |        |
|                | 160      | 23      |        |
|                | 203      | 30      |        |
|                | 151      | 27      |        |
|                | 189      | 28      |        |
|                | 204      | 29      |        |
|                | 209      | 31      |        |
|                | 329      | 49      |        |
|                | 170      | 31      |        |
|                | 169      | 30      |        |
|                | 117      | 21      |        |
|                | 110      | 19      |        |
| Promedio       | 176.00   | 27      | 185.89 |

| Partida Rápida | Derrota | Tiempo |
|----------------|---------|--------|
|                | 251     | 43     |
|                | 113     | 16     |
|                | 42      |        |
|                | 20      |        |
|                | 21      |        |
|                | 34      |        |
|                | 20      |        |
|                | 33      |        |
|                | 34      |        |
|                | 23      |        |
|                | 18      |        |
|                | 21      |        |
|                | 20      |        |
|                | 33      |        |
|                | 22      |        |
|                | 13      |        |
|                | 16      |        |
|                | 18      |        |
|                | 20      |        |
|                | 24      |        |
|                | 24      |        |
|                | 14      |        |
|                | 23      |        |
|                | 14      |        |
|                | 19      |        |
|                | 17      |        |
|                | 26      |        |
|                | 18      |        |
|                | 21      |        |
|                | 22      |        |
|                | 21      |        |
| Promedio       | 19.00   | 20.00  |

| Normal | Victoria | Derrota | Tiempo |
|--------|----------|---------|--------|
|        | 197      | 22      |        |
|        | 151      | 13      |        |
|        | 104      | 12      |        |
|        | 158      | 19      |        |
|        | 130      | 12      |        |
|        | 156      | 21      |        |
|        | 134      | 17      |        |
|        | 124      | 16      |        |
|        | 141      | 19      |        |
|        | 123      | 14      |        |
|        | 105      | 17      |        |
|        | 159      | 20      |        |
|        | 146      | 18      |        |
|        | 237      | 33      |        |
|        | 141      | 22      |        |
|        | 77       | 13      |        |
|        | 141      | 16      |        |
|        | 163      | 18      |        |
|        | 114      | 20      |        |
|        | 166      | 24      |        |
|        | 127      | 20      |        |
|        | 84       | 14      |        |
|        | 134      | 16      |        |
|        | 91       | 14      |        |
|        | 89       | 14      |        |
|        | 113      | 19      |        |
|        | 145      | 20      |        |
|        | 115      | 19      |        |
|        | 116      | 19      |        |
|        | 123      | 17      |        |
|        | Promedio | 133.97  | 18.00  |

| ARAM | Victoria | Derrota | Tiempo |
|------|----------|---------|--------|
|      | 93       | 13      |        |
|      | 130      | 17      |        |
|      | 214      | 10      |        |
|      | 67       | 10      |        |
|      | 149      | 20      |        |
|      | 237      | 25      |        |
|      | 188      | 14      |        |
|      | 132      | 17      |        |
|      | 131      | 17      |        |
|      | 168      | 19      |        |
|      | 250      | 19      |        |
|      | 126      | 13      |        |
|      | 134      | 21      |        |
|      | 127      | 22      |        |
|      | 94       | 13      |        |
|      | 127      | 18      |        |
|      | 115      | 14      |        |
|      | 127      | 19      |        |
|      | 156      | 20      |        |
|      | 99       | 13      |        |
|      | 88       | 16      |        |
|      | 104      | 18      |        |
|

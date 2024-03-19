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
| Partida Rápida     |          | Normal |          | ARAM |            | URF (Modalidad temporal) |            | Coop vs IA (Intermedio) |            | Coop vs IA (Principiante) |            | Coop vs IA (Intro) |            |
|--------------------|----------|--------|----------|------|------------|--------------------------|------------|--------------------------|------------|----------------------------|------------|---------------------|------------|
|                    | Victoria | Derrota | Tiempo   | Victoria | Derrota | Tiempo                   | Victoria   | Derrota                  | Tiempo     | Victoria                  | Derrota    | Tiempo              | Victoria   | Derrota | Tiempo   |
| 153                | 26       |        | 251      | 43   | 197        | 22                       | 93         | 13                       | 148        | 24                         | 95.00      | 16.00               | 158        | 23       |
| 125                | 17       |        | 113      | 16   | 151        | 13                       | 130        | 17                       | 123        | 19                         | 117.00     | 21.00               | 165        | 24       |
| 149                | 22       | 301    | 42       | 104  | 12         | 214                      | 10         | 142                      | 23         | 118.00                     | 21.00      | 116                  | 19         |
| 195                | 28       |        | 129      | 20   | 158        | 19                       | 67         | 10                       | 128        | 20                         | 141.00     | 25.00               | 125        | 23       |
| 127                | 21       | 157    | 21       | 130  | 12         | 149                      | 20         | 120                      | 19         | 122.00                     | 22.00      | 119                  | 22         |
| 214                | 31       | 202    | 34       | 156  | 21         | 237                      | 25         | 125                      | 22         | 120.00                     | 20.00      | 130                  | 24         |
| 72                 | 9        | 118    | 20       | 134  | 17         | 188                      | 14         | 121                      | 21         | 122.00                     | 27.00      | 99                   | 18         |
| 209                | 31       | 198    | 33       | 124  | 16         | 132                      | 17         | 86                       | 14         | 81.00                      | 18.00      | 98                   | 18         |
| 86                 | 15       | 204    | 34       | 141  | 19         | 131                      | 17         | 98                       | 17         | 105.00                     | 23.00      | 132                  | 24         |
| 162                | 29       |        |          | 123  | 14         | 168                      | 19         | 88                       | 16         | 100.00                     | 17.00      | 94                   | 17         |
| 136                | 24       |        |          | 105  | 17         | 250                      | 19         | 104                      | 18         | 88.00                      | 16.00      | 101                  | 18         |
| 239                | 35       |        |          | 167  | 21         | 126                      | 13         | 111                      | 19         | 94.00                      | 16.00      | 96                   | 17         |
| 196                | 28       |        |          | 159  | 20         | 134                      | 21         | 93                       | 16         | 89.00                      | 16.00      | 102                  | 18         |
| 103                | 15       |        |          | 237  | 33         | 146                      | 18         | 127                      | 22         | 102.00                     | 18.00      | 78                   | 17         |
| 117                | 17       |        |          | 141  | 22         | 94                       | 13         | 127                      | 22         | 95.00                      | 16.00      | 114                  | 26         |
| 242                | 36       |        |          | 77   | 13         | 127                      | 18         | 92                       | 20         | 92.00                      | 14.00      | 96                   | 21         |
| 277                | 41       |        |          | 141  | 16         | 115                      | 14         | 87                       | 19         | 90.00                      | 15.00      | 105                  | 19         |
| 299                | 44       |        |          | 163  | 18         | 127                      | 19         | 82                       | 18         | 140.00                     | 25.00      | 118                  | 21         |
| 208                | 31       |        |          | 114  | 20         | 156                      | 20         | 92                       | 20         | 112.00                     | 19.00      | 88                   | 16         |
| 136                | 24       |        |          | 166  | 24         | 99                       | 13         | 89                       | 19         | 107.00                     | 19.00      | 100                  | 18         |
| 160                | 23       |        |          | 127  | 20         | 154                      | 23         | 114                      | 25         | 97.00                      | 17.00      | 88                   | 16         |
| 203                | 30       |        |          | 84   | 14         | 132                      | 16         | 85                       | 18         | 101.00                     | 18.00      | 100                  | 18         |
| 151                | 27       |        |          | 134  | 16         | 111                      | 16         | 94                       | 21         | 125.00                     | 22.00      | 102                  | 18         |
| 189                | 28       |        |          | 91   | 14         | 156                      | 23         | 91                       | 20         | 101.00                     | 18.00      | 99                   | 18         |
| 204                | 29       |        |          | 89   | 14         | 198                      | 24         | 91                       | 20         | 106.00                     | 19.00      | 90                   | 16         |
| 209                | 31       |        |          | 113  | 19         | 145                      | 17         | 80                       | 17         | 85.00                      | 16.00      | 95                   | 17         |
| 329                | 49       |        |          | 145  | 20         | 162                      | 25         | 115                      | 26         | 78.00                      | 14.00      | 130                  | 24         |
| 170                | 31       |        |          | 115  | 19         | 183                      | 20         | 115                      | 25         | 80.00                      | 15.00      | 75                   | 17         |
| 169                | 30       |        |          | 128  | 16         | 141                      | 22         | 91                       | 20         | 114.00                     | 21.00      | 78                   | 17         |
| 117                | 21       |        |          | 116  | 19         | 176                      | 21         | 130                      | 23         | 111.00                     | 21.00      | 77                   | 17         |
| 110                | 19       |        |          | 123  | 17         | 185                      | 21         | 125                      | 22         | 105.00                     | 20.00      | 75                   | 16         |
| 176.00             | 27       | 185.89 | 29       | 133.97 | 18         | 148.48                   | 18         | 107                      | 20         | 104                       | 19         | 105                 | 19         |
|       XP/Min: 6.52xp       |       XP/Min: ~6.38xp      |      XP/Min: 7.44xp       |      XP/Min: 8.25xp      |      XP/Min: 5.35xp       |       XP/Min: 5.47xp       |       XP/Min: 5.53xp       |

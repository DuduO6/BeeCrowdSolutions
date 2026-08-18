a, b, c, d = map(int, input().split())

hours = 24 - a + c
minutes = 60 - b + d


if minutes >= 60:
    minutes -= 60

if b > d:
    hours -= 1

if hours > 24:
    hours -= 24

if hours == 24 and minutes > 0:
    hours = 0

print(f"O JOGO DUROU {hours} HORA(S) E {minutes} MINUTO(S)")
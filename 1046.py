a, b = map(int, input().split())

hours = 24 - a + b

if hours > 24:
    hours -= 24
print(f"O JOGO DUROU {hours} HORA(S)")
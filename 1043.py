a, b, c = map(float, input().split())

vector = [a, b, c]

vector.sort()

if vector[0] + vector[1] > vector[2]:
    print("Perimetro = %.1f" % (vector[0] + vector[1] + vector[2]))
else:
    print("Area = %.1f" % (((a + b) * c) / 2))
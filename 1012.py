
altura, comp, largura = input("").split()
A = float(altura)
B = float(comp)
C = float(largura)

triangulo = (A * C) / 2
circulo = 3.14159 * pow(C, 2)
trapezio = ((A + B) * C) / 2
quadrado = pow(B, 2)
retangulo = A * B
print("TRIANGULO: %.3f" % triangulo)
print("CIRCULO: %.3f" % circulo)
print("TRAPEZIO: %.3f" % trapezio)
print("QUADRADO: %.3f" % quadrado)
print("RETANGULO: %.3f" % retangulo)


A = int(input(""))

print("%d" % A)

B = int(A/100)
print("%d nota(s) de R$ 100,00" % B)
C = A % 100

D = int(C/50)
print("%d nota(s) de R$ 50,00" % D)
E = C % 50

F = int(E/20)
print("%d nota(s) de R$ 20,00" % F)
G = E % 20

H = int(G/10)
print("%d nota(s) de R$ 10,00" % H)
I = G % 10

J = int(I/5)
print("%d nota(s) de R$ 5,00" % J)
K = I % 5

L = int(K/2)
print("%d nota(s) de R$ 2,00" % L)
M = K % 2

N = int(M/1)
print("%d nota(s) de R$ 1,00" % N)
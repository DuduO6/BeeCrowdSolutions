cash = float(input())

cash = int(round(cash * 100))

A = cash//10000
B = (cash%10000)

C = int(B/5000)
D = (B%5000)

E = int(D/2000)
F = (D%2000)

G = int(F/1000)
H = (F%1000)

I = int(H/500)
J = (H%500)

K = int(J/200)
L = (J%200)
print("NOTAS:")
print("%d nota(s) de R$ 100.00" % A)
print("%d nota(s) de R$ 50.00" % C)
print("%d nota(s) de R$ 20.00" % E)
print("%d nota(s) de R$ 10.00" % G)
print("%d nota(s) de R$ 5.00" % I)
print("%d nota(s) de R$ 2.00" % K)

M = int(L/100)
N = (L%100)

O= int(N/50)
P = (N%50)

Q = int(P/25)
R = (P%25)

S = int(R/10)
T = (R%10)

U = int(T/5)
V = (T%5)

W = int(V/1)

print("MOEDAS:")
print("%d moeda(s) de R$ 1.00" % M)
print("%d moeda(s) de R$ 0.50" % O)
print("%d moeda(s) de R$ 0.25" % Q)
print("%d moeda(s) de R$ 0.10" % S)
print("%d moeda(s) de R$ 0.05" % U)
print("%d moeda(s) de R$ 0.01" % W)


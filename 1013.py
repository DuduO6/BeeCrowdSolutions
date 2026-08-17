A, B, S = input().split()
A = int(A)
B = int(B)    
S = int(S)

maiorAB = (A + B + abs(A - B)) / 2      
maiorABC = (maiorAB + S + abs(maiorAB - S)) / 2      

print("%d eh o maior" % maiorABC)
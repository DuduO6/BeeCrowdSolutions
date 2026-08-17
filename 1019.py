A = int(input())

B = int(A%3600)
C = int(B/60)
D = B % 60  

print("%d:%d:%d" % (int(A/3600), C, D))
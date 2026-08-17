a, b, c, d = map(float, input().split())

aw = a*2
bw = b*3
cw = c*4

average = (aw + bw + cw + d) / 10
print("Media: %.1f" % average)

if average >= 7.0:
    print("Aluno aprovado.")
elif average < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    e = float(input())
    print("Nota do exame: %.1f" % e)
    average = (average + e) / 2
    if average >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % average)
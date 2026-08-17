days = int(input())

years = days / 365
A = int(days%365)

months = int(A/30)
B = int(A%30)

print ("%d ano(s)" % years)
print ("%d mes(es)" % months)
print ("%d dia(s)" % B)


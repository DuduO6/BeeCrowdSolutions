cod1, unidades1, preço1 = input().split()
cod1 = int(cod1)
unidades1 = int(unidades1)
preço1 = float(preço1)

cod2, unidades2, preço2 = input().split()
cod2 = int(cod2)
unidades2 = int(unidades2)
preço2 = float(preço2)

TOTAL = (unidades1 * preço1 + unidades2 * preço2)
print("VALOR A PAGAR: R$ %.2f" % TOTAL)


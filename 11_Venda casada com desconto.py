##Exercicio 1
def produto(Qa, Qb):
    a = 0
    b = 0
    if (Qa != 0 and Qb == 0) or (Qa == 0 and Qb != 0):
        a = Qa * 10 - ((Qa * 10) * 0.10)
        b = Qb * 20 - ((Qb * 20) * 0.10)
    else:
        if Qa != 0 and Qb != 0:
            a = Qa * 10 - ((Qa * 10) * 0.15)
            b = Qb * 20 - ((Qb * 20) * 0.15)
    return a + b
a = int(input('Digite o valor do produto A: '))
b = int(input('Digite o valor do produto B: '))
print('Total a pagar =', produto(a, b))

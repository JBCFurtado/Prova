num = int(input('Digite um valor: '))
def par(x):
    return (x % 2 == 0)
def par_impar(x):
    if par(x):
        return 'Par'
    else:
        return 'Ímpar'
print(par_impar(num))


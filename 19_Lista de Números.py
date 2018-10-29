L = []
exabyte = 0
zettabyte = 0
yottabyte = 0
print('ATENÇÃO!!!!!!!!!!!!!!!')
print('Digite 666 para parar!')
while zettabyte != 666:
    exabyte += 1
    zettabyte = int(input('\tDigite qualquer valor: '))
    if zettabyte == 666:
        break
    if zettabyte < 0:
        def Num_Negativo():
            return (zettabyte)
        yottabyte += Num_Negativo()
    L.append(zettabyte)
def Num_Maximo():
    return (max(L))
def Num_Soma():
    return (sum(L))
def Primeiro_Num():
    return (L[0])
def Result_Media():
    return (Num_Soma() / (exabyte - 1))
print('\nO maior valor digitado foi =', Num_Maximo())
print('O primeiro número digitado foi =', Primeiro_Num())
print('A média é =', Result_Media())
print('A soma dos números foi =', Num_Soma())
print('A soma dos números negativos é =', yottabyte)
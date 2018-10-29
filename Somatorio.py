def somatorio():
    a = 0
    n = int(input('Digite o numero: '))
    for i in range(n + 1):
        a += i
    return a
print('Soma dos numeros =',somatorio())
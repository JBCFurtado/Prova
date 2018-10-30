print('-'*22)
print('Sequência de Fibinacci')
print('-'*22)
n = int(input('Digite quantos termos você quer mostrar: '))
n1 = 0
n2 = 1
print('_'*20)
print('{} {} '.format(n1, n2), end='')
contador = 3
while contador <= n:
    n3 = n1 + n2
    print('{} '.format(n3), end='')
    n1 = n2
    n2 = n3
    contador += 1
print('Até aqui')
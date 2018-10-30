numeros = [0, 0, 0, 0, 0]
x = 0
while x < 5:
    numeros[x] = int(input('Numero {0}: '.format(x)))
    x += 1
escolhido = int(input('Que posição você quer imprimir: '))
print('Você escolheu o número: {0}'.format(numeros[escolhido]))

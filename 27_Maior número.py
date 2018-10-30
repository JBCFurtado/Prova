maior = 0
x = int(input('Digite um número: '))
maior = x
while x != 999:
    x = int(input('Digite um número: '))
    if x == 999:
        break
    if x > maior:
        maior = x
print('\n O maior é: ', maior)
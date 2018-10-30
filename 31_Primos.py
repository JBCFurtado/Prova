# num = int(input("Digite um numero: "))
# contador = 1
# while contador <= num:
#     if num % 2 == 1:
#         contador = contador+1
#         print("Número Primo")
#         break
#     else:
#         print("Não é número primo")
#         break

primos = []
num = int(input('Qual numero testar? '))
for n in range(1, num+1):
    if num % n == 0:
        primos.append(n)
    if len(primos) > 2:
        print('O número {} NÃO é Primo!'.format(n))
        break
if len(primos) == 2:
    print('O número {} é PRIMO.'.format(num))

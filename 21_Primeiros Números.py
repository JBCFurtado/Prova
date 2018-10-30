# x = int(input('Digite um valor: '))
# y = 0
# for i in range(x + 1):
#     y = y + i
# print('a soma dos n termos é: ', y)

#Calcular o somatório dos n primeiros números.
soma = 0
limite_sup = int(input('Entre com o limite superior: '))
for i in range(1, limite_sup + 101):
    soma += i
print(soma)

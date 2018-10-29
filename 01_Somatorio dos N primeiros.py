# def somatorio():
#     a = 0
#     n = int(input('Digite o numero: '))
#     for i in range(n + 1):
#         a += i
#     return a
# print('Soma dos numeros =',somatorio())

def main():
    num = int(input("Digite um inteiro [999 para terminar]: "))
    soma = 0
    while num != 999:
        soma = soma + num
        num = int(input("Digite um inteiro [999 para terminar]: "))
    print("A soma foi: ", soma)
main()

def imprimir_spam():
    n = int(input('teste: '))
    for i in range(1, n+1):
        print(n, imprimir_spam())

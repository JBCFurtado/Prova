n = int(input('Digite um número para saber seu fatorial: '))
fatorial = 1
for i in range(2, n+1):
    fatorial *= i
print(fatorial)

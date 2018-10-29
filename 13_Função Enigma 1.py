a = float(input('Digite A: '))
b = float(input('Digite B: '))
p = int(input('Digite P: '))
q = int(input('Digite Q: '))
i = 0
soma = 0
while i <= (q - p):
    soma = (a/b) ** i
    i = i + 1
print(soma)

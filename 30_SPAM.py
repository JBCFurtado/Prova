linha = '-' * 50
titulo = 'ALGORITMOS E TÉCNICAS DE PROGRAMAÇÃO \nProfessora: Vanderlene Rocha\n3ª Avaliação\nAluno: Josué Batista'
print(linha)
print(titulo.center(50))
print(linha)
linha = '-' * 50
titulo = 'Imprime N SPAMs'
print(linha)
print(titulo.center(50))
print(linha)
def total_palavra(a, b):
    total = a * b
    return total
x = int(input('Digite quantas vezes a palavra deve ser repetida: '))
y = input('Digite que palavra deseja que seja repetir: ')
print(total_palavra(x, y))

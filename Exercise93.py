def fucaoEnigma3(n):
    soma = 0
    for i in range(1, n+1):
        soma = soma+i
        j =1
        while j<=n:
            soma = soma -j
        j = j+1
    print(soma)

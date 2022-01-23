def divisao(n):
    tamanho = len(str(n))
    if tamanho == 3:
        resto = n % 100
        centena = n - resto
        print(centena)
        divisao(resto)
    if tamanho == 2:
        resto = n % 10
        dezena = n - resto
        print(dezena)
        divisao(resto)
    if tamanho == 1:
        print(n)

divisao(235)

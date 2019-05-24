import random

alfabeto = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


class Entrada():
    texto = input('Insira sua mensagem: ')
    chave = int(input('Insira sua chave numérica'))

    chave_aleatoria = []

    i = 1
    while i <= chave:
        chave_aleatoria.append(i)
        i += 1

    print(chave_aleatoria)

    random.shuffle(chave_aleatoria)
    print(chave_aleatoria)

    mensagem = texto.replace(" ", "").upper()
    print(mensagem)

    mensagem_array = []
    i = 0

    while i <= len(texto):
        while i <= 5:
            for caractere in mensagem:
                mensagem_array.append(caractere)
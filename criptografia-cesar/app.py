
def principal():
    cabecalho()
    alfabeto = alfabeto_criptografado()

    mensagem = recebe_mensagem()

    chave = input("Insira o valor da chave: ")

    tamanho_chave = len(chave)

    tipo_criptografia = escolhe_criptografia()

    if tipo_criptografia == 1:
        criptografar(alfabeto, mensagem, chave, tamanho_chave)
    elif tipo_criptografia == 2:
        descriptografar(alfabeto, mensagem, chave, tamanho_chave)
    else:
        print('Opção inválida')


def cabecalho():
    print("****************")
    print("Criptografe sua mensagem!")
    print("****************")


def recebe_mensagem():
    mensagem = input("Insira sua mensagem com caracteres alfabeticos: ").upper()
    return mensagem


def alfabeto_criptografado():
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    return alfabeto


def escolhe_criptografia():
    print("O que deseja fazer?")
    tipo_criptografia = int(input("1 - Criptografar   2 - Descriptografar"))

    return tipo_criptografia


def criptografar(alfabeto, mensagem, chave):
    texto_criptografado = []
    for letra in chave:
        for palavra in mensagem:
            for caractere in palavra:
                posicao_chave = alfabeto.index(letra)
                posicao_letra = alfabeto.index(caractere)
                letra_convertida = (posicao_letra + posicao_chave) % 26
                texto_criptografado.append(alfabeto[letra_convertida])
        texto_separado = " ".join(texto_criptografado)
        print(f"A mensagem criptografada é: ")
        print(texto_separado, end='')


def descriptografar(alfabeto, mensagem, chave):
    texto_criptografado = []
    for palavra in mensagem:
        for caractere in palavra:
            posicao_letra = alfabeto.index(caractere)
            letra_convertida = posicao_letra - chave
            texto_criptografado.append(alfabeto[letra_convertida])

    texto_separado = " ".join(texto_criptografado)
    print(f"A mensagem descriptografada é: ")
    print(texto_separado, end='')


if __name__ == '__main__':
    principal()

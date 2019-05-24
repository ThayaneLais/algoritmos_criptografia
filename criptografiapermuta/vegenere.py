class Cifra(object):

    texto = input('Insira sua mensagem: ')
    chave = input('Insira sua chave: ')

    def format_str(self, texto):

        return texto.replace(' ', '').upper()

    def desloca_alfabeto(self, alfabeto, desloca):

        return alfabeto[desloca:] + alfabeto[:desloca]


class Vigenere(Cifra):

    def __init__(self):
        self.letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def repete_chave(self, chave, texto):

        if len(chave) < len(texto):
            nova_chave = chave * int((len(texto) / len(chave)))
            if len(nova_chave):
                nova_chave += chave[:len(nova_chave)]
            return nova_chave.upper()
        return chave.upper()

    def criptografa(self, texto_normal, chave, descriptografa=False):

        chave = self.repeat_password(chave, texto_normal)
        texto_normal = self.format_str(texto_normal)
        texto_saida = ''
        for i, char in enumerate(texto_normal.upper()):
            # indice da letra da cifra
            index_chave = self.letras.find(chave[i])
            # gera alfabeto cifrado
            c_alfabeto = self.desloca_alfabeto(self.letras, index_chave)

            if descriptografa:
                index_p = c_alfabeto.find(char)
                texto_saida += self.letras[index_p]
            else:
                index_p = self.letras.find(char)
                texto_saida += c_alfabeto[index_p]

        return texto_saida

    def descriptografa(self, texto_cifrado, chave):

        return self.criptografa(texto_cifrado, chave, True)

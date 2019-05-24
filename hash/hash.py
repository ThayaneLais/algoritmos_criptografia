texto = input("Insira sua mensagem: ")

valor = 0
for caractere in texto:
    valor += ord(caractere)

hash_dois_digitos = valor % 100
print(f"O HASH da frase é: {hash_dois_digitos}")

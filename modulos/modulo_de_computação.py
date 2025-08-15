from .modulo_de_transições import transicoes
def computação(chave,palavra,modo):
    palavra_traduzida = ""
    for letra in palavra:
        if letra in transicoes(chave, modo):
            palavra_traduzida += transicoes(chave, modo)[letra]
        else:
            palavra_traduzida += letra
    print(palavra_traduzida)
    return palavra_traduzida

#computação("AAA","a","gay")  
# Exemplo de uso


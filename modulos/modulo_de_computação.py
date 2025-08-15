def computação(chave,palavra,modo):
    # abaixo a chamada do modulo de transições, enquanto ainda não estiver pronto crie um dicinario que relacione uma letra a outra exemplo {a}:b 
    from modulo_de_transições import transicoes
    # produção = transições(chave, modo)
    prod = transicoes(chave, modo)
    # voce deve pegar a palavra recebida e traduzir cada letra para seu equivalente no dicionario
    palavra_traduzida = ""
    # exemplo: "casa" faça um loop que passe por cada letra da palavra, identifique a chave equivalente a essa letra no dicionario e salve a letra traduzida em uma variavel chamada "palavra traduzida" que vai receber letra a letra correpondente do valor da letra achada no dicionario
    for letra in palavra:
        if letra in prod:
            palavra_traduzida += prod[letra]
        else:
            palavra_traduzida += letra


    # o retorno dessa função é a palavra traduzida
    print(f"Palavra traduzida: {palavra_traduzida} ")
    return palavra_traduzida

    
# Exemplo de uso


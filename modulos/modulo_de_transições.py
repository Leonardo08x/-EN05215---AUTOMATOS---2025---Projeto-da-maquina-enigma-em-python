import random
def lista_ascii_unica(chave):
   random.seed(sum(ord(c) for c in chave)) 
   lista_ascii = [chr(simbolo) for simbolo in range(65,90)] + [chr(simbolo) for simbolo in range(97,122)] + [chr(32)]
   random.shuffle(lista_ascii)
   return lista_ascii
def transicoes(chave, modo):
    return  { chave:letra for (chave,letra) in zip(lista_ascii_unica(chave) , [chr(simbolo) for simbolo in range(65,90)] + [chr(simbolo) for simbolo in range(97,122)] + [chr(32)],)}  if modo =="Descriptografar" else { chave:letra for (chave,letra) in zip([chr(simbolo) for simbolo in range(65,90)] + [chr(simbolo) for simbolo in range(97,122)] + [chr(32)], lista_ascii_unica(chave))} 
   


#debug, checa se os valores se repetem, e se os modos geram dicionarios invertidos, REMOVER DA VERSÃO FINAL
"""print(transicoes("AAA", "Descriptografar"))
print(transicoes("AAA", "criptografar"))
valores = transicoes("ca", "gay").values()

for i in valores:
    count = 0
    for j in valores:
        if i == j:
            count += 1
            if count == 2:
             print(i+"="+j)"""
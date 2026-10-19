# ======================================================================
# beecrowd 1244 - Ordenação por Tamanho
# Objetivo: imprimir as palavras da MAIOR para a MENOR; palavras de mesmo
#           tamanho mantêm a ordem em que vieram.
# Entrada: número de casos no início; uma linha de palavras por caso.
# ======================================================================
#
# FUNÇÕES (nativas, sem import):
#   lista.sort(key=f, reverse=True) -> ordena NO LUGAR usando f(x) como
#                                      critério; reverse=True = decrescente.
#   sorted(lista, key=...)          -> igual, mas devolve uma lista NOVA.
#   str.split()                     -> quebra o texto nos espaços.
#   "sep".join(lista)               -> junta as strings com o separador.
N = int(input())

for _ in range(N):
    palavras = input().split()

    # key=len: compara pelo tamanho da palavra, não pelo texto.
    # O sort do Python é ESTÁVEL: empates mantêm a ordem original. É
    # exatamente o desempate que o problema pede (o reverse não quebra isso).
    palavras.sort(key = len, reverse = True )

    print(" ".join(palavras))



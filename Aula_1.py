# ======================================================================
# beecrowd 1025 - Onde está o Mármore?  |  Ordenação e Busca Binária
# Objetivo: ordenar os mármores e, para cada consulta, dizer a posição
#           (contando a partir de 1) da PRIMEIRA ocorrência do número.
# Entrada: vários casos "N Q"; termina com a linha "0 0" (sentinela).
# ======================================================================
#
# BIBLIOTECA bisect (padrão do Python): busca binária em lista ORDENADA.
#   bisect_left(lista, x)  -> índice da 1ª ocorrência de x, ou a posição
#                             onde x entraria sem quebrar a ordem.  O(log n)
#   bisect_right(lista, x) -> índice logo DEPOIS da última ocorrência de x.
#   Exemplo com lista = [1, 3, 3, 5]:
#     bisect_left(lista, 3) -> 1   (o primeiro 3)
#     bisect_left(lista, 4) -> 3   (4 não existe; entraria antes do 5)
#     bisect_left(lista, 9) -> 4   (maior que todos: devolve len(lista))
#   Ele SEMPRE devolve uma posição, mesmo se x não existir -> conferir depois.
from bisect import bisect_left

# Contador de casos, usado no cabeçalho "CASE# n:".
Caso = 1

while True:
    # map(int, ...) converte cada pedaço da linha em int.
    N, Q = map(int, input().split())

    # Sentinela: a linha "0 0" encerra o programa.
    if N == 0 and Q == 0:
        break
    marmores = []
    # Lê os N mármores, um por linha.
    for _ in range(N):    
        marmores.append(int(input()))

    # Ordenar é OBRIGATÓRIO: a busca binária só funciona em lista ordenada.
    # Custo: O(N log N).
    marmores.sort()

    print(f"CASE# {Caso}:")

    for _ in range(Q):
        numero = int(input())

        # Busca binária: descarta metade da lista a cada passo -> O(log N).
        # Com números repetidos, devolve a PRIMEIRA ocorrência (o que o problema pede).
        posicao = bisect_left(marmores, numero)

        # Duas checagens, nesta ordem:
        #  1) posicao < N: se o número for maior que todos, posicao == N e
        #     marmores[N] daria IndexError. O "and" para na 1ª parte falsa,
        #     então a 2ª nem chega a ser executada.
        #  2) marmores[posicao] == numero: confirma que o número existe
        #     (bisect_left só diz onde ele ENTRARIA).
        if posicao < N and marmores[posicao]== numero:
            # +1 porque o Python conta a partir do 0 e o problema conta a partir do 1.
            print(f"{numero} found at {posicao+1}")
        else:
            print(f"{numero} not found")
    Caso += 1
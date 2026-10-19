# ======================================================================
# beecrowd 1110 - Jogando Cartas Fora  |  Fila
# Objetivo: descartar a carta do topo, mover a próxima para o fundo e
#           repetir até sobrar uma. Imprimir as descartadas e a que sobrou.
# Entrada: um N por linha; termina com "0" (sentinela).
# ======================================================================
#
# BIBLIOTECA collections.deque (padrão do Python): fila de duas pontas.
#   deque(iteravel) -> cria a fila. Aqui: deque(range(1, N+1)) = 1, 2, ..., N
#   .append(x)      -> insere no FIM                    O(1)
#   .popleft()      -> tira e devolve o do INÍCIO       O(1)
#   .appendleft(x)  -> insere no início                 O(1)
#   .pop()          -> tira do fim                      O(1)
#   .rotate(-1)     -> move o primeiro para o fim
#   fila[0]         -> olha o primeiro sem tirar        O(1)
# Por que não usar list? lista.pop(0) é O(n): desloca todos os elementos.
# Cuidado: popleft() numa deque vazia lança IndexError.
from collections import deque 

while True:
    N = int(input())

    if N == 0:
        break

    # Topo do baralho = esquerda da fila.
    fila = deque(range(1, N+1))

    descartadas = []

    # Repete enquanto houver mais de uma carta.
    while len(fila) > 1:

            # Joga fora a carta do topo. str() porque o join só junta textos.
            descartadas.append(str(fila.popleft()))

            # A nova carta do topo vai para o fundo (equivale a fila.rotate(-1)).
            fila.append(fila.popleft())
    # ATENÇÃO (bug de formato): ",".join gera "1,3,5", mas o esperado é
    # "1, 3, 5" (vírgula + espaço). Com N = 1 a lista fica vazia e sobra um
    # espaço no fim da linha. Correto:
    #     if descartadas:
    #         print("Discarded cards:", ", ".join(descartadas))
    #     else:
    #         print("Discarded cards:")
    # Lembrete: print("A", "B") separa os argumentos com um espaço.
    print("Discarded cards:",",".join(descartadas))
    print("Remaining card:", fila[0])
    
    
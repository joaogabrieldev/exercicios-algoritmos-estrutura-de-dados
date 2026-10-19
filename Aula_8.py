# ======================================================================
# beecrowd 1340 - Eu Posso Adivinhar a Estrutura de Dados!
#                 |  Fila com Remoção de elementos
# Objetivo: dada uma sequência de "1 x" (inseriu x) e "2 x" (removeu x),
#           dizer se a estrutura é pilha, fila ou fila de prioridade.
# Saída: "stack", "queue", "priority queue", "not sure" (mais de uma
#        possível) ou "impossible" (nenhuma).
# Entrada: vários casos até acabar o arquivo (EOF).
# ======================================================================
#
# IDEIA: simular as TRÊS estruturas ao mesmo tempo e eliminar a que errar.
#
# list -> pilha (LIFO): .append(x) empilha, .pop() tira o ÚLTIMO que entrou.
#
# BIBLIOTECA collections.deque -> fila (FIFO):
#   .append(x) -> insere no fim                   O(1)
#   .popleft() -> tira o PRIMEIRO que entrou      O(1)
#
# BIBLIOTECA heapq -> fila de prioridade (heap):
#   heapq.heappush(h, x) -> insere x                      O(log n)
#   heapq.heappop(h)     -> tira e devolve o MENOR        O(log n)
#   h[0]                 -> olha o menor sem tirar        O(1)
#   heapq.heapify(lista) -> transforma uma lista em heap  O(n)
#   O heapq só tem heap de MÍNIMO. Para tirar o MAIOR primeiro, guarde -x
#   e negue de novo ao tirar:  heappush(h, -x)  /  maior = -heappop(h)
#   O heap é uma list comum: use só as funções do heapq nele.
from collections import deque
import heapq

while True:
    try:
        N =int(input())
    except EOFError:
        break

    # As três estruturas recebem as mesmas operações.
    pilha = []
    fila = deque()
    prioridade = []

    # Flags: True = "ainda pode ser essa estrutura".
    epilha = True
    efila = True
    eprioridade = True

    for _ in range(N):
        operacao, valor = map(int, input().split())

        # Operação 1: insere o valor nas três.
        if operacao == 1:
            pilha.append(valor)
            fila.append(valor)
            # Guarda -valor: assim o heap de mínimo devolve o MAIOR primeiro.
            heapq.heappush(prioridade, -valor)

        # Operação 2: remove de cada uma e confere se saiu o valor informado.
        # Estrutura vazia na hora de remover também é eliminada.
        else:
            # Pilha: pop() tira o último que entrou (LIFO).
            if not pilha:
                epilha = False
            else:
                removido = pilha.pop()

                if removido != valor:
                    epilha = False

            # ATENÇÃO (bug): este bloco da FILA foi copiado do bloco da pilha e ficou
            # com "pilha" e "epilha". Assim a fila nunca é eliminada, e a pilha é
            # eliminada pelos erros da fila. Ex.: "1 2 / 1 1 / 2 1 / 2 2" deveria dar
            # "stack", mas este código imprime "queue". Correto:
            #     if not fila:
            #         efila = False
            #     else:
            #         removido = fila.popleft()
            #         if removido != valor:
            #             efila = False
            if not pilha:
                epilha = False
            else:
                removido = fila.popleft()

                if removido != valor:
                    epilha = False

            # Fila de prioridade: nega de volta para obter o maior valor.
            if not prioridade:
                eprioridade = False
            else:
                removido = -heapq.heappop(prioridade)

                if removido != valor:
                    eprioridade = False

    # True vale 1 e False vale 0: a soma conta quantas estruturas sobraram.
    possibilidade = sum([
        epilha,
        efila,
        eprioridade
    ])

    # 0 -> nenhuma serve; mais de 1 -> não dá para saber; 1 -> diz qual.
    if possibilidade == 0:
        print("impossible")
    elif possibilidade > 1:
        print("not sure")
    elif epilha:
        print("stack")
    elif efila:
        print("queue")
    else:
        print("priority queue")
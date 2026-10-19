# ======================================================================
# beecrowd 1162 - Organizador de Vagões  |  Inversão
# Objetivo: menor número de trocas entre vagões VIZINHOS para ordenar.
# Entrada: número de casos no início; cada caso tem L e a ordem dos vagões.
# ======================================================================
#
# IDEIA: cada troca de vizinhos desfaz exatamente uma INVERSÃO (um par
# i < j com v[i] > v[j]). Então a resposta = número de inversões =
# número de trocas que o insertion sort faz. O(N²), ok para L <= 50.
# Sem import: tudo aqui é nativo do Python.
casos = int(input())

for _ in range(casos):
    N = int(input())

    # list(map(int, ...)) transforma a linha "3 1 2" na lista [3, 1, 2].
    vagoes = list(map(int, input().split()))    
    trocas = 0

    # Insertion sort: cada vagão i "afunda" para a esquerda até a posição certa.
    for i in range(1,N):
        J = i

        # Enquanto for menor que o vizinho da esquerda, troca com ele.
        while J > 0 and vagoes[J] < vagoes[J-1]:
            # a, b = b, a troca dois valores sem variável temporária.
            vagoes[J], vagoes[J - 1] = vagoes[J-1],vagoes[J]

            trocas += 1

            J -= 1

    # ATENÇÃO (bug de formato): o esperado é minúsculo e com ponto final.
    # Correto: print(f'Optimal train swapping takes {trocas} swaps.')
    print(f'Optimal Train Swapping takes {trocas} swaps')

# ======================================================================
# beecrowd 1256 - Tabelas Hash
# Objetivo: inserir as chaves numa tabela hash de M posições com
#           h(k) = k mod M, tratando colisões por ENCADEAMENTO (uma lista
#           por posição).
# Saída: "1 -> 27 -> 92 -> \"  (espaço após cada seta e "\" no fim)
# Entrada: número de casos no início; cada caso tem "M C" e as C chaves.
# ======================================================================
#
# CONCEITOS (sem import):
#   função hash      -> transforma a chave num índice da tabela: k % M
#   colisão          -> duas chaves no mesmo índice; aqui cada posição
#                       guarda uma lista e as chaves vão sendo anexadas
#   print(x, end="") -> imprime SEM pular linha (monta a linha aos pedaços)
#
# ATENÇÃO: este arquivo NÃO RODA do jeito que está. Bugs marcados abaixo.
casos = int(input())

for caso in range(casos):
    M, C = map(int, input().split())

    # M listas vazias e INDEPENDENTES, uma por posição. Está certo.
    # Cuidado: [[]] * M criaria M referências para a MESMA lista.
    tabela = [[] for _ in range(M)]

    # ATENÇÃO (bug): falta a vírgula no map -> int() recebe uma lista -> TypeError.
    # Correto: valores = list(map(int, input().split()))
    valores = list(map(int(input().split())))

    for valor in valores:
        # Função hash: o resto da divisão por M decide a posição.
        posicao = valor % M

        # Colisão resolvida por encadeamento: entra no fim da lista da posição.
        tabela[posicao].append(valor)

    for i in range(M):
        # ATENÇÃO (bug de formato): falta o espaço depois de cada "->" e a "\"
        # no fim da linha. Correto:
        #     print(f"{i} -> ", end="")
        #     ...
        #         print(f"{valor} -> ", end="")
        #     print("\\")        # dentro de uma string, a barra se escreve "\\"
        print(f"{i} ->", end="")

        for valor in tabela[i]:
            print(f"{valor} ->", end="")

        print()

    # Linha em branco ENTRE os casos.
    if caso < casos - 1:
        print()
        
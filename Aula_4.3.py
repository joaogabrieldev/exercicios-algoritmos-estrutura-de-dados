# ======================================================================
# beecrowd 1211 - Lista Telefônica Econômica  |  Strings
# Objetivo: quantos dígitos se economiza ao não repetir o prefixo que um
#           telefone tem em comum com o anterior.
# Entrada: vários casos até acabar o arquivo (EOF); cada um com N e N telefones.
# ======================================================================
#
# IDEIA: depois de ORDENAR, números com prefixos parecidos ficam vizinhos.
# O maior prefixo comum com qualquer número anterior é sempre com o
# vizinho de cima -> basta comparar pares vizinhos: O(n log n), em vez de
# comparar todos com todos, O(n²).
# Sem import: tudo aqui é nativo do Python.
#
# ATENÇÃO: este arquivo NÃO RODA do jeito que está. Bugs marcados abaixo.
while True:
    try:
        # ATENÇÃO (bug): input sem () passa a FUNÇÃO para o int() -> TypeError.
        # Correto: N = int(input())
        N = int(input)
    except EOFError:
        break

    Telefones = []

    for _ in range(N):
        # .strip() remove espaços e quebras de linha das pontas.
        Telefones.append(input().strip())

        # ATENÇÃO (bug): sort() e "economia = 0" estão DENTRO do for de leitura
        # (a lista é reordenada N vezes). Os dois devem ficar fora, alinhados
        # com o "for _ in range(N):":
        #     Telefones.sort()
        #     economia = 0
        Telefones.sort()

        economia = 0

    # Compara cada telefone com o vizinho anterior (a lista já está ordenada).
    for i in range (1, N):
        anterior = Telefones[i -1]
        atual = Telefones[i]

        # J = tamanho do prefixo comum: avança enquanto os dígitos forem iguais.
        J = 0
        while J < len(atual) and atual[J] == anterior[J]:
             J += 1 
             # ATENÇÃO (bug): somar J DENTRO do while soma 1+2+3+... em vez de J.
             # O certo é somar uma vez só, depois do while (alinhado com o "J = 0"):
             #     economia += J
             economia += J

    print(economia)

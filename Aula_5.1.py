# ======================================================================
# beecrowd 1251 - Diga-me a Frequência  |  Ordenação com Lambda
# Objetivo: para cada linha, imprimir "código_ASCII frequência" da menor
#           frequência para a maior; no empate, o MAIOR código primeiro.
# Entrada: uma linha por caso, até acabar o arquivo (EOF).
# ======================================================================
#
# FUNÇÕES (nativas, sem import):
#   ord(c)         -> código ASCII do caractere: ord('A') == 65
#   chr(n)         -> o contrário: chr(65) == 'A'
#   dict           -> tabela hash chave -> valor; acesso O(1) em média
#   lambda x: expr -> função anônima de uma linha (usada como key do sort)
#
# ATENÇÃO (bug de leitura): este problema NÃO tem um N no início. Cada
# linha já é um caso, e a entrada vai até o EOF. Com o exemplo oficial,
# int(input()) recebe "AAABBC" e quebra com ValueError. Correto:
#     caso = 0
#     while True:
#         try:
#             texto = input()
#         except EOFError:
#             break
#         if caso > 0:
#             print()            # linha em branco ENTRE os casos
#         ... (contagem e ordenação iguais às de baixo) ...
#         caso += 1
n = int(input())

for caso in range(n):
    texto = input()

    # Dicionário: código -> quantas vezes apareceu.
    frequencia = {}

    for caractere in texto:
        codigo = ord(caractere)

        # Padrão de contagem: cria com 0 na 1ª vez e depois soma 1. Equivale a:
        #     frequencia[codigo] = frequencia.get(codigo, 0) + 1
        if codigo not in frequencia:
            frequencia[codigo] = 0

        frequencia[codigo] +=1
    # Lista com os códigos (as chaves do dicionário), para ordenar.
    # (O nome reaproveita a variável "caractere" do for; "codigos" seria mais claro.)
    caractere = list(frequencia.keys())
    # A lambda devolve uma TUPLA, e tuplas são comparadas elemento a elemento:
    #   1º critério: frequencia[codigo] -> crescente (menor frequência primeiro)
    #   2º critério: -codigo            -> negar inverte: MAIOR código primeiro
    caractere.sort(
        key = lambda codigo: (frequencia[codigo], -codigo)
    )
    for codigo in caractere:
        print(codigo,frequencia[codigo])

    # Linha em branco ENTRE os casos (não depois do último).
    if caso < n - 1:
        print()
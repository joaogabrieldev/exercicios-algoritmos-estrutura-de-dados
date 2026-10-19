# ======================================================================
# beecrowd 1023 - Estiagem  |  Agrupamento  (1ª tentativa)
# Objetivo: agrupar os moradores pelo consumo POR PESSOA (arredondado
#           para baixo), listar os grupos em ordem crescente e mostrar o
#           consumo médio da cidade TRUNCADO em 2 casas.
# Entrada: vários casos; termina com "0" (sentinela).
# ======================================================================
#
# BIBLIOTECA math (padrão do Python):
#   math.floor(x) -> arredonda para BAIXO: floor(13.9) == 13, floor(-2.5) == -3
#   math.ceil(x)  -> arredonda para CIMA:  ceil(2.1) == 3
#   math.trunc(x) -> corta a parte decimal (rumo ao zero): trunc(-2.5) == -2
#   Truncar em 2 casas: math.floor(x * 100) / 100 -> 13.2857 vira 13.28
#   (já f"{x:.2f}" ARREDONDA: 13.2857 vira 13.29)
#
# ATENÇÃO (bug de interpretação): no problema, o 2º número de cada imóvel
# é o consumo TOTAL do imóvel, e não o consumo por pessoa. Este arquivo
# agrupa pelo total. A 2ª tentativa (Aula_7.py) corrige isso.
import math

caso = 1

while True:
    N = int(input())

    if N == 0:
        break

    # Agrupamento com dicionário: consumo -> total de pessoas naquele grupo.
    consumo = {}

    totalpessoas = 0
    totalconsumo = 0

    for _ in range(N):
        pessoas, quantidade = map(int, input().split())

        totalpessoas += pessoas
        # ATENÇÃO: como quantidade já é o total do imóvel, o certo é somar só
        # "quantidade" (sem multiplicar pelas pessoas).
        totalconsumo += pessoas * quantidade

        # Padrão de agrupamento: dict.get(chave, 0) devolve 0 se o grupo ainda não
        # existe; depois soma as pessoas no grupo.
        # ATENÇÃO: o grupo deveria ser o consumo por pessoa: quantidade // pessoas
        consumo[quantidade] = consumo.get(quantidade, 0) + pessoas

    # .items() devolve pares (chave, valor); sorted() ordena pela chave (o 1º
    # elemento do par) -> grupos em ordem crescente de consumo.
    valores = sorted(consumo.items())

    print(f"Cidade# {caso}:")

    resultado = []

    for quantidade, pessoas in valores:
        resultado.append(f"{pessoas}-{quantidade}")
    print(" ".join(resultado))

    media = totalconsumo / totalpessoas

    # Trunca em 2 casas (o problema pede SEM arredondar).
    media = math.floor(media * 100) / 100

    # ATENÇÃO (formato): a linha termina com ponto ("m3."), e a linha em
    # branco vai ENTRE as cidades, não depois de cada uma.
    print(f"Consumo medio: {media:.2f} m3")
    print()

    caso += 1

    

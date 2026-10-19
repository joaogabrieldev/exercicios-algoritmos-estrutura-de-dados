# ======================================================================
# beecrowd 1023 - Estiagem  |  Agrupamento  (2ª tentativa)
# Objetivo: agrupar os moradores pelo consumo POR PESSOA (arredondado
#           para baixo), listar os grupos em ordem crescente e mostrar o
#           consumo médio da cidade TRUNCADO em 2 casas.
# Entrada: vários casos; termina com "0" (sentinela).
# Exemplo: imóveis "3 22", "2 11", "3 39" -> "2-5 3-7 3-13"
# ======================================================================
#
# Esta versão corrige a interpretação da 1ª tentativa (Aula_6.1.py):
# "quantidade" é o consumo TOTAL do imóvel.
# Sem import aqui, mas a correção da média precisa de "import math" no
# topo (veja math.floor no Aula_6.1.py).
# Obs.: com até 10^6 imóveis, input() pode ficar lento no beecrowd.
#
# Correções necessárias (marcadas abaixo):
#   1) consumo.get com a chave errada;
#   2) média arredondada em vez de truncada, e um espaço a mais no formato;
#   3) falta o ponto em "m3.";
#   4) linha em branco no lugar errado.
caso = 1

while True:
    N = int(input())

    if N == 0:
        break
    # Agrupamento: consumo por pessoa -> total de pessoas nesse grupo.
    consumo= {}
    totalpessoas = 0
    totalconsumo = 0
    for _ in range(N):
        pessoas, quantidade = map(int, input().split())

        totalpessoas += pessoas
        # Certo agora: soma o consumo TOTAL do imóvel.
        totalconsumo += quantidade

        # // é a divisão inteira: já arredonda para baixo (22 // 3 == 7).
        consumoporpessoa = quantidade //pessoas
        # ATENÇÃO (bug 1): busca pela chave errada (quantidade). Ex.: os imóveis
        # "1 5" e "2 10" dão 5 por pessoa -> o esperado é 3 pessoas no grupo 5,
        # mas este código dá 2. Correto:
        #     consumo[consumoporpessoa] = consumo.get(consumoporpessoa, 0) + pessoas
        consumo[consumoporpessoa] = consumo.get(quantidade, 0) + pessoas

    # Pares (consumo, pessoas) ordenados pelo consumo, em ordem crescente.
    valores = sorted(consumo.items())
    # ATENÇÃO (bug 4): a linha em branco vai ENTRE as cidades. Correto: logo
    # antes deste print, colocar
    #     if caso > 1:
    #         print()
    # e apagar o print() solto do fim.
    print(f"Cidade# {caso}:")
    resultado = []

    for consumomedio, pessoas in valores:
        resultado.append(f"{pessoas}-{consumomedio}")

    print(" ".join(resultado))

    # ATENÇÃO (bug 2): o problema pede a média TRUNCADA. Correto, logo depois
    # desta linha (com "import math" no topo):
    #     media = math.floor(media * 100) / 100
    media = totalconsumo / totalpessoas

    # ATENÇÃO (bugs 2 e 3): "{media: .2f}" tem um espaço antes do ".2f", que
    # imprime um espaço na frente do número; e falta o ponto em "m3.". Correto:
    #     print(f"Consumo medio: {media:.2f} m3.")
    print(f"Consumo medio: {media: .2f} m3")

    # ATENÇÃO (bug 4): este print() deve sair (veja o comentário do "Cidade#").
    print()

    caso += 1
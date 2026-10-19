# ======================================================================
# beecrowd 1119 - A Fila do Desemprego  |  Fila Aplicada
# Objetivo: N pessoas em roda. Um oficial conta k pessoas no sentido
#           1 -> N; outro conta m pessoas no sentido N -> 1, AO MESMO TEMPO.
#           Os dois escolhidos saem juntos (se for a mesma pessoa, sai só ela).
# Entrada: "n k m" por linha; termina com "0 0 0" (sentinela).
# Saída: cada número com largura 3, rodadas separadas por vírgula.
#        Ex.: "  4  8,  9  5,  3  1,  2  6, 10,  7"
# ======================================================================
#
# Sem import. Conceitos usados:
#   %          -> faz a contagem "dar a volta" na roda (lista circular)
#   list.pop(i)-> remove o elemento do índice i; os seguintes andam uma
#                 posição para a esquerda. O(n), ok porque n < 20.
#
# ATENÇÃO: este arquivo NÃO RODA do jeito que está (NameError). Os bugs
# estão marcados abaixo, com a versão corrigida do bloco principal.
while True:
    n,k,m = map(int, input().split())

    if n == 0 and k == 0 and m == 0:
        break
    # A roda: lista com as pessoas 1..n. Quem sai é removido com pop(índice).
    pessoas = list(range(1, n + 1))

    # Oficial 1 começa na pessoa 1 (índice 0); oficial 2 na pessoa n (índice n-1).
    pos_k = 0
    pos_m = n - 1

    resultado = []

    # Cada volta deste while é uma rodada de escolha.
    while pessoas:
        # Anda k-1 casas para frente (a pessoa onde ele está já conta como a 1ª).
        # O % len(pessoas) faz a contagem dar a volta na roda.
        pos_k = (pos_k + k -1 ) % len(pessoas)

        # Mesmo raciocínio, para trás. Em Python, % de número negativo dá positivo
        # (-1 % 5 == 4), então andar para trás também dá a volta na roda.
        pos_m = (pos_m - (m-1)) % len(pessoas)

        pessoas_k = pessoas[pos_k]
        # ATENÇÃO (bug): pessoas_m ainda não existe aqui -> NameError.
        # Correto: pessoas_m = pessoas[pos_m]
        pessoas_m = pessoas[pessoas_m]

        # ATENÇÃO (bugs neste bloco):
        #  - largura: o problema pede :3d, não :2d;
        #  - o "else" lá embaixo está aninhado no "if pessoas:", mas deveria ser o
        #    else DESTE if (quando os oficiais escolhem pessoas diferentes);
        #  - "appned" está escrito errado (o certo é append), e o par deve entrar
        #    junto, num item só: f"{pessoas_k:3d}{pessoas_m:3d}";
        #  - depois de remover, quem vem depois anda um índice para a esquerda,
        #    então as posições dos oficiais precisam ser ajustadas.
        # Versão corrigida deste bloco (testada contra uma solução aceita):
        #     if pessoas_k == pessoas_m:
        #         resultado.append(f"{pessoas_k:3d}")
        #         pessoas.pop(pos_k)
        #         pos_m = pos_k - 1          # oficial 2 recomeça no anterior
        #     else:
        #         resultado.append(f"{pessoas_k:3d}{pessoas_m:3d}")
        #         if pos_k > pos_m:          # remove primeiro o MAIOR índice
        #             pessoas.pop(pos_k)
        #             pessoas.pop(pos_m)
        #             pos_k -= 1
        #             pos_m -= 1
        #         else:
        #             pessoas.pop(pos_m)
        #             pessoas.pop(pos_k)
        #             pos_m -= 2
        #     if pessoas:
        #         pos_k %= len(pessoas)
        #         pos_m %= len(pessoas)
        if pessoas_k == pessoas_m:
            resultado.append(f"{pessoas_k:2d}")

            pessoas.pop(pos_k)

            if pessoas:
                pos_k %=len(pessoas)
            else:
                resultado.appned(f"{pessoas_k:2d}")
                resultado.appned(f"{pessoas_m:2d}")

                if pos_k > pos_m:
                    pessoas.pop(pos_k)
                    pessoas.pop(pos_m)
                else:
                    pessoas.pop(pos_k)
                    pessoas.pop(pos_m)

                if pessoas:
                    pos_k %= len(pessoas)
                    pos_m %= len(pessoas)
    # Rodadas separadas por vírgula (a largura 3 já cria o espaçamento).
    print(",".join(resultado))
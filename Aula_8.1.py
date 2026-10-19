# ======================================================================
# beecrowd 1087 - Dama  |  na lista da prova: "Processamento de Strings"
# Objetivo: menor número de movimentos de uma dama do xadrez para ir de
#           (X1, Y1) até (X2, Y2).
# Entrada: vários casos; termina com "0 0 0 0" (sentinela).
# ======================================================================
#
# IDEIA (modelagem): a resposta só pode ser 0, 1 ou 2.
#   0 -> já está no destino
#   1 -> mesma linha, mesma coluna ou mesma diagonal
#   2 -> qualquer outro caso (vai até a linha do destino, depois até a coluna)
# Função nativa: abs(x) -> valor absoluto (tira o sinal): abs(-3) == 3
while True:
    X1, Y1, X2, Y2 = map(int, input().split())

    if X1 == 0 and Y1 ==  0 and X2 == 0 and Y2 == 0:
        break
    # Mesma casa: 0 movimentos.
    if X1 == X2 and Y1 == Y2:
        print(0)
    # Mesma linha ou mesma coluna: 1 movimento.
    elif X1 == X2 or Y1 == Y2:
        print(1)
    # Mesma diagonal: andou o mesmo tanto na horizontal e na vertical.
    # abs() tira o sinal, então vale para as 4 diagonais.
    elif abs(X1 - X2) == abs(Y1 - Y2):
        print(1)
    # Qualquer outro caso: sempre dá em 2.
    else:
        print(2)
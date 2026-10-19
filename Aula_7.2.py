# ======================================================================
# beecrowd 1236 - Compressão de Strings  |  Varredura de Strings
# Objetivo: 3 ou mais zeros seguidos viram "#" + chr(quantidade);
#           3 ou mais espaços seguidos viram "$" + chr(quantidade).
#           1 ou 2 repetições ficam como estão. Acima de 255, quebra em
#           blocos de 255 (um caractere só guarda valores até 255).
# Entrada: número de casos no início; uma linha de texto por caso.
# ======================================================================
#
# FUNÇÕES (nativas, sem import):
#   chr(n)         -> caractere de código n (chr(5) = caractere de código 5)
#   ord(c)         -> o contrário: ord('A') == 65
#   "0" * 3        -> "000" (multiplicar uma string repete o texto)
#   "".join(lista) -> junta os pedaços numa string só (mais eficiente do
#                     que concatenar com + dentro do laço)
#
# TÉCNICA: varredura com dois marcadores (compressão RLE, run-length):
#   inicio = onde a sequência começa; o while avança i até ela acabar;
#   quantidade = i - inicio = tamanho da sequência.
#
# ATENÇÃO (codificação): o print padrão escreve em UTF-8, e um chr() acima
# de 127 vira 2 bytes; o juiz espera 1 byte. Correto, no topo do arquivo:
#     import sys
#     sys.stdin.reconfigure(encoding="latin-1")
#     sys.stdout.reconfigure(encoding="latin-1")
N = int(input())

for _ in range(N):
    texto = input()
    resultado = []
    # i percorre o texto; quem avança o i são os whiles internos ou o else.
    i = 0

    while i < len(texto):
        # Achou um zero: mede o tamanho da sequência de zeros.
        if texto[i] == "0":
            inicio = i

            while i < len(texto) and texto[i] == "0":
                i += 1
            quantidade = i - inicio

            # ATENÇÃO (bug): o while dos blocos de 255 está dentro do "if >= 3". Com
            # 256 zeros sai "#"+chr(255) e depois "#"+chr(1), mas o resto 1 deveria
            # sair como "0". Correto: o while vem ANTES do if, fora dele:
            #     while quantidade > 255:
            #         resultado.append('#')
            #         resultado.append(chr(255))
            #         quantidade -= 255
            #     if quantidade >= 3:
            #         resultado.append('#')
            #         resultado.append(chr(quantidade))
            #     else:
            #         resultado.append('0' * quantidade )
            if quantidade >= 3:
                while quantidade > 255:
                    resultado.append('#')
                    resultado.append(chr(255))

                    quantidade -= 255
                resultado.append('#')
                resultado.append(chr(quantidade))
            else:
                resultado.append('0' * quantidade )
        #Referente aos espaços
        # ATENÇÃO (bug): este bloco foi copiado do bloco dos zeros e não foi
        # adaptado. "" é a string VAZIA (nunca é igual a um caractere), então este
        # elif nunca entra e os espaços nunca são comprimidos. Correto:
        #     elif texto[i] == " ":
        # e trocar "0" por " " no while e no '0' * quantidade. O mesmo ajuste do
        # while de 255 do bloco dos zeros vale aqui.
        # Dica (DRY): uma função comprimir(caractere, marcador) chamada duas vezes
        # evitaria esse tipo de erro de copiar e colar.
        elif texto[i] == "":
            inicio = i

            while i < len(texto) and texto[i] == "0":
                i += 1
            quantidade = i - inicio

            if quantidade >= 3:
                while quantidade > 255:
                    resultado.append('$')
                    resultado.append(chr(255))

                    quantidade -= 255
                resultado.append('$')
                resultado.append(chr(quantidade))
            else:
                resultado.append('0' * quantidade )
        # Qualquer outro caractere é copiado como está, e o i avança 1.
        else:
            resultado.append(texto[i])
            i += 1
    # Junta os pedaços uma vez só, no fim.
    print(''.join(resultado))
            
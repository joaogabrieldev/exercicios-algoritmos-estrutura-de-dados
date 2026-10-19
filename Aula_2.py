# ======================================================================
# beecrowd 1068 - Balanço de Parênteses I  |  Pilha
# Objetivo: dizer se os parênteses de cada expressão estão balanceados.
# Entrada: uma expressão por linha, até acabar o arquivo (EOF).
# ======================================================================
#
# ESTRUTURA: pilha (LIFO - o último que entra é o primeiro que sai).
# Em Python, uma list funciona como pilha (sem import):
#   pilha.append(x) -> empilha no fim          O(1)
#   pilha.pop()     -> desempilha do fim       O(1)
#   pilha[-1]       -> olha o topo sem tirar   O(1)
while True:
    # try/except EOFError: lê até a entrada acabar. Quando não há mais linhas,
    # input() lança EOFError e o except (no fim do arquivo) faz o break.
    try:
        expressao = input()
        # Pilha e flag começam zeradas a cada expressão.
        pilha = []
        correta = True 

        for caractere in expressao:

            # "(" abre um grupo: empilha.
            if caractere == '(':
                pilha.append(caractere)

            # ")" fecha o grupo aberto mais recente: desempilha.
            elif caractere == ')':

                # Pilha vazia = fechou sem ter aberto -> incorreta. O break para de ler o resto.
                if len(pilha) == 0:
                    correta = False
                    break
                pilha.pop()
        # Correta só se nunca fechou sem abrir E não sobrou nenhum "(" aberto.
        # Os outros caracteres (letras, + - * /) são ignorados pelo for.
        if correta and len(pilha) == 0:
            print("correct")
        else:
            print("incorrect")
    except EOFError:
        break

# ======================================================================
# beecrowd 1077 - Infixa para Posfixa  |  Pilha com notação matemática
# Objetivo: converter "(A*2+c-d)/2" em "A2*c+d-2/" (notação polonesa reversa).
# Entrada: número de casos no início; uma expressão por linha.
# ======================================================================
#
# ALGORITMO Shunting-yard (Dijkstra), com uma pilha de operadores:
#   1) operando (letra/dígito) -> vai direto para a saída
#   2) "("                     -> empilha
#   3) ")"                     -> desempilha para a saída até achar o "(",
#                                 e descarta o "("
#   4) operador                -> antes de empilhar, desempilha do topo tudo
#                                 que tiver prioridade MAIOR OU IGUAL
#   5) fim da expressão        -> esvazia a pilha na saída
# Sem import. str.isalnum() devolve True se o caractere é letra ou dígito.
#
# ATENÇÃO: este arquivo TRAVA do jeito que está (laço infinito). Bugs abaixo.
#
# Prioridade de cada operador: ^ (3) > * / (2) > + - (1).
def prioridade(operador):
    if operador == "^":
        return 3
    # ATENÇÃO (bug): um caractere não pode ser "*" E "/" ao mesmo tempo, então
    # estes dois ifs nunca são verdadeiros e tudo fica com prioridade 0.
    # Correto (com "or"):
    #     if operador == "*" or operador == "/":
    #     if operador == "+" or operador == "-":
    if operador == "*" and operador == "/":
        return 2
    if operador == "+" and operador == "-":
        return 1
    return 0

N = int(input())

for _ in range(N):
    expressao = input().strip()

    pilha = []
    saida = []

    for caractere in expressao:
        # isalnum(): True se for letra ou dígito = operando -> direto para a saída.
        if caractere.isalnum():#analisa boleans (numeros)
            saida.append(caractere)
        # "(" marca o início de um grupo: empilha.
        elif caractere == "(":
            pilha.append(caractere)
        # ")": desempilha até achar o "(" e depois descarta o "(" (o if pilha: pilha.pop()).
        elif caractere == ")":
            while pilha and pilha[-1] != "(":
                saida.append(pilha.pop())
            if pilha:
                pilha.pop()
        # Operador: tira do topo os de prioridade >= (eles precisam sair antes) e
        # depois empilha este. pilha[-1] é o topo; o "and" para na 1ª condição
        # falsa, então pilha[-1] só é lido se a pilha não estiver vazia.
        else:
            while (
                pilha
                and pilha[-1] != "("
                and prioridade(pilha[-1]) >= prioridade(caractere)
            ):
                saida.append(pilha.pop())
            pilha.append(caractere)
        # ATENÇÃO (bugs):
        #  1) este while está DENTRO do for (8 espaços), então esvazia a pilha a
        #     cada caractere. Ele deve ficar FORA do for, com 4 espaços;
        #  2) pilha.pop sem () coloca a FUNÇÃO na saída e não remove nada: a
        #     pilha nunca esvazia -> laço infinito.
        # Correto (alinhado com o "for caractere", logo antes do print):
        #     while pilha:
        #         saida.append(pilha.pop())
        while pilha:
            saida.append(pilha.pop)
    # Junta a lista de caracteres numa string só.
    print("".join(saida))
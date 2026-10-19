# ======================================================================
# beecrowd 1022 - TDA Racional  |  Modelagem Matemática
# Objetivo: fazer uma operação entre duas frações e mostrar o resultado e
#           a forma simplificada. Ex.: "1 / 2 - 3 / 4" -> "-2/8 = -1/4"
# Entrada: número de casos no início; uma operação por linha.
# ======================================================================
#
# BIBLIOTECA math (padrão do Python):
#   gcd(a, b) -> MDC (máximo divisor comum): gcd(12, 18) == 6
#   - ignora o sinal: gcd(-2, 8) == 2 (o abs() abaixo é redundante, mas
#     não atrapalha)
#   - dividir numerador e denominador pelo MDC dá a fração irredutível
#   Sem a biblioteca, pelo algoritmo de Euclides:
#       def mdc(a, b):
#           while b:
#               a, b = b, a % b
#           return abs(a)
from math import gcd

N = int(input())

for _ in range(N):

    # "1 / 2 + 3 / 4".split() vira 7 pedaços. O "_" é o nome convencional para
    # "valor que não interessa" (aqui, as barras).
    n1, _, d1, operador, n2, _, d2 = input().split()

    n1 = int(n1)
    d1 = int(d1)
    n2 = int(n2)
    d2 = int(d2)

    # Fórmulas da escola:
    #   a/b + c/d = (a*d + c*b) / (b*d)      a/b - c/d = (a*d - c*b) / (b*d)
    #   a/b * c/d = (a*c) / (b*d)            a/b / c/d = (a*d) / (b*c)
    #   (dividir = multiplicar pelo inverso)
    if operador == "+":
        numerador = n1 * d2 + n2 * d1
        denominador = d1 * d2
    elif operador == "-":
            numerador = n1 * d2 - n2 * d1
            denominador = d1 * d2
    elif operador == "*":
            numerador = n1 * n2 
            denominador = d1 * d2
    else:
        numerador = n1 * d2 
        denominador = d1 * n2

    # Guarda o resultado ANTES de simplificar: o problema imprime as duas formas.
    originalnumerador = numerador
    originaldenominador = denominador

    # MDC do numerador e do denominador.
    divisor = gcd(
          abs(numerador),
          abs(denominador)
    )

    # // é a divisão inteira; aqui é exata, porque o MDC divide os dois.
    numerador //= divisor
    denominador //=divisor

    # Se o denominador ficou negativo, passa o sinal para o numerador.
    if denominador < 0:
          numerador *= -1
          denominador *= -1

    # Duas f-strings seguidas são juntadas automaticamente pelo Python.
    print(
          f"{originalnumerador}/{originaldenominador} = "
          f"{numerador}/{denominador}"
    )
        
from bisect import bisect_left

while True:
    N, Q = map(int, input().split())
    
    if N == 0 and Q == 0:
        break

    codigos = []
    for _ in range(N):
        codigos.append(N)

    for _ in range(Q):
        numero = int(input())
        

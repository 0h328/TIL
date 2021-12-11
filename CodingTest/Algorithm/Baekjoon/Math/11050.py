import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())

def fact(N):
    if N <= 1:
        return 1

    return N * fact(N-1)

print(fact(N) // (fact(K) * fact(N-K)))
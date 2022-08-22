import sys
sys.stdin = open('input.txt')

def fact(N):
    num = 1
    for i in range(1, N+1):
        num *= i
    return num

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    bridge = fact(M) // (fact(N) * fact(M-N))

    print(bridge)
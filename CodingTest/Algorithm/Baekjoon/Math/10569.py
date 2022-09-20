import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    V, E = map(int, input().split())
    K = 2 - V + E
    print(K)
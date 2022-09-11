import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    N = list(map(int, input().split()))
    N.remove(max(N))
    N.remove(min(N))
    if max(N) - min(N) >= 4:
        print('KIN')
    else:
        print(sum(N))
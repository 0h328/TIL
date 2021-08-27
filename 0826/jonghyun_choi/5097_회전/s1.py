import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    print('#{} {}'.format(case + 1, data[M % N]))
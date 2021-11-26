import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))
    print('#{} {}'.format(tc, num[M % N]))
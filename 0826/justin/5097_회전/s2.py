import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    ans = arr[M % N]                     # M을 N으로 나눈 나머지 활용
    print('#{} {}'.format(tc, ans))
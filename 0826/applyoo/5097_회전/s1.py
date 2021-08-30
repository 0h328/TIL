import sys
sys.stdin = open('input.txt')

T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(test+1, arr[M % N]))

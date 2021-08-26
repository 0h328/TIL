import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N: 숫자의 개수, M: 이동 할 횟수
    Q = input().split()

    for i in range(M):
        Q.append(Q.pop(0))
    ans = Q.pop(0)
    print('#{} {}'.format(tc, ans))
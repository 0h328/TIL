import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    front = rear = -1

    for _ in range(M):
        Q.append(Q[front+1])
        Q.pop(0)

    print('#{} {}'.format(tc, Q[0]))
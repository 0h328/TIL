import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    data = input().split()
    front = -1

    while front < M - 1:
        front += 1
        data.append(data[front])

    ans = data[front+1]

    print('#{} {}'.format(tc, ans))
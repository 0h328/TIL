import sys

sys.stdin = open('input.txt')
from collections import deque


def sol():
    move = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    queu = deque()
    queu.append((0, 0))
    while queu:
        x, y = queu.popleft()
        for i in range(4):
            nx = x + move[i][0]
            ny = y + move[i][1]
            if 0 <= nx < N and 0 <= ny < N:
                plus = 0
                if data[nx][ny] > data[x][y]: # 차이 값 가중치 구하기 위해서
                    plus = data[nx][ny] - data[x][y]
                if temp[nx][ny] > temp[x][y] + plus + 1: # 최소값으로 갱신
                    temp[nx][ny] = temp[x][y] + plus + 1
                    queu.append((nx, ny)) # 갱신될때만 탐색하면 된다.
    return temp[N - 1][N - 1] # 마지막 위치가 결국 도착지까지의 최소값


for test in range(1, 1 + int(input())):
    N = int(input())
    data = list(list(map(int, input().split())) for _ in range(N))
    temp = [[1e9] * N for _ in range(N)] # G처럼 초기화 시켜주고 여기다가 각 이동할 수 있는 최소비용 갱신
    temp[0][0] = 0

    answer = sol()
    print(temp)

    print('#{} {}'.format(test, answer))

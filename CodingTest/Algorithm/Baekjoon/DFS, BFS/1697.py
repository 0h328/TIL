from collections import deque
import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
v = [-1] * 100001   # -1로 한 이유는 출발 지점을 0초로 바꾸기 위해
q = deque()
q.append(N)
v[N] = 0    # 출발지점 0초로 맞춤
cnt = 0     # 몇초만에 가는지?

while q:

    s = q.popleft()

    moves = [s-1, s+1, s*2] # 1초 후에 X-1, X+1, 2*X 위치로 이동

    if s == K:  # 도착지에 도착하면 종료
        break

    for move in moves:
        if 0 <= move <= 100000 and v[move] == -1:   # 시간초과 조건 & 미방문 조건
            q.append(move)
            v[move] = v[s] + 1  # 다음 이동하는 곳으로 +1초

print(v[K])
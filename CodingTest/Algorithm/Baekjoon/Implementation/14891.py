# 톱니바퀴
from collections import deque
import sys
sys.stdin = open('input.txt')

def left(num, direction):
    if num < 0: # 톱니바퀴의 인덱스 번호는 0~3이므로 범위 밖이면 종료
        return
    if q[num][2] != q[num+1][-2]:   # 양쪽 인접 바퀴(idx는 2와 6) 같음여부 확인 (탐색들어온 바퀴 번호 기준)
        left(num-1, -direction)     # 방향은 다시 반대로
        q[num].rotate(direction)

def right(num, direction):
    if num > 3: # 톱니바퀴의 인덱스 번호는 0~3이므로 범위 밖이면 종료
        return
    if q[num][-2] != q[num-1][2]:   # 양쪽 인접 바퀴(idx는 2와 6) 같음여부 확인 (탐색들어온 바퀴 번호 기준)
        right(num+1, -direction)    # 방향은 다시 반대로
        q[num].rotate(direction)

q = []
for _ in range(4):
    q.append(deque(list(input())))

K = int(sys.stdin.readline())

for i in range(K):
    n, d = map(int, sys.stdin.readline().split())    # 1: 시계, -1: 반시계
    left(n-2, -d)       # 왼쪽 바퀴 탐색, 방향은 반대로
    right(n, -d)        # 오른쪽 바퀴 탐색, 방향은 반대로
    q[n-1].rotate(d)    # 처음 기준 바퀴 회전

score = 0
if q[0][0] == '1': score += 1
if q[1][0] == '1': score += 2
if q[2][0] == '1': score += 4
if q[3][0] == '1': score += 8

print(score)
import sys
sys.stdin=open('input.txt')
"""
1. 대각선 방향을 정한다.
2. 도는동안의 값들을 저장하는 스택을 하나 만든다
3. 다 돌면 스택의 정보를 확인한다
4. 중복하는 값이 없다면 일단 길이를 구한다.
5. answer와 비교하고 최댓값을 갱신한다.
"""
from collections import deque
move = [(1,1),(1,-1),(-1,-1),(-1,1)]

def BFS(start):
    queu=deque()
    queu.append(start)
    visit = []

    while queu:
        x,y = queu.popleft()
        for dx,dy in move:


for test in range(1,1+int(input())):
    N = int(input())
    data = list(list(map(int,input().split())) for _ in range(N))

    for i in range(1,N-1):
        for j in range(1,N-1):
            start = (i,j)


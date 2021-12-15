import sys
from collections import deque
sys.stdin = open('input.txt')

N = int(input())
q = deque()

for i in range(1, N+1):
    q.append(i)

if len(q) == 1: # N이 1일때
    print(q[0]) # 1을 출력

while q:                # q가 비어있지 않을때
    q.popleft()         # 맨위(맨 왼쪽)수를 버리고
    if q:               # q가 비어있지 않으면
        a = q.popleft() # 맨위(맨 왼쪽)수를 pop하고
        q.append(a)     # 맨아래(맨 오른쪽)으로 push한다.
        if len(q) == 1: # 모든 과정 후, q에 1개 남으면
            print(q[0]) # 남은 수를 출력
            exit()      # 시스템 강제 종료






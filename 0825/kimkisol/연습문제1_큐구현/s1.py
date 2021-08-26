"""
문제1-1. 기본 Queue 구현 - 기본 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

#1. Queue 생성 (리스트)
Q = [0] * 3
front = rear = -1

#2. Queue에 데이터를 삽입
for i in range(1, 4):
    rear += 1
    Q[rear] = i

#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
for _ in range(3):
    front += 1
    print(Q[front])

"""
문제1-2. 기본 Queue 구현 - 기본 구현 (내장 모듈 활용)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""
import collections

#1. Queue 생성
Q = collections.deque()

#2. Queue에 데이터를 삽입
for i in range(10, 14):
    Q.append(i)

#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
for _ in range(3):
    print(Q.popleft())
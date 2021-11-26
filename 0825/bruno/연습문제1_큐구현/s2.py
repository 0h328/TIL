"""
문제1-2. 기본 Queue 구현 - 기본 구현 (내장 모듈 활용)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""
import queue
#1. Queue 생성
Q = queue.Queue()
print(Q.empty())
#2. Queue에 데이터를 삽입
Q.put(1)
Q.put(2)
Q.put(3)
print(Q.empty())
print(Q.qsize())
print(Q.get())
print(Q.get())
print(Q.get())
#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)

from collections import deque

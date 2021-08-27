"""
문제1-2. 기본 Queue 구현 - 기본 구현 (내장 모듈 활용)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

# 1. Queue 생성

q = queue.Queue()
print(q.empty())

# 2. Queue에 데이터를 삽입

q.put(1)
print(q.empty())
print(q.qsize())
print(q.qet())

# 3. Queue에 삽입한 데이터를 출력(First-In-First-Out)

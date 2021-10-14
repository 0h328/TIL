#엥 한거같은데 다 어디갔지,.?

"""
문제1-1. 기본 Queue 구현 - 기본 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

#1. Queue 생성 (리스트)
Queue = []
#2. Queue에 데이터를 삽입
Queue.append(1)
Queue.append(2)
Queue.append(3)
#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)1
print(Queue.pop(0))
print(Queue.pop(0))
# print(Queue.pop(0))

if Queue:
    print(Queue.pop(0))
print(Queue)
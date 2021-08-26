#1. Queue 생성 (리스트)
q=[]
#2. Queue에 데이터를 삽입
q.append(1)
q.append(2)
q.append(3)
print(q)
#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
print(q.pop(0))
print(q.pop(0))
print(q.pop(0))


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


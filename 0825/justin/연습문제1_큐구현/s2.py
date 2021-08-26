"""
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하자
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력하자
  (1, 2, 3을 차례대로 출력해야 함)
"""
import queue        #1-2. Queue 모듈
Q = queue.Queue()   # Queue 생성
print(Q.empty())    # Queue가 비어있는지 확인 -> True
Q.put(1)            # put -> Queue에 데이터 삽입
Q.put(2)
Q.put(3)
print(Q.empty())    # Queue가 비어있는지 확인 -> False
print(Q.qsize())    # 데이터의 크기 확인  -> 3
print(Q.get())      # 1
print(Q.get())      # 2
print(Q.get())      # 3
print(Q.qsize())    # 0
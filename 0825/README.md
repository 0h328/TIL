# 08/25 Queue

| No.       | Title          | Directory           |
| --------- | -------------- | ------------------- |
| 연습문제1 | 큐 구현        | `연습문제1_큐구현`  |
| 연습문제2 | BFS 구현       | `연습문제2_BFS구현` |
| 연습문제3 | 마이쭈 시뮬레이션       | `연습문제3_마이쭈` |
| 1225      | 암호생성기(HW) | `1225_암호생성기`   |



## 연습문제1

```python
"""
문제1-1. 기본 Queue 구현 - 기본 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

#1. Queue 생성 (리스트)

#2. Queue에 데이터를 삽입

#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
```

```python
"""
문제1-2. 기본 Queue 구현 - 기본 구현 (내장 모듈 활용)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

#1. Queue 생성

#2. Queue에 데이터를 삽입

#3. Queue에 삽입한 데이터를 출력(First-In-First-Out)
```

```python
"""
문제2. 기본 Queue 구현 - 클래스 구현 (가변)
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

class Queue:
    def __init__(self):
        """
        인스턴스 생성 시에 새로운 Queue 생성
        """
        pass

    def is_empty(self):
        """
        Queue에 비어있는지 여부를 True / False로 반환
        """
        pass

    def enqueue(self):
        """
        Queue에 원소 삽입
        """
        pass 
    
    def dequeue(self):
        """
        Queue에서 원소 삭제 후 반환
        """
        pass
    
    def size(self):
        """
        Queue의 길이 반환
        """
        pass


#1. Queue 인스턴스 생성

#2. Queue가 비었는지 확인

#3. 1, 2, 3 원소를 Queue 삽입

#4. 원소가 정상적으로 삽입되었는지 확인 / 사이즈 확인 / 비었는지 여부 확인

#5. Queue에서 원소 삭제 후 반환 & 원소 확인 / 사이즈 확인
```

```python
"""
문제3. 고정 배열 크기의 Queue 구현
 - 세 개의 데이터 1, 2, 3을 차례로 큐에 삽입
 - 큐에서 세 개의 데이터를 차례로 꺼내어 출력
  (1, 2, 3을 차례대로 출력)
"""

# Queue의 사이즈 지정
SIZE = 4
Q = [0] * SIZE

# 초기 상태의 표현
front, rear = -1, -1

# isFull
def is_full():
    """
    Queue가 포화상태인지 확인
    """
    pass

# isEmpty
def is_empty():
    """
    Queue가 공백상태인지 확인
    """
    pass

# enQueue
def enqueue(item):
    """
    Queue의 뒤쪽(rear 다음)에 원소를 삽입
    - rear를 뒤쪽으로 옮기고 (rear + 1)그 자리에 원소를 삽입
    """
	pass

# deQueue
def dequeue():
    """
    Queue의 앞쪽(front)에서 원소를 삭제하고 반환
    - front를 뒤쪽으로 옮기고(front + 1) 그 자리에 있는 원소를 반환하며 삭제
    """
	pass

# Qpeek
def Qpeek():
    """
    Queue의 앞쪽(front)의 한 자리뒤(front+1)에서 원소를 삭제없이 반환
    - front의 값을 단순하게 증가시켜 가져온다. (큐의 첫 번째 원소 반환)
    - 이때 중요한 것은 dequeue와 다르게 front의 값 자체를 '변경'하지 않는다는 점
     - front += 1은  front + 1과 다름
    """
	pass


#1. Queue 초기화 상태 확인
print(Q)

#2. Queue가 비었는지 확인
print(is_empty()) # True

#3. enQueue 작업 & 확인
enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
enqueue(5) # Queue is full!

print(Q)

#4. Qpeek
print(Qpeek())

#5. deQueue 작업 & 확인
print(dequeue()) # 1
print(dequeue()) # 2
print(dequeue()) # 3
print(dequeue()) # 4
print(dequeue()) # Queue is empty!


"""
1) 기본 개념
선형 큐 기본
- 큐의 크기 == 배열의 크기
- front: 마지막에 꺼내진 원소의 인덱스
- rear: 저장된 마지막 원소의 인덱스

초기 상태
front, rear = -1, -1

공백 상태
 - front = rear

포화 상태
 - Queue가 전부 찼을 때
 - rear = n - 1 (n: 배열의 크기, n-1: 배열의 마지막 인덱스)

2) 기본 Queue의 연산 과정
1. 공백 Queue 생성
    - 고정 배열에서 Queue의 사이즈를 지정
    - front와 rear의 값을 -1로 초기화
        - 이때 파이썬에서 음수 인덱스 유의
2. 원소 A 삽입
    삽입 과정은 rear의 증가
    - front → -1
    - rear → 0 (+1)
3. 원소 B 삽입
    삽입 과정은 rear의 증가
    - front → -1
    - rear → 1 (+1)
4. 원소 반환/삭제
    삭제 과정은 front의 증가
    - front → 0 (+1)
        - 이때 해당 자리에 있었던 원소 반환
    - rear → 1
5. 원소 C 삽입
    - front → 0
    - rear → 2 (+1)
6. 원소 반환/삭제
    - front → 1 (+1)
    - rear → 2
7. 원소 반환/삭제
    - front → 2 (+1)
    - rear → 2
    - front와 rear가 같아진다? → 공백 상태
"""
```



## 연습문제2

```python
# input.txt

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
```

```python
"""
1. bfs - 인접 행렬 구현
"""

def bfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# bfs 탐색 시작
bfs(1)
```

```python
"""
2. bfs - 인접 리스트 구현
"""

def bfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# bfs 탐색 시작
bfs(1)
```

```python
"""
3. bfs - 인접 딕셔너리 구현
"""

def bfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# bfs 탐색 시작
bfs(1)
```

```python
"""
4. bfs - 1번 노드에서 가장 멀리 떨어진 노드 찾기 (거리에 대한 정보 담아 놓기)
"""

def bfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# bfs 탐색 시작
bfs(1)
```


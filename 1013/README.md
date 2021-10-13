# 10/13 그래프

| No.  | Title       | Directory         |
| ---- | ----------- | ----------------- |
| | Stack 직접 구현 (복습) | `연습문제_1` |
| | Queue 직접 구현 (복습) | `연습문제_2` |
| | DFS 구현 (복습) | `연습문제_3` |
| | BFS 구현 (복습) | `연습문제_4` |
| | Disjoint Set (`연습문제5` 폴더 내부를 복사해서 사용) | `연습문제_5` |
| | MST (Prim) (`연습문제6` 폴더를 내부 복사해서 사용) | `연습문제_6` |
| | MST (Kruskal) (`연습문제7` 폴더 내부 복사해서 사용) | `연습문제_7` |
| | Dijkstra (`연습문제8` 폴더 내부 복사해서 사용) | `연습문제_8` |
| 2814 | 최장경로(HW) | `2814_최장경로` |



## 연습문제_1

```python
"""
연습 문제1. 고정 배열로 Stack 구현
"""
SIZE = 5             # 크기가 5인 배열을 생성하기 위한 변수 초기화
top = -1             # top의 기본값
stack = [0] * SIZE   # 5 크기의 배열 생성

def push(item):
    global top, stack
    pass

def pop():
    global top, stack
    pass

print(stack)      # [0, 0, 0, 0, 0]
push(1)
push(2)
push(3)
push(4)
push(5)
push(6)           # Stack is Full!
print(stack)      # [1, 2, 3, 4, 5]

item = pop()
print(item) # 5
item = pop()
print(item) # 4
item = pop()
print(item) # 3
item = pop()
print(item) # 2
item = pop()
print(item) # 1
item = pop()
print(item) # Stack is Empty!
```



## 연습문제_2
```python
"""
연습 문제2. 고정 배열로 Queue 구현
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



## 연습문제_3
```python
# input.txt

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
```
```python
"""
연습 문제3. DFS 구현 (인접 행렬/인접 리스트/인접 딕셔너리)
"""

def dfs(v):
    pass


import sys
sys.stdin = open('input.txt')

# V(ertex), E(dge)

# 간선 정보 초기화

# Graph 초기화

# 방문 표시 초기화

# dfs 탐색 시작
dfs(1)
```



## 연습문제_4
```python
# input.txt

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
```
```python
"""
연습 문제4. BFS 구현 (인접 행렬/인접 리스트/인접 딕셔너리)
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



## 연습문제_5

`연습문제5~8` 폴더 내부에 있는 자료를 확인해주세요.

```python
"""
연습문제 5. 
"""
```



## 연습문제_6

`연습문제5~8` 폴더 내부에 있는 자료를 확인해주세요.

```python
"""
연습문제 6. 
"""
```



## 연습문제_7

`연습문제5~8` 폴더 내부에 있는 자료를 확인해주세요.

```python
"""
연습문제 7. 
"""
```



## 연습문제_8

`연습문제5~8` 폴더 내부에 있는 자료를 확인해주세요.

```python
"""
연습문제 8. 
"""
```
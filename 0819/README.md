# 08/19 Stack 1 - 문제풀이

| No.  | Title             | Directory               |
| ---- | ----------------- | ----------------------- |
|  | DFS 구현 | `연습문제_3` |
|  | function call + recursive call (푸는 문제 아님 -> 학습용) | `연습문제_4` |
|  | memoization (푸는 문제 아님 -> 학습용) | `연습문제_5` |
|  | dp (푸는 문제 아님 -> 학습용) | `연습문제_6` |
| 4869 | 종이붙이기 (DP) -> 반드시 손으로 그려서 풀어보세요! | `4869_종이붙이기` |
| 4866 | 괄호검사 | `4866_괄호검사` |
| 4871 | 그래프 경로 | `4871_그래프경로` |
| 4873 | 반복문자 지우기 | `4873_반복문자지우기` |
| 1234 | 비밀번호 | `1234_비밀번호` |
| 1219 | 길찾기(HW) | `1219_길찾기` |



## 연습문제 3

```python
# input.txt

7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
```

```python
"""
1. dfs - 인접 행렬 - 반복
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

```python
"""
2. dfs - 인접 행렬 - 재귀
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

```python
"""
3. dfs - 인접 리스트
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



## 연습문제 4 (결과 확인)

> 재귀 함수 호출시에 Stack Frame이 어떻게 형성되는지 관찰!!
> 파이썬 튜터보단 디버거를 충분히 활용하도록 연습해주세요. 😄

``` python
# 디버거를 통해 결과를 확인해보세요
# print 결과는 디버거를 실행 시켰을 때 보이는 'Console'이라는 탭에서 확인 가능합니다.

def func2():
    print('함수 2 시작')
    print('함수 2 종료')

def func1():
    print('함수 1 시작')
    func2()
    print('함수 1 종료')

print('메인시작')
func1()
print('메인끝')

"""
메인시작
함수 1 시작
함수 2 시작
함수 2 종료
함수 1 종료
메인끝
"""
```

```python
# global 영역부터 각 함수의 고유한 영역을 디버거에서 확인해보세요!

n = 10

def f1(a):
    f2(a)

def f2(b):
    f3(b)

def f3(c):
    print(c**2)

f1(n) # 100
```

```python
# 반드시 디버거를 통해 결과를 확인해주세요!

def factorial(n):
    if n == 1:                # base case -> 종료 조건
        return 1
    return n * factorial(n-1) # 인자의 크기가 1씩 줄어감

print(factorial(5))

"""
Step 1. 
|  2 * factorial(1)  |
|  3 * factorial(2)  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

Step2.
2-1.
|  2 * 1  |
|  3 * factorial(2)  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

2-2.
|    |
|  3 * 2  |
|  4 * factorial(3)  |
|  5 * factorial(4)  |
|  main  |

2-3.
|    |
|    |
|  4 * 6 |
|  5 * factorial(4)  |
|  main  |

2-4.
|    |
|    |
|    |
|  5 * 24  |
|  main  |

2-5. 
|    |
|    |
|    |
|  120 반환 |
|  main  |

2-6. 끝
|    |
|    |
|    |
|    |
|    |
"""
```

```python
# 재귀로 배열의 각 요소 출력
# 반드시 디버거를 활용하여 결과를 확인해주세요!!

a = [1, 2, 3]
N = len(a)

def f(i, N, a):
    if i == N:
        return # return None
    # else:
    print(a[i])
    f(i+1, N, a)
    # return이 없으면? None을 return

f(0, N, a)
```





## 연습문제 5 (결과 확인)

> 후반기 파트에서 다시 등장합니다.

```python
# 재귀
def fibo_recursion(num):
    # nm <= 1:
    if num == 0 or num == 1:
        return num
    return fibo_recursion(num-1) + fibo_recursion(num-2)

# print(fibo_recursion(10))
print(fibo_recursion(50))
```

```python
# 저장 공간을 만들어 놓은 상태에서 저장 (길이를 직접 지정)
def fibo(n):
    global cnt
    cnt += 1
    if memo[n] == -1:                   # 값을 아직 구하지 않은 경우
        memo[n] = fibo(n-1) + fibo(n-2)
    return memo[n]

memo = [-1] * 51 # n의 크기보다 1 크게 생성
memo[0] = 0
memo[1] = 1
cnt = 0

# print(memo)
print(fibo(50))
print(cnt)
```

```python
import time
start = time.time()

# 저장 공간을 만들어 놓은 상태에서 저장 (길이를 직접 지정)
def fibo2(n):
    global cnt
    cnt += 1
    if n >= 2 and memo2[n] == 0:        # 아직 계산되지 않은 값이면
        memo2[n] = fibo2(n-1) + fibo2(n-2)
    return memo2[n]

memo2 = [0] * 51
memo2[0] = 0
memo2[1] = 1
cnt = 0

# print(memo)
print(fibo2(50))
print(cnt)
```



## 연습문제 6 (결과 확인)

> 후반기 파트에서 다시 등장합니다. (`4869_종이붙이기`)

```python
# dp - 또보나치
def fibo_dp(num):
    # 피보나치의 하위 -> 상위 결과값이 담길 리스트(테이블) 선언
    result = [0 for _ in range(num+1)]
    # 0항과 1항 값 넣어놓기
    result[0] = 0
    result[1] = 1

    # 두 번째 항부터 시작 (0항과 1항은 미리 계산)
    for i in range(2, num+1):
        # 기존에 리스트에 저장된 값을 그대로 활용
        result[i] = result[i-2] + result[i-1]

    # 마지막 항 반환
    return result[num]

print(fibo_dp(50))
```

```python
# dp - 또토리얼
def fact(num):
    table[0] = 1

    for i in range(1, num+1):
        table[i] = i * table[i-1]

    return table[num]

n = 10
table = [0] * (n+1)
print(fact(n))
```


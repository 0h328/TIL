# 08/23 Stack2

| No.       | Title       | Directory                                  |
| --------- | ----------- | ------------------------------------------ |
| 연습문제1 | 후위표기법  | `연습문제1_후위표기법`                     |
| 연습문제2 | 부분집합    | `연습문제2_부분집합`                       |
| 연습문제3 | 퀵정렬      | `연습문제3_퀵정렬` (`1966_숫자를정렬하자`) |
| 1223      | 계산기2(HW) | `1223_계산기2`                             |

## 연습문제1

```python
# input.txt

2+3*4/5
```

```python
"""
수식 문자열을 읽어서 피연산자는 바로 출력하고 연산자는 stack에 push하여 수식이 끝나면 스택의 남아있는 연산자를 모두 pop하여 출력하시오.
(연산자는 사칙연산만 활용)

2+3*4/5 -> 2345/*+
"""

import sys
sys.stdin = open('input.txt')
```

## 연습문제 2

```python
#1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]
N = len(arr)
sel = [0] * N

def powerset(idx):
    pass

powerset(0)
```

```python
#2.
# 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
results = []

def powerset(idx):
    pass

powerset(0)
```

## 연습문제3

- 아래의 입력을 통해 연습하고 추가적으로 `1966_숫자를 정렬하자` 문제를 통해서도 채점 가능

```python
# input.txt

3 9 4 7 5 0 1 6 8 2
```

```python
def quick_sort(nums):
    pass

# 가변 배열
import sys
sys.stdin = open('input.txt')
nums = list(map(int, input().split()))
print(quick_sort(nums))
```

```python
def partition(arr, start, end):
    pass

def quick_sort(arr, start, end):
    pass

# 고정 배열
import sys
sys.stdin = open('input.txt')
numbers = list(map(int, input().split()))
print(quick_sort(numbers, 0, len(numbers)-1))
```

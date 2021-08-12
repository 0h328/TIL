# 08/12 List II - 문제풀이

| No.  | Title     | Directory       |
| ---- | --------- | --------------- |
|  | 선택정렬 | `99_선택정렬` |
|  | 순차탐색 | `99_순차탐색` |
|  | 이진탐색 | `99_이진탐색` |
| 4836 | 색칠하기 | `4836_색칠하기` |
|  2001    | 파리퇴치          | `2001_파리퇴치`           |
| 4837 | 부분집합의 합 | `4837_부분집합의합` |
| 4839 | 이진탐색 | `4839_이진탐색` |
| 4843 | 특별한 정렬 (선택정렬 연습) | `4843_특별한정렬` |
| 1945 | 간단한 소인수분해 | `1945_간단한소인수분해` |
| 1210 | Ladder1(HW) | `1210_Ladder1` |



## 99_선택정렬

```
input.txt

-2 0 4 1 3 1 2 4 -9
```

```python
def selection_sort(nums):
    pass

print(numbers)
numbers = list(map(int, input().split()))
print(numbers)
```





## 99_순차탐색

```
input.txt

-9 1 2 3 4 6 6 7 8 92
```

```python
# 정렬된 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def ordered_sequential_search(numbers, target):
    pass

numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False
```



```
input.txt

93 2 74 5 6 8 6 8 4 9
```

```python
# 정렬되지 않은 요소의 순차탐색
# 검색 대상이 리스트 안에 존재하면 True / 아니면 False
def unordered_sequential_search(numbers, target):
    pass

numbers = list(map(int, input().split()))
print(unordered_sequential_search(numbers, 9))  # True
print(unordered_sequential_search(numbers, 94))  # False
```





## 99_이진탐색

```
input.txt

1 2 3 4 5 6 6 7 8 9
```

```python
# 이진 탐색 기본

def binary_search(numbers, target):
   pass

numbers = list(map(int, input().split()))
print(binary_search(numbers, 5)) # True
print(binary_search(numbers, 10)) # False
```

```python
# 이진 탐색 재귀

def recursive_binary_search(numbers, target):
    pass

numbers = list(map(int, input().split()))
print(recursive_binary_search(numbers, 5)) # True
print(recursive_binary_search(numbers, 10)) # False
```


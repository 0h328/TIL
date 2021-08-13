# 08/13 String - 불코

| No.  | Title             | Directory               | PPT 번호 |
| ---- | ----------------- | ----------------------- | ---- |
|  | 문자열 비교 | `연습문제_1` |  |
|  | 문자열 뒤집기(반복문 & 슬라이싱) | `연습문제_2` |  |
|  | 문자열 뒤집기(재귀) | `연습문제_3` |  |
|  | atoi_itoa | `연습문제_4` |  |
|  | 고지식한 패턴검색 | `연습문제_5` |  |
| 1213 | String 활용(고지식한 패턴 검색) | `1213_String활용` |  |
| 1966 | 숫자를 정렬하자 | `1966_숫자를정렬하자` | 버블, 카운팅, 선택 정렬 복습 |
| 1221 | GNS(HW) | `1221_GNS` |  |



## 연습문제 1

> my_str1과 my_str2가 같은지 여부 확인 -> T/F

```
input.txt

abccd
abcd
```

```python
def solve(my_str1, my_str2):
    pass

import sys
sys.stdin = open('input.txt')
my_str1 = input()
my_str2 = input()

print(solve(my_str1, my_str2)) # False
```





## 연습문제 2

> 문자열을 거꾸로 뒤집기(반복문 & 슬라이싱)

```
input.txt

abcde
Reverse this strings
```

```python
def solve(word):
    pass

import sys
sys.stdin = open('input.txt')

#1. 반복문 활용
word = input()
print(solve(word)) # edcba

#2. pythonic (slicing)
word2 = input()
print(word2) # sgnirts siht esreve
```





## 연습문제 3

> 문자열을 거꾸로 뒤집기(재귀함수)

```
input.txt

tomato
banana
```

```python
def solve(word):
    pass

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab
```





## 연습문제 4

> 문자를 숫자로 변경(while & for 활용)
> 반드시 디버거 활용!

```python
# atoi (ASCII to Integer) - while

def atoi_while(my_str):
    pass

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_int1 = atoi_while(my_str)
print(my_int1, type(my_int1)) # 123, int

my_int2 = int(my_str)
print(my_int2, type(my_int2)) # 123, int
```

```python
# atoi (ASCII to Integer) - for

def atoi_for(num_str):
    pass

my_str = '123'
print(my_str, type(my_str))   # 123, str

my_str = atoi_for(my_str)
print(my_str, type(my_str))   # 123, int
```





## 연습문제 5

> 패턴이 일치하는 요소의 첫번째 인덱스 반환
> 반드시 디버거 활용!

```
input.txt

TTTTA
TTA
```

```python
def solve_while(target, pattern, N, M):
    pass

def solve_for(target, pattern, N, M):
    pass


import sys
sys.stdin = open('input.txt')
target = input()      
N = len(target)      

pattern = input()    
M = len(pattern)     


# 방법 1 - while
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
ans = solve_while(target, pattern, N, M)
print('{}'.format(ans))		# 2

# 방법 2 - for
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
ans2 = solve_for(target, pattern, N, M)
print('{}'.format(ans2))	# 2

# 방법 3 - .find() 활용
# target과 일치하는 pattern 문자가 발견되는 첫 번째 index 반환
print(target.find(pattern)) # 2
```


# 08/13 String - 불금

| No.  | Title             | Directory               | PPT 번호 |
| ---- | ----------------- | ----------------------- | ---- |
|  | 문자열 비교 | `연습문제_1` |  |
|  | 문자열 뒤집기(반복문 & 슬라이싱) | `연습문제_2` |  |
| 1213 | String 활용(고지식한 패턴 검색) | `1213_String활용` |  |
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

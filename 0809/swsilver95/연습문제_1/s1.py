import sys
sys.stdin = open('input.txt')

# 1. 숫자
num = int(input())
print('#1 {0}'.format(num))


# 2. 리스트
numbers = list(map(int, input().split()))
print('#2 {0}'.format(numbers))

# 3. 이차원 배열
# n = int(input())
# data = []
# for _ in range(n):
#     data.append(list(map(int, input().split())))
# print('#3 {0}'.format(data))


# 3-1. 조금 더 심플한 방법
n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
print('#3 {0}'.format(data))
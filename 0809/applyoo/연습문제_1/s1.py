import sys
sys.stdin = open('input.txt')

#1. 숫자
num = int(input())
print('#1 {}'.format(num))

#2. 1차원 리스트
print('#2 {}'.format(list(map(int, input().split()))))

#3 2차원 리스트
N = int(input())
arr = [[] for _ in range(N)]

for i in range(N):
    arr[i] = list(map(int, input().split()))

print('#3 {}'.format(arr))

# print([list(map(int, input().split())) for _ in range(N)])
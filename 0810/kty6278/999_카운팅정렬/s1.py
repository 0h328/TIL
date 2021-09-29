# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))

# 정렬된 리스트 -> [0, 0, 0, 0, 0, 0, 0, 0, 0]
a = [0] * len(arr)
# 카운트 리스트
b = [0] * (max(arr)+1)

# 받아온 input을 count -> [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
for i in range(0, len(a)):
    b[arr[i]] += 1

# 받이온 input을 count를 앞의 값을 포함한 값  -> [0, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 9]
for i in range(1, len(b)):
    b[i] += b[i-1]


for i in range(len(a)-1, -1, -1):
    a[b[arr[i]]-1] = arr[i]
    b[arr[i]] -= -1

print(a)




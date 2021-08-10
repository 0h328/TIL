# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')

a = list(map(int, input().split()))

# 정렬된 리스트 -> [0, 0, 0, 0, 0, 0, 0, 0, 0]
my_sort = [0] * len(a)
# 카운트 리스트
my_count = [0] * (max(a)+1)

# 받아온 input을 count -> [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1]
for i in range(0, len(my_sort)):
    my_count[a[i]] += 1

# 받이온 input을 count를 앞의 값을 포함한 값  -> [0, 1, 2, 2, 2, 3, 3, 4, 5, 6, 7, 8, 8, 8, 8, 8, 9]
for i in range(1, len(my_count)):
    my_count[i] += my_count[i-1]


for i in range(len(my_sort)-1, -1, -1):
    my_sort[my_count[a[i]]-1] = a[i]
    my_count[a[i]] -= -1

print(my_sort)
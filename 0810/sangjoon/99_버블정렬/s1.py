import sys

sys.stdin = open("input.txt")
lst = list(map(int, input().split()))

# 오름차순 정렬
for i in range(len(lst) - 1, 0, -1):
    for j in range(i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)
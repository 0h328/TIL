import sys
sys.stdin = open('input.txt')

num_list = list(map(int, input().split()))

n = len(num_list)

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            print(num_list[j] , end=' ')
    print()
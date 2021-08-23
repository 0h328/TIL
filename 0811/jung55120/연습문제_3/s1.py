import sys
sys.stdin = open('input.txt')

num_list = list(map(int, input().split()))
N = len(num_list)

for i in range(1, 1 << N):
    for j in range(N):
        if i & (1 << j) :
            print(num_list[j], end=' ')
    print()

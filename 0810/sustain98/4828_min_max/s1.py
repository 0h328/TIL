import sys
sys.stdin = open('input.txt')

t = int(input())

for idx in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    maxi = 0
    mini = float('inf')

    for i in n_list:
        if mini > i:
            mini = i
        if maxi < i:
            maxi = i
    print('#{} {}'.format(idx, maxi - mini))
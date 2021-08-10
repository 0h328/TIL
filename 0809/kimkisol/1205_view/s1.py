import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for i in range(1, 11):
    T = int(input())
    homes = list(map(int, input().split()))
    cnt = 0
    for idx in range(2, len(homes) - 2):
        if homes[idx] < homes[idx - 1] or homes[idx] < homes[idx - 2] or homes[idx] < homes[idx + 1] or homes[idx] < homes[idx + 2]:
            continue
        cnt += homes[idx] - max(homes[idx - 2: idx] + homes[idx + 1: idx + 3])
    print('#{0} {1}'.format(i, cnt))
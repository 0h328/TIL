import sys
sys.stdin = open("input.txt")

# A = {1~12까지의 숫자}
T = int(input())
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        sub_set = []
        for j in range(12):
            if i & (1 << j):
                sub_set.append(numbers[j])
        # print(sub_set)
        if len(sub_set) == N and sum(sub_set) == K:
            cnt += 1

    print(cnt)


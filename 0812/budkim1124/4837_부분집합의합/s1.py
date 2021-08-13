import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(1, T+1):
    N, K = list(map(int, input().split()))
    lst = list(range(1,13))
    cnt = 0

    for i in range(1, 1 << len(lst)):
        num_list = []
        for j in range(len(lst)):
            if i & (1 << j):
                num_list.append(lst[j])
        if sum(num_list) == K and len(num_list) == N:
            cnt += 1
    print("#{} {}".format(num, cnt))




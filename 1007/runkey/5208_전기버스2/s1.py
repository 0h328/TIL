import sys
sys.stdin = open('input.txt')

tc = int(input())

for t in range(1, tc + 1):
    result = 0
    N_list = list(map(int, input().split()))
    cnt = N_list[1]
    idx = 2
    while idx < len(N_list):
        max_i = 0
        for i in range(idx, idx + cnt):
            if i >= len(N_list):
                break
            if max_i < N_list[i]:
                max_i = N_list[i]

        idx += max_i
        if idx < len(N_list):
            cnt = N_list[idx]
        result += 1
    print("#{} {}".format(t, result))
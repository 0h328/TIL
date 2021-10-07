import sys
sys.stdin = open('input.txt')

tc = int(input())

for t in range(1, tc + 1):
    N, M = map(int, input().split())
    N_list = list(map(int, input().split()))
    M_list = list(map(int, input().split()))

    for m in M_list:
        l = 0
        r = len(N_list) - 1
        while l < r:
            if N_list[l] < N_list[r]:
                break
    result = arr[N//2]
    print("#{} {}".format(t, result))
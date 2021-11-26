import sys
import heapq
sys.stdin = open('input.txt')

tc = int(input())
for t in range(1, tc + 1):
    result = 0
    N = int(input())
    N_list = list(map(int, input().split()))
    heapq.heapify(N_list)

    while N > 1:
        N //= 2
        result += N_list[N - 1]
    print("#{} {}".format(t, result))
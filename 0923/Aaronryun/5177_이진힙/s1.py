import sys
import heapq

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    heapq.heapify(data)
    answer = 0

    while N > 1:
        N //= 2

        answer += data[N - 1]

    print('#{} {}'.format(test, answer))

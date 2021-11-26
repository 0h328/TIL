# N과 M(11)
import sys
sys.stdin = open('input.txt')

def seq(idx, M):
    if idx == M:
        for i in range(M):
            print(res[i], end=' ')
        print()
        return

    for i in range(1, len(nums)):
        res[idx] = nums[i]
        check[i] = 1
        seq(idx+1, M)
        check[i] = 0

N, M = map(int, input().split())
nums = [0] + sorted(list(set(map(int, input().split()))))
check = [0] * (N+1)
res = [0] * M
seq(0, M)
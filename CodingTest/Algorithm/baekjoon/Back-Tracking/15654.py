# N과 M(5)
import sys
sys.stdin = open('input.txt')

def seq(idx, M):
    if idx == M:
        for i in range(M):
            print(res[i], end=' ')
        print()
        return

    for i in range(1, N+1):
        if check[i]: continue
        res[idx] = nums[i]
        check[i] = 1
        seq(idx+1, M)
        check[i] = 0

N, M = map(int, input().split())
nums = [0] + list(map(int, input().split()))
nums.sort()
check = [0] * (N+1)
res = [0] * M
seq(0, M)




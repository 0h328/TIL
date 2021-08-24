# 1. 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]
N = len(arr)
sel = [0] * N


def powerset(idx):
    if idx > 0:
        print([i for i in sel if i != 0])
        if idx == N:
            return

    for i in range(max(sel), N):
        sel[i] = arr[i]
        powerset(idx+1)
        sel[i] = 0


powerset(0)
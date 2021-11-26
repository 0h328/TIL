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


def powerset(idx):
    if idx == N:
        for i in range(len(sel)):
            if sel[i] == 1:
                print(arr[i], end=' ')
        print()

    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)


powerset(0)
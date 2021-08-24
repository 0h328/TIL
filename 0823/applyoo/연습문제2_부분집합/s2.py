# 2. 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
results = []


def powerset(idx):
    if idx > 0:
        if sum(sel) == 10:
            print([i for i in sel if i != 0])
        if idx == N:
            return

    for i in range(max(sel), N):
        sel[i] = arr[i]
        powerset(idx+1)
        sel[i] = 0


powerset(0)
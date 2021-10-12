#1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]
N = len(arr)
sel = [0] * N

def powerset(idx):
    if idx == N:
        print(sel)
    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx]
        powerset(idx+1)


powerset(0)
#1. 내가 작성
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]
N = len(arr)
sel = [0] * N

def powerset(idx):
    #Base Case
    if idx == N:
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)

powerset(0)
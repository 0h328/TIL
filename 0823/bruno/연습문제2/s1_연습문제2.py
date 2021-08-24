#1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]
N = len(arr)
sel = [0] * N   # 해당 요소를 선택 / 선택하지 않음을 표현하는 배열

def powerset(idx):
    if idx == N:
        print(sel)
    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)

powerset(0)
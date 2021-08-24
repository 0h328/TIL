# 1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]     # 전체 집합
N = len(arr)        # 집합의 원소 수
sel = [0] * N       # [0, 0, 0] 선택 여부를 확인할 배열


def powerset(idx):
    if idx == N:
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
    else:
        sel[idx] = 1
        powerset(idx + 1)
        sel[idx] = 0
        powerset(idx + 1)


powerset(0)
#2.
# 집합 {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}의 부분 집합의 요소 중 합이 10이 되는 부분집합을 구하시오.

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
results = []

def powerset(idx):
    # 선택 미완료
    if idx < N:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)
    # 선택 완료
    else:
        total = 0   # 부분집합의 합
        for i in range(N):
            if sel[i]:
                total += arr[i]

        if total == 10:
            for i in range(N):
                if sel[i]:
                    print(arr[i], end=' ')
            print()

powerset(0)
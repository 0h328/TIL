arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N

#합이 10이 되는 부분집한의 경우의 수를 구하는 문제

def powerset(idx):
    if idx < N:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)
    else:#부분집합 가능한 경우의 수를 말함
        total = 0
        for i in range(N):
            if sel[i]:
                total += arr[i]
                #나는 앞에서 곱했는데, 그렇게 안 하고 1이 있는 경우에 계산하면 됨
        if total == 10:
            for i in range(N):
                if sel[i]:
                    print(arr[i], end=' ')
            print()

powerset(0)
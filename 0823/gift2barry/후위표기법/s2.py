arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
N = len(arr)
sel = [0] * N
results = []

# 나를 불렀던 곳으로 돌아간다. 항상 명심
# 합 까지 고려하는 방법

def powerset(idx):
    # 선택 미완료
    if idx < N:
        sel[idx] = 1    #자리선택
        powerset(idx+1)
        sel[idx] = 0    #다음자리결정을 위한 원상복구
        powerset(idx+1)

    # 선택 완료
    else:
        total = 0       #부분집합의 합
        for i in range(N):
            if sel[i]:  # sel[i]가 1이면 ==> 선택했다면
                total += arr[i] #해당 부분집합의 합 누적
        if total == 10:
            for i in range(N):
                if sel[i]:
                    print(arr[i], end=' ')
            print()

powerset(0)


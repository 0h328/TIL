#1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3]   # 전체 집합(요소)
N = len(arr)      # 해당 집합의 요소 수
sel = [0] * N     # 해당 요소를 선택 / 선택하지 않음을 표현하는 배열열

def powerset(idx):
    if idx == N:
        # print(sel)
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
        print()
    else:
        sel[idx] = 1
        powerset(idx+1) # 재귀 호출 3까지 가면 마지막으로 부른곳은 여기므로 여기로 돌아감
        sel[idx] = 0    # 위에 라인으로 돌아갔으니 그다음 구조상 여기로 내려옴
        powerset(idx+1)

powerset(0)
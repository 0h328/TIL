#1.
# 집합 {1, 2, 3}의 모든 부분집합을 구하시오.

arr = [1, 2, 3] # 전체 집합(요소)
N = len(arr)    # 해당 집합의 요소 수
sel = [0] * N   # 자리로 대응 01 01 01 / arr과 대응 / 해당 요소를 선택 or 선택하지 않음을 표현하는 배열
# [0, 0, 0]

def powerset(idx):
    if idx == N:
        print(*sel)
        return
        # for i in range(N):
        #     if sel[i]:
        #         print(arr[i], end=' ')
        # print()
    else:
        sel[idx] = 1        # [1, 0, 0]
        powerset(idx+1)     # 다음 단계를 알고 싶어!
        sel[idx] = 0        # 선택 안한 경우
        powerset(idx+1)     # 역시 재귀!

powerset(0)

# 재귀... 디버깅... 돌아가는??? 함수의 호출 Stack
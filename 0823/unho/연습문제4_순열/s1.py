# 연습
def permutation(idx):
    #Base Case
    if idx == N:
        print(*selected)
        return

    for j in range(N):
        if check[j] == 0:
            check[j] = 1
            selected[idx] = arr[j]
            permutation(idx+1)
            check[j] = 0


arr = [1, 2, 3, 4, 5]
N = len(arr)
selected = [0] * N
check = [0] * N

permutation(0)

# arr = [1, 2, 3]
# N = len(arr)
# sel = [0] * N
# check = [0] * N
#
# def permutation(idx):
#     if idx == N:
#         print(sel)
#         return
#
#     for i in range(N):
#         if check[i] == 0:       # 해당 요소를 아직 사용하지 않았다면
#             sel[idx] = arr[i]   # 요소가 있는 자리에 arr의 i 번째 요소를 넣음
#             check[i] = 1        # 해당 원소를 사용했다고 체크
#             permutation(idx+1)  # 다음 자리를 확인
#             check[i] = 0        # 다음 반복문을 위해 원상 복구
#
# permutation(0)
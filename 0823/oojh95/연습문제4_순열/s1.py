arr = [1, 2, 3]
N = len(arr)
sel = [0] * N
check = [0] * N

def permutation(idx):
    if idx == N:
        print(sel)
        return

    for i in range(N):
        if check[i] == 0:       # 해당 원소를 아직 사용하지 않았다면
            sel[idx] = arr[i]   # 원소가 있는 자리에 arr의 i번째 요소를 넣자
            check[i] = 1        # 해당 원소를 사용했다고 체크해주자
            permutation(idx+1)  # 다음 자리를 확인하는 로직.
            check[i] = 0        # 다음 반복문을 위해 원상복구.

permutation(0)
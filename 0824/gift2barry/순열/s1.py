arr = [1, 2, 3]
N = len(arr)
sel = [0] * N
check = [0] * N

def permutation(idx):
    if idx == N:
        print(sel)
        return

for i in range(N):
    if check[i] == 0:           # 해당 원소를 아직 미사용이면,
        sel[i] = arr[i]       # 원소가 있는 자리에 arr 의 i번째 원소를 넣는다
        check[i] = 1            # 해당 원소 확인했다 체크한다
        permutation(i+1)      # 다음 원소를 확인하러 ㄱㄱ
        check[i] = 0            # 다음 반복문을 위해 확인체크를 초기화

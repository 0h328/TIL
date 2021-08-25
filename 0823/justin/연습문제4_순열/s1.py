# 순열 - 재귀

arr = [1, 2, 3]       # 활용 할 리스트
N = len(arr)          # 리스트 길이
sel = [0] * N         # 결과들이 저장 될 리스트
check = [0] * N       # 해당 원소를 이미 사용했는지/안했는지에 체크

def permutation(idx):  # idx는 sel의 자리를 결정하는 것 -> 3(N)이 된다는 것은? 모든 자리 결정이 끝났다는 의미
    if idx == N:       # 만약에 다 뽑아서 정리했다면 (순열이 완성됐다면)
        print(*sel)
        return
    for i in range(N):          # i -> 0, 1, 2
        if check[i] == 0:       # 해당 원소를 아직 사용하지 않았다면
            sel[idx] = arr[i]   # 원소 선택 자리(sel)에 arr의 i번째 값을 쓰고
            check[i] = 1        # 해당 원소를 사용했다고 체크
            permutation(idx+1)  # 다음 확인
            check[i] = 0        # 다음 반복문을 위한 원상 복구
permutation(0)
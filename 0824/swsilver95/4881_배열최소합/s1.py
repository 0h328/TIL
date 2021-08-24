import sys
sys.stdin = open('input.txt')

T = int(input())


def permutation(idx):
    global temp, min_num

    if min_num < temp:
        return

    if idx == N:
        if min_num > temp:
            min_num = temp
        return

    for i in range(N):
        if check[i] == 0:           # 해당 원소를 아직 사용하지 않았다면
            temp += arr[idx][i]     # 원소가 있는 자리에 arr의 i번째 요소를 넣는다.
            check[i] = 1            # 해당 원소를 사용했다는 뜻
            permutation(idx + 1)    # 다음 자리를 확인
            temp -= arr[idx][i]
            check[i] = 0            # 다음 반복문을 위해 check 초기화


for tc in range(1, T + 1):
    min_num = 501
    temp = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    check = [0] * N
    permutation(0)
    print('#{} {}'.format(tc, min_num))

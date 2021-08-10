import sys

sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    K, N, M = map(int, input().split())
    cnt = 0
    charge = [0] * (N + 1)

    Mlist = list(map(int, input().split()))

    for i in Mlist:
        charge[i] = 1                               # 충전소 초기화

    i = K
    # for i in range(start, len(charge), K):  # 갈수 있는 거리로 나누고
    while i < N:

        check = 0

        for j in range(K):
            if charge[i - j] == 1:                   # 뒤로가면서 충전소가 등장한다면 체크를 하나올리고 탈출
                check += 1
                i = i - j + K
                break
        if check == 1:
            cnt += 1
        elif check == 0:                             # 체크가 되지 않았다면 멈췄으므로 cnt를 0으로 만들고 탈출
            cnt = 0
            break

    print('#{} {}'.format(test + 1, cnt))

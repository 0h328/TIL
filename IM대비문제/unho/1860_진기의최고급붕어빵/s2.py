import sys
sys.stdin = open('input.txt')

tc = int(input())

# 2 2 2
# 1 3 3 3
# 3 3 3 3

for t in range(1, tc + 1):
    flag = 0
    N, M, K = map(int, input().split())
    custom = list(map(int, input().split()))
    custom.sort()

    if custom[0] < M:
        result = "Impossible"
    else:
        for j in range(1, N//K + 2):        # 붕어빵 만드는 싸이클
            cnt = 0                         #
            for i in range(N):              # 사람 명단 반복
                if custom[i] <= M * j:      # 사람이 오는 시간 < (몇초간 * 싸이클)
                    cnt += 1                # 사람 카운트 + 1
                    custom[i] = 11112       # 사람 팔았으므로 값 삭제

            if cnt > K * j:                 # 사람 수 > (붕어빵 갯수 * 현재 이전에 만들수 있는 붕어빵 싸이클)
                result = "Impossible"
                flag = 1
                break

        if flag == 0:                       # 그 외 가능
            result = "Possible"

    print("#{} {}".format(t, result))
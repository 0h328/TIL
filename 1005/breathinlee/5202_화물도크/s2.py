import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    running_info = []
    for _ in range(N):
        running_info.append(list(map(int, input().split())))
    running_info.sort(key=lambda x:x[1])
    cnt_list = []

    for i in range(N - 1):
        cnt = 1
        j = i + 1
        while j < N:
            if running_info[i][1] > running_info[j][0]:
                j += 1
            else:
                cnt += 1
                i = j
                j += 1

        cnt_list.append(cnt)

    print('#{} {}'.format(tc, max(cnt_list)))

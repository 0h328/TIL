import sys
sys.stdin = open('input.txt')

# 테스트 케이스 4개 통과(시작시간 기준으로 정렬 => 모든 경우 고려 불가)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    running_info = []
    for _ in range(N):
        running_info.append(list(map(int, input().split())))
    running_info.sort(key=lambda x:x[0])
    cnt_list = []

    for i in range(N - 1):
        cnt = 1
        j = i+1
        while j < N:
            if running_info[i][1] > running_info[j][0]:
                j += 1
            else:
                cnt += 1
                i = j
                j += 1

        cnt_list.append(cnt)

    print(max(cnt_list))

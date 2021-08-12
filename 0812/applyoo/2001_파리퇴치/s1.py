import sys
sys.stdin = open('input.txt')

def kill_fly(arr, size):
    max_kill = 0
    maxi = max(sum(arr, []))                                        # 최대값 구하기

    for row in range(len(arr) + 1 - size):                          # 가로 시작값
        for col in range(len(arr) + 1 - size):                      # 세로 시작값
            now_kill = 0                                            # 합계 초기화
            cnt = 0                                                 # 카운팅 초기화
            for row_size in range(size):                            # 가로 블럭 구현
                for col_size in range(size):                        # 세로 블럭 구현
                    now_kill += arr[row + row_size][col + col_size]
                    cnt += 1                                        # 카운트 +1
                if now_kill + (size**2-cnt) * maxi <= max_kill:     # 남은 칸을 최대값으로 다 더해도 현재 최대값보다 작은 경우
                    break
            else:                                                   # break 안 걸렸다면 실행됨
                max_kill = max(max_kill, now_kill)

    return max_kill

T = int(input())

for test in range(T):
    N, M = list(map(int, input().split()))
    fly_map = []
    for i in range(N):
        fly_map.append(list(map(int, input().split())))
    print('#{}'.format(test+1), kill_fly(fly_map, M))
import sys
sys.stdin = open('input.txt')

import copy

# feat. 우수법
# -90도 회전
'''
arr[i][j]               arr[j][N-1-i]
0,0 0,1 0,2             0,2 1,2 2,2
1,0 1,1 1,2      =>     0,1 1,1 2,1
2,0 2,1 2,2             0,0 1,0 2,0
'''
# 입력 받는 곳
for tc in range(1, 2):             # 테스트 케이스
    t = int(input())                # 해당 테스트 케이스 번호
    maze = []                       # 미로 리스트
    for _ in range(16):             # 미로가 16줄이므로 0 ~ 15까지 반복
        maze.append(list(input()))  # maze에 리스트들을 받아줌
    temp2 = copy.deepcopy(maze)
    """
# maze 상태 확인
    print("현재 maze 상태 입니다.")
    print("# 0 ", end = '  ')
    for j in range(1, len(maze) + 1):
        if j < 10:
            print(j, end = '    ')
        else:
            print(j, end = '   ')
    print()
    for i in range(len(maze)):
        if i < 9:
            print("# {} {}".format(i + 1, maze[i]))
        else:
            print("#{} {}".format(i + 1, maze[i]))
    print()
# maze 상태 확인
    """

    temp = copy.deepcopy(maze)  # temp에 현재 maze를 deepcopy한다.
    result = 0                  # 길 있는지 여부판단하는 변수
    r, c = 1, 1                 # 시작 지점이 1,1이므로 r, c를 1, 1로 초기화
    r2, c2 = 1, 1
    temp_rc = [(r, c)]          # 좌표인 r, c값을 저장할 리스트
    temp2_rc = [(r, c)]
    for rot in range(512):      # 미로의 전체 크기 * 2 = 16 * 16 * 2 (전체적으로 벽은 2번을 최대로 짚음)
        if rot != 0:            # 단순히 처음 위치를 표시하기 위해 사용함
            # print("(r, c) : ({}, {}) =>".format(r, c), end=" ")     # 바뀌기 전 r, c 값
            # 종료 조건                      # 좌측은 지나온 길이기에 고려를 안 함
            if maze[r][c + 1] == '3':       # 우측, c + 1 위치 값이 3인 경우
                c = c + 1                   # c = c + 1
                result = 1                  # result = 1
            elif maze[r - 1][c] == '3':     # 상측, r - 1 위치 값이 3인 경우
                r = r - 1                   # r = r - 1
                result = 1                  # result = 1
            elif maze[r + 1][c] == '3':     # 하측, r + 1 위치 값이 3인 경우
                r = r + 1                   # r = r + 1
                result = 1                  # result = 1

            else:                           # 종료되지 않을 경우
                for i in range(len(temp_rc)):   # temp_rc 범위만큼 반복
                    if (maze[r + 1][c] == '1') and (maze[r][c + 1] == '0' or maze[r][c + 1] == "2"): # 오른쪽에 벽이 있고
                        temp2_rc.append((r, c))
                        r2, c2 = r, c
                        pass                                                                        # 앞에 길이 있는 경우
                    elif (maze[r + 1][c] == '0') and (maze[r + 1][c - 1] == '1'): # 세,네갈래길, 오른쪽 뒤에 벽이 있는 경우
                        temp_rc[i] = (16 - 1 - temp_rc[i][1], temp_rc[i][0])      # temp_rc에 저장된 값들을 -90도 회전
                        temp2_rc.append((temp_rc[i][1], 15 - temp_rc[i][0]))
                        r2, c2 = temp2_rc[i][0], temp2_rc[i][1]
                    else:                            # 그 외의 모든 경우
                        temp_rc[i] = (temp_rc[i][1], 16 - 1 - temp_rc[i][0])    # 그런 뒤 90도 회전시킴
                        temp2_rc.append((15 - temp_rc[i][1],temp_rc[i][0]))
                        r2, c2 = temp2_rc[i][0], temp2_rc[i][1]
                if (maze[r + 1][c] == '1') and (maze[r][c + 1] == '0' or maze[r][c + 1] == "2"):   # 오른쪽에 벽이 있고
                    c = c + 1   # 앞으로 한 칸 이동, 여기서 앞은 우측 이동이다.                       # 앞에 길이 있는 경우
                elif (maze[r + 1][c] == '0') and (maze[r + 1][c - 1] == '1'):   # 세,네갈래길인데 오른쪽 뒤에 벽이 있는 경우
                    r = r + 1   # 아래로 한 칸 이동                              # if에 의해 앞 : 벽, 좌 : 길, elif 우 : 길
                    r, c = 16 - 1 - c, r                      # 미로를 -90도 회전
                    for a in range(16):                       # 행 탐색
                        for b in range(16):                   # 열 탐색
                            maze[a][b] = temp[b][16 - 1 - a]  # 미로를 -90도 회전시킨 모양으로 다시 바꿈
                    # print("-90도로 회전 시킴")
                else:                               # 그 외의 모든 경우
                    if maze[r - 1][c] == '0':       # 위 쪽에 길이 있으면
                        r = r - 1                   # 위로 한 칸 이동, 미리 이동을 시켜놔야 회전 시 길을 안 잃음
                    r, c = c, 16 - 1 - r            # r, c 값 역시 90도 회전시킨 값으로 이동 시킴, (위 쪽 0이 아니더라도 함)

                    for a in range(16):             # 미로 전체 탐색
                        for b in range(16):
                            maze[a][b] = temp[16 - 1 - b][a]    # 미로를 90도 회전시킨 모양으로 다시 바꿈
                    # print("90도로 회전 시킴")
                temp = copy.deepcopy(maze)  # maze가 모양이 다시 바뀌었기 때문에 temp에 deep copy 시킴

            # print("({}, {})".format(r, c))    # 바뀐 r, c 값
        temp_rc.append((r, c))
        # print(temp_rc)
        for a in range(16):             # 미로 출력
            for b in range(16):
                # if a == r and b == c:
                if (a, b) == (r2, c2):
                    print('\033[30m' '\033[47m' + str(temp2[a][b]) + '\033[00m', end=' ')
                elif (a, b) in temp2_rc:
                    print('\033[31m' '\033[43m' + str(temp2[a][b]) + '\033[00m', end=' ')
                else:
                    print(temp2[a][b], end=' ')
            print()
        print()

        if maze[r][c] == '3':       # 현재 미로의 (r, c) 좌표의 값이 3일 경우 즉시 종료
            break

    print(" #{} {}".format(tc, result))  # 테스트 케이스 번호와 길이 존재하는지 결과 출력

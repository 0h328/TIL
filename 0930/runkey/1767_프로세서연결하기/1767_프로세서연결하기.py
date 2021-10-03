"""
가장 자리 코어는 제외
한 줄씩 비교하면서 코어의 네 방향의 길이를 따짐
N * N 크기의 빈 리스트 생성
해당 리스트에 i, j 리스트에 갯수를 적어줌
1 이상의 값 중 갈 수 있는 갯수가 적은 곳부터 탐지 시작
갈 수 있는 곳이 적은 곳부터 시작
네 방향 탐색 중 가장 짧은 길이의 지나가는 길에 2를 표시
"""

def direc(r, c, move, l):   # 행, 열, 이동횟수(전선길이), l값 # 갈 수 있는 갯수를 탐지하는 함수
    flag = 0    # 중간에 0(길) 이외의 값이 있는지 확인
    if n_list[r][c] != 0:   # 0이 아닌 값이 나오면
        flag = 1    # flag = 1
    if flag == 1:   # flag 가 1이면
        return      # 함수 탈출

    if n_list[r][c] == 0:   # 프로세서의 초기 상태에서 길이 있을 때
        if r == 0:          # 0행이면,             # 해당 좌표에서 상으로 탐색함
            direc_list[r + move][c].append(1)       # 1을 추가
            direc_list[r + move][c].append(move)    # 가장자리까지 길이 있는 것이므로 전선 길이 추가
        elif r == N - 1:    # N - 1행이면           # 해당 좌표에서 하로 탐색함
            direc_list[r - move][c].append(2)       # 2를 추가
            direc_list[r - move][c].append(move)    # 전선 길이 추가
        elif c == 0:        # 열이 0이면            # 해당 좌표에서 좌로 탐색함
            direc_list[r][c + move].append(3)       # 3을 추가
            direc_list[r][c + move].append(move)    # 전선 길이 추가
        elif c == N - 1:    # 열이 N-1열이면         # 해당 좌표에서 우로 탐색함
            direc_list[r][c - move].append(4)       # 4를 추가
            direc_list[r][c - move].append(move)    # 전선 길이 추가
            # 해당 좌표에서 move만큼 움직여서 가장자리로 왔으므로 direc_list에서 move만큼 움직임

    if 0 < r < N - 1 and 0 < c < N - 1:     # r과 c가 0과 N - 1사이에 있다면
        if l == 0:                          # 상으로 탐색 시
            direc(r - 1, c, move + 1, l)    # r을 1 빼줌
        elif l == 1:                        # 하로 탐색 시
            direc(r + 1, c, move + 1, l)    # r을 1 더해줌
        elif l == 2:                        # 좌로 탐색 시
            direc(r, c - 1, move + 1, l)    # c를 1 빼줌
        elif l == 3:                        # 우로 탐색 시
            direc(r, c + 1, move + 1, l)    # c를 1 더해줌


def core():   #전선 표시해주는 곳
    for new in new_list:    # new_list에서 하나씩 꺼냄
        i = new[0]  # 행
        j = new[1]  # 열
        c = new[2]  # 코어에서 움직일 수 있는 방향 갯수를 따지기 위함

        temp_dict = {}  # 빈 딕셔너리 생성
        for x in range(1, c, 2): # x는 방향 인덱스만 따짐, dict 만들어서 최소 길이 순 정렬 위함
            direction = direc_list[i][j][x] # 방향 = direc_list의 (i, j)인덱스의 x번째 인덱스
            move = direc_list[i][j][x + 1]  # 해당 방향의 전선길이는 x + 1 인덱스
            temp_dict[direction] = move     # temp_dict에 방향을 키 값으로 전선 길이를 값으로 넣음
        temp_dict = sorted(temp_dict.items(), key = lambda x:x[1])  # 전선 길이 순으로 정렬
        # temp_dict는 이제 리스트 안에 방향, 전선 길이 세트가 담김
####################################
        print("temp_dict에 담겨있는 값")
        print(temp_dict)
####################################

        for ct in range((c - 1)//2):    # 방향 갯수 # c에서 0번째 인덱스 빼주고 2로 나눔
            flag = 0                    # 길을 찾는 도중 0 이외의 값이 있나 확인 용도
            current = temp_dict[ct][0]  # 방향
            zero_cnt = temp_dict[ct][1] # 전선 길이

            if current == 1:            # 방향이 1, 상이면
                for n in range(0, i):   # i는 현재 행의 값, 위로 움직이므로 0부터 i까지
                    if n_list[n][j] != 0:   # 길 검색 도중 0이 아닌 값이 나오면
                        flag = 1        # flag = 1
                        break           # 빠져나감
                if flag == 0:           # flag가 0이면 (가장자리까지 길이 존재하면)
                    for n in range(0, i):   # 0부터 i까지 탐색 (열은 고정 행만 움직이므로)
                        n_list[n][j] = 2    # n_list의 해당 인덱스 값을 2로 채워줌
                    break   # 더 이상 해당 코어에서는 다른 방향을 탐지할 필요 없으므로 break

            elif current == 2:            # 방향이 2, 하이면
                for n in range(i + 1, N): # i는 현재 행의 값, 아래로 움직이므로 i + 1부터 N까지
                    if n_list[n][j] != 0: # 길 검색 도중 0이 아닌 값이 나오면
                        flag = 1          # flag = 1
                        break             # 빠져나감
                if flag == 0:             # flag가 0이면 (가장자리까지 길이 존재하면)
                    for n in range(i + 1, N):   # i + 1부터 N까지 탐색 (열은 고정 행만 움직이므로)
                        n_list[n][j] = 2        # n_list의 해당 인덱스 값을 2로 채워줌
                    break   # 더 이상 해당 코어에서는 다른 방향을 탐지할 필요 없으므로 break

            elif current == 3:            # 방향이 3, 좌이면
                if n_list[i][0:j] == [0] * zero_cnt:    # i행의 0부터 j열까지 슬라이스한 값이 전선 길이만큼 0으로 채워져 있으면
                    n_list[i][0:j] = [2] * zero_cnt     # 2로 다 바꿔줌
                    break   # 더 이상 해당 코어에서는 다른 방향을 탐지할 필요 없으므로 break

            elif current == 4:            # 방향이 4, 우이면
                if n_list[i][j + 1:N] == [0] * zero_cnt:    # i행의 j + 1부터 N열까지 슬라이스한 값이 전선 길이만큼 0으로 채워져 있으면
                    n_list[i][j + 1:N] = [2] * zero_cnt     # 2로 다 바꿔줌
                    break   # 더 이상 해당 코어에서는 다른 방향을 탐지할 필요 없으므로 break


############################ 시작 위치  ###############################
tc = int(input())           # 테스트 케이스 갯수

for t in range(1, tc + 1):  # 테스트 케이스 갯수 만큼 반복
    result = 0              # 최종 결과값
    N = int(input())        # 입력 값
    n_list = [list(map(int, input().split())) for _ in range(N)]    # 초기 프로세서 상태

####################################
    print("n_list에 담겨 있는 값")
    for z in range(N):
        print(n_list[z])
####################################

    dr = [-1, 1, 0, 0]  # 상하
    dc = [0, 0, -1, 1]  # 좌우

    # direc_list 초기화, 길 = [0] , 코어 있는 위치 = [0, 방향, 전선 길이, 방향, 전선 길이...]
    # 한 줄로 direc_list를 정의하면 얕은 복사로 같은 인덱스에 모든 값들이 동일 값으로 변환됨
    direc_list = [0] * N                # N개 만큼 공간 확보, [] * N 으로 해도 [] 하나만 나옴
    for m in range(N):                  # N줄
        direc_list[m] = []              # m번째 인덱스를 빈 리스트로 변경
        for _ in range(N):
            direc_list[m].append([0])   # m번째 인덱스의 빈 리스트에 [0]을 N개 추가

    new_list = []   # 코어가 있는 좌표값과 direc_list의 해당 좌표에서 마지막 인덱스 길이를 담음
                    # 마지막 인덱스 길이가 짧다 = 갈 수 있는 방향이 적다.
    for i in range(1, N - 1):       # 가장 자리는 굳이 검사할 필요 없으므로
        for j in range(1, N - 1):   # 1부터 N - 1까지 반복
            if n_list[i][j] == 1:   # 초기 n_list에서 1인 부분만 탐색
                for l in range(4):  # 1인 부분에서 네 방향을 전부 탐색해야 하므로
                    nr = i + dr[l]  # 상하
                    nc = j + dc[l]  # 좌우

                    direc(nr, nc, 1, l) # nr, nc, 1, l값을 전달인자로 direc 함수에 넘겨줌

                if len(direc_list[i][j]) > 1:   # direc_list의 길이가 1 초과 = 코어있는 위치
                    # indentation -> 코어에서 네 방향을 다 돈 뒤에 해야 네 방향의 정보가 담김
                    new_list.append([i, j, len(direc_list[i][j])])
                    # new_list에 i, j, direc_list[i][j]의 길이를 추가함
                    new_list = sorted(new_list, key = lambda x : x[2])
                    # 갈 수 있는 방향이 적은 순으로 탐색해야 하므로 길이 기준 정렬

    # new_list
    # i, j와 (i, j)에서 (가장 자리까지의 길이 존재하는 것의 갯수 *2) + 1 값을 담음
    # 마지막 부분은 direc_list[i][j]의 전체 길이로
    # 해당 인덱스에서의 0과 방향, 해당 방향의 전선 길이의 총 갯수다.

    core()  # core 함수 실행
####################################
    print()
    print("모든 실행이 끝난 후 n_list에 담겨있는 값")
    for z in range(N):
        print(n_list[z])
####################################
    print()
    print("direc_list에 담겨있는 값")
    for z in range(N):
        print(direc_list[z])
####################################
    print()
    print("new_list에 담겨있는 값")
    print(new_list)
####################################

    # 전체 탐색 후 2의 갯수를 세줌. (2는 전선이 깔린 곳)
    for i in range(N):
        for j in range(N):
            if n_list[i][j] == 2:
                result += 1


    print("#{} {}".format(t, result))
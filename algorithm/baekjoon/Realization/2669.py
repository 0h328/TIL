# from pandas import DataFrame

xy = [[0 for _ in range(100)] for _ in range(100)] # 좌표 범위가 1~100이므로 xy라는 2차원 배열 list 생성

for _ in range(4):                                 # 입력 예시 4줄 반복
    x1, y1, x2, y2 = map(int, input().split())     # 입력받기

    for x in range(x1, x2):                        # 범위를 x1, x2로 한 이유는 해당 범위는 선형으로 이루어져 있으므로 좌표 list에 1을 더하기 위함.
        for y in range(y1, y2):                    # 위와 동일
            xy[x][y] += 1                          # 입력받은 좌표 범위(xy)에 1을 더해준다.

cnt = 0                                            # 업데이트 된 좌표 합을 구하기 위해 초기화 변수 생성

for i in range(100):                               # 좌표 범위가 1~100 이므로
    for j in range(100):                           # 좌표 범위가 1~100 이므로
        if xy[i][j] > 0:                           # xy 2차원 list가 0보다 큰 경우는 면적을 가지고 있다는 것과 같으므로
            cnt += 1                               # 앞서 설정한 변수에 1씩 더해준다.

print(cnt)                                         
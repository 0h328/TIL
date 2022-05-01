import sys
sys.stdin = open('input.txt')

H, W = map(int, input().split())
sky = [input() for _ in range(H)]
predict = [[0] * W for _ in range(H)]   # 출력 값(예측 정보)을 저장할 리스트

for i in range(H):
    time = 0        # 몇분 뒤 올지 시간 체크
    cloud = False   # 해당 행에 구름이 있는지 없는지 기본 값으로 False 지정
    for j in range(W):
        if sky[i][j] == 'c':    # 구름이 있으면
            cloud = True        # True
            predict[i][j] = 0   # 해당 지역에 구름이 있으므로 시간은 0
            time = 1            # 1분뒤 옆으로 이동하므로 시간은 1
        elif sky[i][j] == '.' and not cloud:    # 해당 행에 구름이 없고, 현 위치도 구름이 없는 경우
            predict[i][j] = -1                  # 구름이 오지 않으므로 -1
        elif sky[i][j] == '.' and cloud:        # 해당 행에 구름이 있고, 현 위치에 구름이 없는 경우
            predict[i][j] = time                # 이전에 구름이 있었을 때, n분 뒤에 올 시간을 정했으므로 리스트 갱신
            time += 1                           # 옆으로 이동하므로 시간 +1

for i in predict:
    print(*i, end=' ')
    print()

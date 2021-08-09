import sys
sys.stdin = open('input.txt')


for i in range(10):
    len_total = int(input())
    building_h = list(map(int, input().split()))
    total_river_view = river_view = 0

    # 첫 빌딩부터 마지막 빌딩까지 반복
    for j in range(2, len_total-2):
        max_side = 0

        # 빌딩이 왼쪽 2개, 오른쪽 2개의 빌딩보다 높을 때
        if building_h[j] > building_h[j-1] and building_h[j] > building_h[j-2] and building_h[j] > building_h[j+1] and building_h[j] > building_h[j+2]:
            # 주변 빌딩 높이 중 최대값 구하기
            for k in (j-2, j-1, j+1, j+2):
                if building_h[k] > max_side:
                    max_side = building_h[k]
            # 해당 빌딩 중 조망권 확보한 세대
            river_view = building_h[j] - max_side
            # 전체 빌딩의 조망권 확보 세대
            total_river_view += river_view

    print('#{0} {1}'.format(i+1, total_river_view))

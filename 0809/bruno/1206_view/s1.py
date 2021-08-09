import sys
sys.stdin = open('input.txt')

total_river_view = river_view = 0
max_side = 0
for i in range(10):
    building_h = list(map(int, input().split()))
    for j in range(2, len(building_h)-2):
        if building_h[j] > building_h[j-1] and building_h[j] > building_h[j-2] and building_h[j] > building_h[j+1] and building_h[j] > building_h[j+2]:
            for k in (j-2, j-1, j+1, j+2):
                if building_h[k] > max_side:
                    max_side = building_h[k]
            river_view = building_h[j] - max_side
            total_river_view += river_view

    print('#{0} {1}'.format(i+1, total_river_view))
import sys
sys.stdin = open('input.txt')
for i in range(10) :
    numbers = int(input())
    building_floor = list(map(int, input().split()))
    floor = 0
    for j in range(2,numbers-2) :
        cnt_floor_1 = building_floor[j] - building_floor[j-2]
        cnt_floor_2 = building_floor[j] - building_floor[j-1]
        cnt_floor_3 = building_floor[j] - building_floor[j+1]
        cnt_floor_4 = building_floor[j] - building_floor[j+2]
        if cnt_floor_1 > 0 and cnt_floor_2 > 0 and cnt_floor_3 > 0 and cnt_floor_4 > 0 :
            floor += min(cnt_floor_1,cnt_floor_2,cnt_floor_3,cnt_floor_4)
    print('#{0} {1}'.format(i+1, floor))
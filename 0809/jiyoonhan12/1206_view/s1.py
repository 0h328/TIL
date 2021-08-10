import sys
sys.stdin = open('input.txt')

for t in range(1, 11): # 10개의 케이스
    case = int(input()) # 건물 수
    buildings = list(map(int, input().split()))
    view = 0

    for b in range(2, case-2): # 양쪽 끝 2개씩 제거
        side = [buildings[b-2], buildings[b-1], buildings[b+1], buildings[b+2]] # 체크할 양 옆 건물 4개
        highest = max(side) # 4개 중 가장 큰 것 보다 크면 조망권 확보
        if buildings[b] > highest:
            view += (buildings[b] - highest)

    print('#{} {}'.format(t, view))
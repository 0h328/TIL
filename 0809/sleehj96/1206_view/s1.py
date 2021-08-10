import sys

sys.stdin = open('input.txt')

i = 1
while i <= 10:
    n = int(input())

    buildings = list(map(int, input().split()))

    ans = 0

    # 리스트의 3번째 부터 끝에서 3번째 까지 반복
    for idx in range(2, len(buildings)-2):

        # max 내장함수를 쓰면 더 편리한 구현 가능
        near_building_max = buildings[idx-2]

        for n in range(-1, 3):      # 원래는 range(-2, 3)을 해야함 but 초기화한 인덱스가 -2
            if not n:               # n == 0이면, 즉, 빌딩 자기 자신이면
                continue            # continue

            # 나를 제외한 주변에서 가장 큰 빌딩을 찾기 위함
            if near_building_max < buildings[idx+n]:
                near_building_max = buildings[idx+n]

            # 주변에 나보다 더 큰 빌딩이 있으면
            if buildings[idx] <= near_building_max:
                break

        # for문을 다 돌았으면 == 주변 5개 중 내가 가장 높은 빌딩이면
        else:
            ans += buildings[idx] - near_building_max

    print('#{0} {1}'.format(i, ans))
    i += 1
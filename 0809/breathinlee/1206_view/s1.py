for k in range(1, 11):   # 총 10개의 tc
    N = int(input())
    numbers = list(map(int, input(). split()))
    cnt = 0  # 조망권이 확보되는 세대의 수를 0으로 초기화
    for i in range(2, N - 2):   # i번째 빌딩에 대하여 양쪽 모두 거리가 2 이상의 공간이 확보될 떄, 조망권이 확보되므로 i-2, i-1, i+1, i+2 이렇게 4개와 비교해야 함.
        if numbers[i] > numbers[i - 2] and numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1] and numbers[i] > numbers[i + 2]:
            # 주변 네개의 빌딩과 비교했을 때, 모두 i 번째가 더 클 경우에만 조망권이 확보되는 세대 수가 생길 수 있음
            data = [numbers[i - 2], numbers[i - 1], numbers[i + 1], numbers[i + 2]]
            max_data = data[0]
            for j in range(4):   # 주변 i-2, i-1, i+1, i+2 번째 빌딩의 높이 중 가장 높은 것을 고르기 위함
                if data[j] > max_data:
                    max_data = data[j]
                    j += 1
            # max_data = max(numbers[i-2], numbers[i-1], numbers[i+1], numbers[i+2])
            cnt += numbers[i] - max_data   # 조망권이 확보되는 세대의 수는 i번째 빌딩에서 i-2, i-1, i+1, i+2 번째 빌딩 중 가장 높은 것과의 차이이므로 cnt에 더함
            i += 1
        else:
            continue
    print("#{} {}".format(k, cnt))
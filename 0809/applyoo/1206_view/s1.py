def view(arr, length):
    result = 0  # 결과 값

    for i in range(2, length - 2):  # 양 사이드는 '0, 0'으로 주어졌으므로 계산할 필요 없음
        cut = max(arr[i - 2], arr[i - 1], arr[i + 1], arr[i + 2])  # 좌우 2칸에서 최대값 뽑아냄
        if arr[i] <= cut:  # 만약 해당 건물이 좌우 2칸보다 작거나 같은 경우
            continue  # 계산할 필요 없음
        else:  # 좌우 2칸보다 큰 경우
            result += arr[i] - cut  # cut에서 뺀만큼 result에 더해줌

    return result


for i in range(10):
    length = int(input())
    arr = list(map(int, list(input().split())))
    print('#{} {}'.format(i + 1, view(arr, length)))
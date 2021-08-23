import sys

sys.stdin = open('input.txt')

i = 1
while i <= 10:
    dump = int(input())
    box_list = list(map(int, input().split()))
    ans = 0

    while dump > 0:         # 덤프 횟수 동안
        box_max = max(box_list) # 최대 상자개수
        box_min = min(box_list) # 최소 상자개수

        if box_max - box_min <= 1:  # 차이가 1이하 이면
            ans = box_max - box_min # 그 값을 반환
            break
        else:       # 차이가 1보다 크면
            box_list[box_list.index(box_max)] -= 1  # 가장 큰 상자에서 하나 빼고
            box_list[box_list.index(box_min)] += 1  # 가장 작은 상자에서 하나 추가
            ans = max(box_list) - min(box_list)     # 최대 상자 개수와 최소 상자 개수의 차이를 새로 계산

        dump -= 1

    print('#{0} {1}'.format(i, ans))
    i += 1

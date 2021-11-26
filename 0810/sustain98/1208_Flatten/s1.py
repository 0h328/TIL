import sys
sys.stdin = open('input.txt')

for idx in range(1,11):
    cnt = int(input())
    heights = sorted(list(map(int, input().split())))              # 우선적으로 sort를 한번해서 제일 낮은곳과 제일 높은곳을 찾기 쉽도록 한다.

    while cnt and heights[-1]-heights[0] > 1:                      # 덤프 횟수가 남았고, 평탄화가 아직 되지 않은 경우 while문을 계속 돈다.
        heights[-1] -= 1                                           # 가장 높은 곳에서 하나를 뺀다.
        for i in range(98, 0, -1):                                 # heights[-1]의 변경된 값이 앞의 다른값들보다 작아졌을수 있으므로 정렬해줌
            if heights[i] > heights[i+1]:
                heights[i], heights[i+1] = heights[i+1], heights[i]
            else:
                break
        heights[0] += 1                                             # 가장 낮은곳에 하나 더해준다.
        for i in range(100):                                        # heights[0]의 변경된 값이 뒤의 다른 값보다 클수 있으므로 정렬해줌
            if heights[i] > heights[i + 1]:
                heights[i], heights[i + 1] = heights[i + 1], heights[i]
            else:
                break
        cnt -= 1                                                    # 덤프횟수를 하나 빼준다.
    print('#{} {}'.format(idx, heights[-1] - heights[0]))




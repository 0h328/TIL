import sys
sys.stdin = open('input.txt')

for cnt in range(10):                                            # 10개의 test case가 있기 때문에 10번 반복
    num = int(input())                                           # 덤프의 횟수를 num에 저장
    box_height = list(map(int, input().split()))                 # box의 높이를 list에 넣어줌
    for _ in range(num):                                         # num(덤프)의 횟수 만큼 반복
        box_height[box_height.index(max(box_height))] -= 1       # 가장 높은 박스 높이에서 1을 빼고
        box_height[box_height.index(min(box_height))] += 1       # 가장 낮은 박스 높이에 1을 더해주기

    print('#{0} {1}'.format(cnt+1,max(box_height)-min(box_height))) # 덤프 횟수만큼 반복된 결과의 list에서 최대값 - 최소값을 출력

import sys
sys.stdin = open("input.txt")

for i in range(1, 11):                              # 10개의 테스트 케이스
    dumb = int(input())                             # dumb 갯수
    boxes = list(map(int, input().split()))         # 상자 높이 lsit

    for _ in range(dumb):                           # 덤프 갯수만큼 반복
        boxes[boxes.index(max(boxes))] -= 1         # 가장 높은 상자 중 가까운 것 - 1
        boxes[boxes.index(min(boxes))] += 1         # 가장 낮은 상자 중 가까운 것 + 1
        if max(boxes) - min(boxes) <= 1:            # 가장 높은 것과 낮은 것의 차가 1 이하면
            break                                   # 반복 종료
    result = max(boxes) - min(boxes)                # 가장 높은 것과 낮은 것의 차를 result에 저장
    print("#{0} {1}".format(i, result))
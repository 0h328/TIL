import sys
sys.stdin = open('input.txt')

T = 10
for test_case in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))

    result = 0

    for _ in range(N):
        boxes[boxes.index(max(boxes))] -= 1
        boxes[boxes.index(min(boxes))] += 1

    result = max(boxes)-min(boxes)

    print('#{} {}'.format(test_case, result))

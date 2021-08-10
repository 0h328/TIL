import sys

sys.stdin = open('input.txt')

n = int(input())

i = 1
while i <= n:

    box_spots = int(input())

    box_up = list(map(int, input().split()))

    for idx, box in enumerate(box_up):
        cnt = 0
        for idx2 in range(idx + 1, box_spots):
            if box <= box_up[idx2]:
                cnt += 1

        box_up[idx] = box_spots - (idx + cnt + 1)

    print('#{0} {1}'.format(i, max(box_up)))

    i += 1
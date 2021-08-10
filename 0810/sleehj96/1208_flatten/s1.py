import sys

sys.stdin = open('input.txt')

i = 1
while i <= 10:
    dump = int(input())
    box_list = list(map(int, input().split()))
    ans = 0

    while dump > 0:
        box_max = max(box_list)
        box_min = min(box_list)

        if box_max - box_min <= 1:
            ans = box_max - box_min
            break
        else:
            box_list[box_list.index(box_max)] -= 1
            box_list[box_list.index(box_min)] += 1
            ans = max(box_list) - min(box_list)

        dump -= 1

    print('#{0} {1}'.format(i, ans))
    i += 1

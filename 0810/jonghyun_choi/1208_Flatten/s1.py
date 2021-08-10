import sys
sys.stdin = open('input.txt')

for case in range(10):
    dump = int(input())
    box_height = list(map(int,input().split()))
    sorted_box = sorted(box_height)
    for _ in range(dump):
        sorted_box[-1] -= 1
        sorted_box[0] += 1
        sorted_box = sorted(sorted_box)
    gap = sorted_box[-1] - sorted_box[0]
    print('#{} {}'.format(case+1, gap))


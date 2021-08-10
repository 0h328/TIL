

import sys
sys.stdin = open('input.txt')

A = int(input())

for number in range(1, A+1):
    num = int(input())
    heights = list(map(int, input().split()))

    drop_list=[]
    for i in range(0, len(heights)):
        cnt = 0
        for j in range(i, len(heights)):
            if heights[i] > heights[j]:
                cnt += 1
        drop_list.append(cnt)

    result = max(drop_list)
    print("#{} {}".format(number, result))

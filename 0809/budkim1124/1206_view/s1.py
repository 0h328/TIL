# 코드가 들어가는 파일

import sys
sys.stdin = open('input.txt')

A = 10

for number in range(1, A+1):
    num = int(input())
    b_height = list(map(int, input().split()))

    cnt = 0

    for idx in range(2, num-2):
        if b_height[idx] > b_height[idx-1] and b_height[idx] > b_height[idx-2] and b_height[idx] > b_height[idx+1] and b_height[idx] > b_height[idx+2]:

            if b_height[idx-1] > b_height[idx-2]:
                a = b_height[idx-1]
            else:
                a = b_height[idx-2]


            if b_height[idx+1] > b_height[idx+2]:
                b = b_height[idx+1]
            else:
                b = b_height[idx+2]


            if a > b:
                cnt += b_height[idx] - a
            else:
                cnt += b_height[idx] - b

    print("#{} {}".format(number, cnt))
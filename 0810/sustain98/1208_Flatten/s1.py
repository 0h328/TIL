import sys
sys.stdin = open('input.txt')

for idx in range(1,11):
    cnt = int(input())
    heights = sorted(list(map(int, input().split())))

    while cnt and heights[-1]-heights[0] > 1:
        heights[-1] -= 1
        for i in range(98, 0, -1):
            if heights[i] > heights[i+1]:
                heights[i], heights[i+1] = heights[i+1], heights[i]
            else:
                break
        heights[0] += 1
        for i in range(100):
            if heights[i] > heights[i + 1]:
                heights[i], heights[i + 1] = heights[i + 1], heights[i]
            else:
                break
        cnt -= 1
    print('#{} {}'.format(idx, heights[-1] - heights[0]))




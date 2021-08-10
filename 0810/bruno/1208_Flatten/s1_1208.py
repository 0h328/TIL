import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    cnt = int(input())
    height = list(map(int, input().split()))
    while cnt:
        max_height = min_height = height[0]
        max_idx = min_idx = 0
        for j in range(100):
            if height[j] > max_height:
                max_height = height[j]
                max_idx = j
            if height[j] < min_height:
                min_height = height[j]
                min_idx = j

        height[max_idx] -= 1
        height[min_idx] += 1
        cnt -= 1
    height_gap = height[max_idx] - height[min_idx]
    print('#{} {}'.format(tc, height_gap))

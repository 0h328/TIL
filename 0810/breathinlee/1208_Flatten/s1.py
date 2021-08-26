import sys
sys.stdin = open("input.txt")

def max_height():
    max_value = 0
    for i in range(100):
        if box_height[i] > max_value:
            max_value = box_height[i]
            max_idx = i
    return max_idx

def min_height():
    min_value = 101
    for i in range(100):
        if box_height[i] < min_value:
            min_value = box_height[i]
            min_idx = i
    return min_idx


for tc in range(1, 11):
    num = int(input())
    box_height = list(map(int, input().split()))
    for i in range(num):
        box_height[max_height()] -= 1
        box_height[min_height()] += 1
    height_difference = box_height[max_height()] - box_height[min_height()]
    print('#{} {}'.format(tc, height_difference))
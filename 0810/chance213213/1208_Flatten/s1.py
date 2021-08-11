import sys
sys.stdin = open('input.txt')

def max_index():
    my_max = 0
    max_idx = 0
    for idx in range(len(numbers)):
        if numbers[idx]> my_max:
            my_max = numbers[idx]
            max_idx = idx
    return max_idx

def min_index():
    my_min = 100
    min_idx = 0
    for idx in range(len(numbers)):
        if numbers[idx] < my_min:
            my_min = numbers[idx]
            min_idx = idx
    return min_idx


for T in range(1, 11):
    N = int(input())
    numbers = list(map(int, input().split()))
    for _ in range(N):
        numbers[max_index()] -= 1
        numbers[min_index()] += 1
    ans = numbers[max_index()] - numbers[min_index()]
    print('#{} {}'.format(T, ans))
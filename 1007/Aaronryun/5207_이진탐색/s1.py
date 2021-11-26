import sys

sys.stdin = open('input.txt')


def search(nums, target, start, end):
    global answer
    tmp = 0
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            answer += 1
            return
        elif nums[mid] < target:
            if tmp == 2:
                return
            else:
                start = mid + 1
                tmp = 2
        else:
            if tmp == 1:
                return
            else:
                end = mid - 1
                tmp = 1
    return


for test in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    data1 = [*map(int, input().split())]
    data2 = [*map(int, input().split())]
    data1.sort()
    answer = 0
    for i in data2:
        start = 0
        end = N - 1
        temp = search(data1, i, start, end)

    print('#{} {}'.format(test, answer))

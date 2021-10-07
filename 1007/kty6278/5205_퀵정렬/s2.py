import sys
sys.stdin = open('input.txt')


def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[len(num) // 2]
    lesser_num, equal_num, greater_num = [], [], []
    for my in num:
        if my < pivot:
            lesser_num.append(my)
        elif my > pivot:
            greater_num.append(my)
        else:
            equal_num.append(my)
    return quick_sort(lesser_num) + equal_num + quick_sort(greater_num)

for tc in range(int(input())):
    n = int(input())
    num = list(map(int, input().split()))

    result = quick_sort(num)
    print('#{} {}'.format(tc+1, result[n//2]))

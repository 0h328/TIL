import sys
sys.stdin = open('input.txt')


def merge(l: list, r: list):
    global ans

    if l[-1] > r[-1]:
        ans += 1

    i = j = 0
    result = []
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1

    while i < len(l):
        result.append(l[i])
        i += 1

    while j < len(r):
        result.append(r[j])
        j += 1

    return result


def partition(lst: list):      # 리스트 전체 전달
    if len(lst) < 2:
        return lst

    mid = len(lst)//2
    left = partition(lst[:mid])
    right = partition(lst[mid:])
    return merge(left, right)


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    ans = 0

    print('#{0} {1} {2}'.format(t, partition(nums)[N//2], ans))
    # break

import sys
sys.stdin = open('input.txt')

T = int(input())

def merge_sort(start, end):
    if start + 1 == end:
        return [data[start]]
    mid = start + (end - start) // 2

    left = merge_sort(start, mid)
    right = merge_sort(mid, end)

    if left[-1] > right[-1]:
        ans[1] += 1

    return merge(left, right)

def merge(left, right):
    l_idx, r_idx = 0, 0
    result = []

    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] < right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1

    while l_idx < len(left):
        result.append(left[l_idx])
        l_idx += 1

    while r_idx < len(right):
        result.append(right[r_idx])
        r_idx += 1

    return result

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    ans = [0, 0]    # N//2 원소, 오른쪽 원소 먼저 복사

    ans[0] = merge_sort(0, N)[N//2]
    print('#{}'.format(tc), end=' ')
    print(*ans)

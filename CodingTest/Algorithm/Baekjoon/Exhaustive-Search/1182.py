import sys
sys.stdin = open('input.txt')

def subset_sum(idx, sub_sum):
    global cnt

    if idx >= N:
        return

    sub_sum += arr[idx]

    if sub_sum == S:
        cnt += 1

    # 현재 arr[idx]를 선택한 경우의 가지
    subset_sum(idx + 1, sub_sum)

    # 현재 arr[idx]를 선택하지 않은 경우의 가지
    subset_sum(idx + 1, sub_sum - arr[idx])

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0

subset_sum(0, 0)
print(cnt)
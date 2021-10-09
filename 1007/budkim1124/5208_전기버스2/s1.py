import sys
sys.stdin = open("input.txt")


def dfs(i):
    global cnt, result
    if cnt > result:
        return

    if i >= N-1:    # 목적지를 지난 경우
        result = min(cnt, result)
        return

    for k in range(1, arr[i]+1):
        cnt += 1
        dfs(i+k)   # k만큼 가야하니까
        cnt -= 1

T = int(input())

for t in range(T):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    arr.append(0)

    result = 10000
    cnt = 0

    dfs(0)

    print("#{} {}".format(t+1, result-1))


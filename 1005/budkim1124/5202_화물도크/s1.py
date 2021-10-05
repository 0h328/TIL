import sys
sys.stdin = open("input.txt")

T = int(input())
for t in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda e : e[1])
    result = 1
    queue = arr[0]

    for i in range(1, len(arr)):
        if arr[i][0] >= queue[1]:
            result += 1
            queue = arr[i]
            queue.append(arr[i])
    print("#{} {}".format(t+1, result))
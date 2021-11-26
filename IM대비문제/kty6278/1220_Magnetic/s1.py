import sys
sys.stdin = open('input.txt')

for tc in range(10):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(100):
        stack = []
        for j in range(100):
            if arr[j][i] == 1:
                stack.append(arr[j][i])
            elif arr[j][i] == 2:
                if stack:
                    cnt += 1
                    stack.clear()
    print("#{} {}".format(tc+1, cnt))
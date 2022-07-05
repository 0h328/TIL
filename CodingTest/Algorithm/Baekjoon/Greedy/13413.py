import sys
sys.stdin = open('input.txt')


T = int(sys.stdin.readline().rstrip())
ans = []
res = 0
arr = []

for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    start = list(sys.stdin.readline().rstrip())
    goal = list(sys.stdin.readline().rstrip())

    for i in range(N):
        if start[i] != goal[i]:
            arr.append(start[i])

    if arr.count("B") >= arr.count("W"):
        res = arr.count("B")
    else:
        res = arr.count("W")
    ans.append(res)
    arr = []

for answer in ans:
    print(answer)

import sys
sys.stdin = open('input.txt')

M = int(input())
N = int(input())

ans = []
for i in range(M, N+1):
    cnt = 0
    for j in range(1, i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 2:
                break
    if cnt == 2:
        ans.append(i)

if len(ans) != 0:
    print(sum(ans))
    print(ans[0])
else:
    print('-1')

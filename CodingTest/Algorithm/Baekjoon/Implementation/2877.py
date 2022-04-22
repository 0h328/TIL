import sys
sys.stdin = open('input.txt')

K = int(input())

cnt = 0
n = 0
ans = []
res = ''
while 1:
    n += 1
    cnt += 2**n # 4, 7, 44, 47, 74, 77, 444, 447, 477, 744, 747, 777
    if cnt >= K:
        break

tmp = K-2**n+1
for i in range(n):
    ans.append(tmp%2)
    tmp//=2

ans.reverse()
for i in range(len(ans)):
    if ans[i] == 1:
        res += '7'
    else:
        res += '4'

print(int(res))


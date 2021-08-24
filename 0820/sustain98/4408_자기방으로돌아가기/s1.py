import sys
sys.stdin = open('input.txt')

t = int(input())
for num in range(1, t+1):           #최대로 겹치는 수를 찾아야함
    n = int(input())                #괄호문제랑 비슷
    dp = [0]*201
    add = []
    res = 0
    for _ in range(n):
        s, e = map(int, input().split())
        s, e = (s+1)//2, (e+1)//2
        if s > e:
            s, e = e, s
        dp[s] += 1
        dp[e] -= 1
        if s == e:
            add.append(s)
    res_idx = 0
    for i in range(1, 201):
        dp[i] += dp[i-1]
        if dp[i] > dp[res_idx]:
            res_idx = i
    res = dp[res_idx]
    if res_idx in add:
        res += 1
    print(dp)
    print('#{} {}'.format(num, res))

#첫 풀이에서 바로 맞은편 방으로 가는 경우를 고려하지 못함

import sys
sys.stdin = open('input.txt')

T = int(input())

def find_max(cnt, start):
    global ans
    if cnt == change or start == N-1:
        og = (data[-2], data[-1])
        if cnt < change:
            while cnt < change:
                data[-1], data[-2] = data[-2], data[-1]
                cnt += 1
        result = ''.join(data)
        data[-2], data[-1] = og
        if int(ans) < int(result):
            ans = result
        return
    else:
        if ans != '0' and int(ans[start-1]) < int(ans[start-1]):
            return
        for i in range(start+1, N):
            data[start], data[i] = data[i], data[start]
            find_max(cnt+1, start+1)
            data[start], data[i] = data[i], data[start]
            find_max(cnt, start+1)


for tc in range(1, T+1):
    data, change = input().split()
    data = list(data)
    N = len(data)
    change = int(change)

    ans = '0'

    find_max(0, 0)

    print('#{} {}'.format(tc, ans))




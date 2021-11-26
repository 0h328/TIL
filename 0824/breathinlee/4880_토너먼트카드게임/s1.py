import sys
sys.stdin = open('input.txt')

# 가위: 1, 바위: 2, 보: 3
def rsp(s, e):
    if data[s] - data[e] == 1 or data[s] - data[e] == -2 or data[s] == data[e]:
        return s
    else:
        return e

def divide(start, end):
    if start == end:
        return start
    else:
        mid = (start + end) // 2
        rs = divide(start, mid)
        re = divide(mid+1, end)
        return rsp(rs, re)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    print('#{} {}'.format(tc, divide(1, N)))

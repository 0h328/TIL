import sys
sys.stdin = open('input.txt')


def tournament(start, end):
    if end-start > 1:
        border = (start + end)//2
        return rps(tournament(start, border), tournament(border+1, end))
    elif start == end:
        return start
    else:
        return rps(start, end)


def rps(s, e): # 가위바위보값을 앞에꺼에다 뒤에껄빼면 그 값이 1,-2인경우 앞에가 win, -1, 2인경우 뒤에가 win, 비기면 앞에가 win
    if l[s] == l[e] or (l[s] - l[e]) in [1, -2]:
        return s
    else:
        return e


t = int(input())
for idx in range(1,t+1):
    n = int(input())
    l = [0] + list(map(int, input().split()))
    print('#{} {}'.format(idx, tournament(1, n)))
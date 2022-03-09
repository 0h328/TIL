import sys
sys.stdin = open('input.txt')

def sum(s):
    tmp = 0
    for i in s:
        if i.isdigit():
            tmp += int(i)
    return tmp

N = int(input())
serial = [sys.stdin.readline().rstrip() for _ in range(N)]
serial.sort(key=lambda x: (len(x), sum(x), x))  # 1. 짧은것 2. 자릿수 합 작은거 3. 사전순
for ans in serial:
    print(ans)


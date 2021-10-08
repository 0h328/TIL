import sys
sys.stdin = open('input.txt')


def dfs(idx):
    global cnt, total, result
    if target <= total:
        if cnt < result: # 총 멈출 수 있는 수(첫번째, 마지막 정류소 제외)
            result = cnt
            return

    for i in range(2, len(bus)):
        total += bus[i]
        cnt += 1
        dfs(bus[i])
        cnt -= 1
        total -= bus[i]


for tc in range(int(input())):
    bus = list(map(int, input().split()))
    n = bus[0]
    cnt = 0 # 멈추는 정류소
    total = 0 # 현재 주유량
    result = len(bus)-2
    target = len(bus) - 1 - bus[1]
    dfs(0)
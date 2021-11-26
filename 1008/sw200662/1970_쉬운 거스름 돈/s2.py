import sys

sys.stdin = open('input.txt')

T = int(input())

def calculate(Won,cnt):
    if len(Won_list) == 0:
        return
    exchange = Won_list.pop(0)
    while Won >= exchange:
        Won -= exchange
        ans_list[cnt] += 1
    calculate(Won,cnt+1)

for tc in range(1, T + 1):
    N = int(input())
    ans_list = [0] * 8
    Won_list = [50000,10000,5000,1000,500,100,50,10]
    calculate(N,0)
    print('#{}'.format(tc))
    print(*ans_list)
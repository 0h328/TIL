import sys
sys.stdin = open('input.txt')

T = int(input())

def oven(piz):
    oven = []
    for _ in range(N):
        oven.append(pizza.pop(0))
    while len(oven) > 1:
        oven[0][1] = oven[0][1] // 2
        if oven[0][1] == 0:
            oven.pop(0)
            if len(pizza) > 0:
                oven.append(pizza.pop(0))
        else:
            oven.append(oven.pop(0))
    return oven[0][0]



for i in range(T):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    pizza = []
    for idx,num in enumerate(lst, start = 1):
        pizza.append([idx, num])
    print('#{} {}'.format(i+1,oven(pizza)))

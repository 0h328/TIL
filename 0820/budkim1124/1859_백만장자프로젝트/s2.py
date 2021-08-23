import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    N = int(input())
    bns = list(map(int, input().split()))
    max_price = bns[-1]
    gain = 0

    for i in range(len(bns)-1, -1, -1):
        if max_price > bns[i]:
            gain += max_price - bns[i]
        else:
            max_price = bns[i]
    print("#{} {}".format(num+1, gain))

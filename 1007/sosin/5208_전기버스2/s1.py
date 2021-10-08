import sys
sys.stdin = open('input.txt')

for  T in range(int(input())):
    result = 1e9
    charges = list(map(int, input().split()))
    N = charges.pop(0)
    stack = [(0, charges[0], 0)]

    while stack:
        idx, charge, cnt = stack.pop()
        for k in range(charge, 0, -1):
            if idx+k >= N-1:
                result = cnt
                break
            if result > cnt+1:
                stack.append((idx+k, charges[idx+k], cnt+1))

    print('#{} {}'.format((T+1), result))

#1 1
#2 2
#3 5
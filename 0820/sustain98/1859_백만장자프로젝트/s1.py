import sys
sys.stdin = open('input.txt')

t = int(input())
for num in range(1, t+1):
    n = int(input())
    l = list(map(int, input().split()))
    res = 0
    max_val = l[-1]
    for i in range(n-1,-1,-1): # 더 큰걸 만나면 max_val을그 값으로 변경.
        if l[i] > max_val:
            max_val = l[i]
        else:
            res += max_val-l[i]
    print('#{} {}'.format(num, res))

import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    res = 0
    num = int(input())
    l = list(map(int, input().split())) + [0,0]

    for i in range(2, num):
        max_height = max(l[i-2], l[i-1], l[i+1], l[i+2])
        if max_height < l[i]:
            res += l[i] - max_height
    print('#{0} {1}'.format(t, res))




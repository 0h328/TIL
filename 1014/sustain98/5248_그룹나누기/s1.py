import sys
sys.stdin = open('input.txt')

def find_set(val):
    if s[val] == val:
        return val
    else:
        return find_set(s[val])

t = int(input())
for idx in range(1, t+1):
    n, m = map(int, input().split())
    l = list(map(int, input().split()))
    s = [i for i in range(n+1)]
    for i in range(m):
        s[find_set(l[i*2])] = find_set(l[i*2 + 1])

    print('#{} {}'.format(idx, len(list(filter(lambda x: x[0] == x[1], enumerate(s))))-1))
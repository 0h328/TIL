import sys
from itertools import combinations

sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, b = map(int, input().split())
    height_list = list(map(int, input().split()))
    height_list.sort()

    kind = []
    for i in range(n+1):
        kind.append(list(combinations(height_list, i)))
    kind_list = []
    for ki in kind:
        for i in ki:
            kind_list.append(sum(i))
    kind_list = list(set(kind_list))

    result = kind_list[-1]
    for kind in kind_list:
        if kind - b >= 0:
            if result > kind - b:
                result = kind - b
    print('#{} {}'.format(tc+1, result))


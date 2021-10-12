import sys
sys.stdin = open('input.txt')

from itertools import combinations

for T in range(int(input())):
    result = 1e9
    N, B = map(int, input().split())
    heights = tuple(map(int, input().split()))

    for i in range(1, N+1):
        for case in combinations(heights, i):
            if sum(case)>=B:
                result = min(result, sum(case))

    print('#{} {}'.format((T+1), result-B))

#1 1
#2 4
#3 27
#4 11
#5 42
#6 32
#7 2
#8 3
#9 25
#10 0

from itertools import combinations
import sys
sys.stdin = open('input.txt')


for tc in range(int(input())):
    num = [i for i in range(int(input()))]
    my_list = [list(map(int, input().split())) for _ in range(len(num))]
    max_v = []
    result_list = []
    for i in combinations(num, len(num)//2):
        result_list.append(i)
    for j in range(len(result_list)//2):
        s1 = []
        s2 = []
        for x, y in combinations(result_list[j], 2):
            ss1 = my_list[x][y] + my_list[y][x]
            s1.append(ss1)
        for x, y in combinations(result_list[-j-1], 2):
            ss2 = my_list[x][y] + my_list[y][x]
            s2.append(ss2)
        ans = abs(sum(s1)-sum(s2))
        max_v.append(ans)
    print('#{} {}'.format(tc+1, min(max_v)))
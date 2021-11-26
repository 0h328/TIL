import sys
sys.stdin = open('input.txt')
from itertools import combinations

T = int(input())

def sinerge(a,b):
    global ans
    temp_1 = 0
    temp_2 = 0
    for c in a:
        temp_1 += sinerge_list[c[0]][c[1]]
        temp_1 += sinerge_list[c[1]][c[0]]
    for d in b:
        temp_2 += sinerge_list[d[0]][d[1]]
        temp_2 += sinerge_list[d[1]][d[0]]
    temp_ans = abs(temp_1 - temp_2)

    if ans > temp_ans:
        ans = temp_ans

for tc in range(1,T+1):
    N = int(input())
    sinerge_list = [list(map(int,input().split())) for _ in range(N)]
    find_list_range = list(range(N))
    find_list = list(combinations(find_list_range,N//2))
    ans = 987654321
    for i in range(len(find_list)):
        find_temp = find_list_range[::]
        for a in find_list[i]:
            find_temp.remove(a)
        find_temp_sinerge = list(combinations(find_temp,2))
        find_temp_2_singere = list(combinations(find_list[i],2))
        sinerge(find_temp_sinerge,find_temp_2_singere)
    print('#{} {}'.format(tc,ans))
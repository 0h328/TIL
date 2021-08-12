import sys
sys.stdin = open('input.txt')


for tc in range(10):        # Test Case 10번 반복
    N = int(input())        # 숫자 입력 해줘야 하니까
    L = [list(map(int, input().split())) for _ in range(100)]   # 100 * 100 리스트

    max_value = 0       # 초기값 설정 (비교)

    for i1 in range(len(L)):            #
        my_row = []                     #
        for i2 in range(len(L[i1])):    #
            my_row.append(L[i1][i2])    #
        if sum(my_row) > max_value:     #
            max_value = sum(my_row)     #

    idx = 0                             # 정사각형이 아니라면?
    for j1 in range(len(L[idx])):       # idx = 0, 1, 2 ...
        my_col = []                     #
        for j2 in range(len(L)):        #
            my_col.append(L[j2][j1])    #
        if sum(my_col) > max_value:     #
            max_value = sum(my_col)     #
        idx += 1                        # 정사각형이 아니라면?

    my_llist = []                       #
    for k in range(len(L)):
        my_llist.append(L[k][k])
    if sum(my_llist) > max_value:
        max_value = sum(my_llist)

    my_rlist = []                       #
    for l in range(len(L)):
        my_rlist.append(L[l][len(L)-l-1])
    if sum(my_rlist) > max_value:
        max_value = sum(my_rlist)

    print('#{} {}'.format(tc+1, max_value))
import sys
sys.stdin = open('input.txt')


for tc in range(10):        # Test Case 10번 반복
    N = int(input())        # 숫자 입력 해줘야 하니까
    L = [list(map(int, input().split())) for _ in range(100)]   # 100 * 100 리스트

    max_value = 0       # 초기값 설정 (비교)

    for i1 in range(len(L)):            # 부모 리스트 길이
        my_row = []
        for i2 in range(len(L[i1])):    # 자식 리스트 길이
            my_row.append(L[i1][i2])    # 자식 리스트 애들 다 넣음
        if sum(my_row) > max_value:     # 다 더해서 크면
            max_value = sum(my_row)     # 값으로


    for j1 in range(len(L[0])):         # 자식 길이가 다 같으니 [0]
        my_col = []
        for j2 in range(len(L)):        # 부모 리스트 길이
            my_col.append(L[j2][j1])    # 먼저 고정하는 것이 바깥 for문
        if sum(my_col) > max_value:
            max_value = sum(my_col)


    my_llist = []
    for k in range(len(L)):             # 좌 대각 길이 (초기화 필요X)
        my_llist.append(L[k][k])
    if sum(my_llist) > max_value:
        max_value = sum(my_llist)


    my_rlist = []
    for l in range(len(L)):             # 우 대각 길이 (초기화 필요X)
        my_rlist.append(L[l][len(L)-l-1])
    if sum(my_rlist) > max_value:
        max_value = sum(my_rlist)

    print('#{} {}'.format(tc+1, max_value))
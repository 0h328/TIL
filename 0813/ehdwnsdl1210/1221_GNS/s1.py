import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):

    N, B = map(str, input().split())
    L = input().split()     # split은 리스트로 만들어줌

    # 숫자로, 값으로 딕셔너리
    num = {'ZRO':0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9}
    reverse_num = {0:'ZRO', 1:'ONE', 2:'TWO', 3:'THR', 4:'FOR', 5:'FIV', 6:'SIX', 7:'SVN', 8:'EGT', 9:'NIN'}

    my_list = []
    for i in L:
        my_list.append(num[i])  # 숫자로 변환

    my_list.sort()  # 숫자로 됬으니 오름차순 정렬

    my_result = []
    for j in my_list:
        my_result.append(reverse_num[j])    # 다시 값으로 변환

    print(N)            # #번호
    print(*my_result)   # list에 있는 값들을 풀어서 출력
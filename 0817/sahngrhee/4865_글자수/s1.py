import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    str1 = input()
    str2 = input()
    N = len(str2)
    deleted_str = set(str1)

    cnt_list = []
    for char in deleted_str:
        cnt = 0
        for i in range(N):
            if str2[i] == char:
                cnt += 1
        cnt_list.append(cnt)
    ans = max(cnt_list)

    print('#{} {}'.format(test_case, ans))
import sys
sys.stdin = open('input.txt')

T = int(input())

def find(left, right, target):
    global ans, flag
    if right >= left:
        mid = (left + right) // 2
        if target == N_list[mid]:
            ans += 1
            return
        elif target < N_list[mid]:
            if flag == 1:
                return
            flag = 1
            find(left, mid - 1, target)
        elif target > N_list[mid]:
            if flag == -1:
                return
            flag = -1
            find(mid + 1, right, target)


for tc in range(1, T + 1):
    N, M = map(int, (input().split()))
    N_list = list(map(int, input().split()))
    N_list.sort()
    M_list = list(map(int, input().split()))
    ans = 0
    for i in M_list:
        flag = 0
        find(0, len(N_list) - 1, i)
    print('#{} {}'.format(tc, ans))
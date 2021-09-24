import sys

sys.stdin = open('input.txt')


def in_order(node):
    global ans

    if len(WORD[node]) == 4:
        in_order(int(WORD[node][2]))
        ans += WORD[node][1]
        in_order(int(WORD[node][3]))
        return  # 처음에 이 리턴을 안줬더니 돌아와서 else로 가버려서 실행을 해버림 그래서 리턴

    if len(WORD[node]) == 3:
        in_order(int(WORD[node][2]))
        ans += WORD[node][1]

    else:
        ans += WORD[node][1]


for i in range(10):
    T = int(input())
    ans = ''
    WORD = [0] + [list(map(str, input().split())) for _ in range(T)]
    in_order(1)
    print('#{} {}'.format(i + 1, ans))

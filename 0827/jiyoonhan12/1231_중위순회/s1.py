import sys
sys.stdin = open('input.txt')


def in_order(v):
    global word
    if v:
        in_order(left[v])
        word += temp[v-1][1]
        in_order(right[v])


for t in range(1, 11):
    N = int(input())
    temp = [input().split() for _ in range(N)]
    left = [0] * (N+1)
    right = [0] * (N+1)
    word = ''

    for idx, char, *child in temp:
        if child:
            left[int(idx)] = int(child[0])
            if len(child) == 2:
                right[int(idx)] = int(child[1])

    in_order(1)
    print('#{} {}'.format(t, word))
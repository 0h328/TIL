import sys
sys.stdin = open('input.txt')


for _ in range(10):
    idx = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    loc_c = ladders[-1].index(2)

    for loc_r in range(99, 0, -1):
        if loc_c > 0 and ladders[loc_r][loc_c - 1] == 1:                #다른 방법 없을까....
            while loc_c > 0 and ladders[loc_r][loc_c - 1] == 1:
                loc_c -= 1
        elif loc_c < 99 and ladders[loc_r][loc_c + 1]:
            while loc_c < 99 and ladders[loc_r][loc_c + 1] == 1:
                loc_c += 1

    print('#{} {}'.format(idx, loc_c))


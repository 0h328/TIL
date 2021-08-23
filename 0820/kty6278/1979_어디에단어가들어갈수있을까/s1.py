import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T + 1):
    space, words = map(int, input().split())

    space_list = []
    for s1 in range(space):
        space_list.append(list(map(int, input().split())))

    # 가능한 단어 개수
    count = 0
    for i in range(space):
        # 가능한 가로 빈칸 개수
        plus = 0
        for j in range(space):
            # 비어있는 칸이 있는 경우 빈칸 개수 +1
            if space_list[i][j] == 1:
                plus += 1
            # 비어있는 칸이 없는 경우지만 빈칸 개수가 words의 길이와 같다면 단어 개수 +1
            if space_list[i][j] == 0 or j == space - 1:
                if plus == words:
                    count += 1
                plus = 0

        # 가능한 세로 빈칸 개수
        for j in range(space):
            if space_list[j][i] == 1:
                plus += 1
            # 비어있는 칸이 없는 경우지만 빈칸 개수가 words의 길이와 같다면 단어 개수 +1
            if space_list[j][i] == 0 or j == space - 1:
                if plus == words:
                    count += 1
                plus = 0

    print('#{} {}'.format(t, count))
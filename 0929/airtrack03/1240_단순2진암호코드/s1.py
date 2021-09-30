import sys
sys.stdin = open('input.txt')

T = int(input())

code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]
code[0][0][0][1][1][0][1] = 0
code[0][0][1][1][0][0][1] = 1
code[0][0][1][0][0][1][1] = 2
code[0][1][1][1][1][0][1] = 3
code[0][1][0][0][0][1][1] = 4
code[0][1][1][0][0][0][1] = 5
code[0][1][0][1][1][1][1] = 6
code[0][1][1][1][0][1][1] = 7
code[0][1][1][0][1][1][1] = 8
code[0][0][0][1][0][1][1] = 9

def binary_to_eight(start):
    while len(eight) != 8:
        num = code[data[start-6]][data[start-5]][data[start-4]][data[start-3]][data[start-2]][data[start-1]][data[start]]
        eight.append(num)
        start -= 7

    return eight


for tc in range(1, T+1):
    N, M = map(int, input().split())

    eight = []
    for _ in range(N):
        data = list(map(int, list(input())))

        if eight:
            continue
        start = 0
        for i in range(M-1, -1, -1):
            if data[i] == 1:
                start = i
                break
        if start:
            eight = binary_to_eight(start)
    ans = 0
    temp = 0
    # eight 순서 반대로 되어 있음
    for i in range(8):
        if i & 1:
            temp += 3 * eight[i]
        else:
            temp += eight[i]

    if not temp % 10:
        ans = sum(eight)


    print('#{} {}'.format(tc, ans))




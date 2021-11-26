import sys
sys.stdin = open('input.txt')

# input을 받아올 때 split으로 받아오지 말고 input() 그대로 받아와보자!

amho = {  # 딕셔너리
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 배열의 세로, 가로 길이
    code = [input() for _ in range(N)]
    # print(code)
    ans = ''
    for i in code:
        for j in range(M-1, -1, -1):
            if i[j] == '1':
                ans = i[j-55:j+1]
                break
    # print(ans)

    result = []

    for i in range(0, 56, 7):
        result.append(amho[ans[i:i + 7]])

    # print(result)
    check = (result[0] + result[2] + result[4] + result[6]) * 3 + result[1] + result[3] + result[5] + result[7]

    if not check % 10:
        print('#{} {}'.format(tc, sum(result)))
    else:
        print('#{} {}'.format(tc, 0))

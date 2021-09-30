import sys
sys.stdin = open('input.txt')


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Secret = [input() for _ in range(N)]
    P = {
        '0001101': 0,
        '0011001': 1,
        '0010011': 2,
        '0111101': 3,
        '0100011': 4,
        '0110001': 5,
        '0101111': 6,
        '0111011': 7,
        '0110111': 8,
        '0001011': 9,
    }

    my_str = []
    for info in Secret:
        new_info = info.strip('0')
        if new_info:
            new_info = '0' * (56-len(new_info)) + new_info
            my_str.append(new_info)

    my_str = list(set(my_str))

    result = []
    for i in range(8):
        result.append(P[my_str[0][i*7:i*7+7]])

    cert = 0
    for j in range(8):
        if j % 2:
            cert += result[j]
        else:
            cert += 3 * result[j]

    if cert % 10:
        ans = 0
    else:
        ans = sum(result)

    print('#{} {}'.format(test_case, ans))


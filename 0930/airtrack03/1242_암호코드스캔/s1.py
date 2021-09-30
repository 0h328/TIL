from math import gcd
import sys
sys.stdin = open('input.txt')

T = int(input().strip())

ratio = {
    '112': 0,
    '122': 1,
    '221': 2,
    '114': 3,
    '231': 4,
    '132': 5,
    '411': 6,
    '213': 7,
    '312': 8,
    '211': 9,
}

def ascii_to_hex(c):
    if '0' <= c <= '9':
        return ord(c) - ord('0')
    return ord(c) - ord('A') + 10


def hex_to_binary(num):
    result = ''
    for i in range(3, -1, -1):
        if num & (1 << i):
            result += '1'
        else:
            result += '0'
    return result


for tc in range(1, T+1):
    N, M = map(int, input().rstrip().split())
    ans = 0
    targets = set()

    for _ in range(N):
        data = input().rstrip()
        data = data.strip('0')
        if data:
            new_row = ''

            for col in range(len(data)):
                new_row += hex_to_binary(ascii_to_hex(data[col]))
            new_row = new_row.strip('0')


            idx = len(new_row) - 1
            eight = []
            cnt = [0, 0, 0]
            while idx > -1:
                if new_row[idx] == '1':
                    while new_row[idx] == '1':
                        cnt[0] += 1
                        idx -= 1
                    while new_row[idx] == '0':
                        cnt[1] += 1
                        idx -= 1
                    while idx > -1 and new_row[idx] == '1':
                        cnt[2] += 1
                        idx -= 1
                else:
                    idx -= 1
                    continue

                my_gcd = gcd(gcd(cnt[0], cnt[1]), gcd(cnt[1], cnt[2]))
                temp = ''
                for i in range(3):
                    temp += str(cnt[i] // my_gcd)
                cnt = [0, 0, 0]

                eight.append(str(ratio.get(temp)))

                if len(eight) == 8:
                    targets.add(''.join(eight))
                    eight = []

    for target in targets:
        target = list(map(int, list(target)))
        temp = 0
        for i in range(8):
            if i & 1:
                temp += int(target[i]) * 3
            else:
                temp += int(target[i])

        if not temp % 10:
            ans += sum(list(map(int, target)))

    print('#{} {}'.format(tc, ans))
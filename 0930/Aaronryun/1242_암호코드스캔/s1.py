import sys

sys.stdin = open('input.txt')

decode = {'211': 0, '221': 1, '122': 2, '411': 3, '132': 4, '231': 5, '114': 6, '312': 7, '213': 8, '112': 9}
hex = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
       '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

for test in range(1, 1 + int(input())):
    N, M = map(int, input().split())
    data = [input().strip() for _ in range(N)]

    for i in range(N):
        temp = ''
        for j in data[i]:
            temp += hex[j]
        data[i] = temp

    result = []
    visited = []
    answer = 0
    for i in range(N):
        a = b = c = 0
        # cba == 211 == 0
        for j in range(M * 4 - 1, -1, -1):
            if b == 0 and c == 0 and data[i][j] == '1':
                a += 1
            elif a and c == 0 and data[i][j] == '0':
                b += 1
            elif a and b and data[i][j] == '1':
                c += 1

            if a and b and c and data[i][j] == '0':
                min_num = min(c, b, a)
                c //= min_num
                b //= min_num
                a //= min_num
                string = str(c) + str(b) + str(a)
                result.append(decode[string])
                a = b = c = 0

            if len(result) == 8:
                result = result[::-1]
                value = (result[0] + result[2] + result[4] + result[6]) * 3 + \
                        (result[1] + result[3] + result[5]) + result[7]

                # if answer:
                #     break

                if result not in visited and not value % 10:
                    answer += sum(result)
                visited.append(result)
                result = []

    print('#{} {}'.format(test, answer))

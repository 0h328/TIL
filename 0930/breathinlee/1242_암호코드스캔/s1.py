import sys
sys.stdin = open('input.txt')

# 미완성

dict_patterns = {'3211': '0', '2221': '1', '2122': '2', '1411': '3', '1132': '4', '1231': '5', '1114': '6', '1312': '7', '1213': '8', '3112': '9'}
hex_to_binary = {'0':'0000', '1':'0001', '2':'0010', '3':'0011',
                 '4':'0100', '5':'0101', '6':'0110', '7':'0111',
                 '8':'1000', '9':'1001', 'A':'1010', 'B':'1011',
                 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]
    binary_num = [''] * N

    for row in range(N):
        for col in range(M):
            binary_num[row] += hex_to_binary.get(arr[row][col])

        binary_row = binary_num[row]
        if '1' in binary_row:
            opposite_col = binary_row[::-1].index('1')
            break
        else:
            continue

        col = M - opposite_col
        a = b = c = d = 0
        for i in range(col, -1, -1):
            if c == 0 and binary_row[i] == '1':
                d += 1
            elif d > 0 and binary_row[i] == '0':
                c += 1
            elif c > 0 and binary_row[i] == '1':
                b += 1
            elif b > 0 and binary_row[i] == '0':
                a += 1

        gcd1 = gcd(a, b)
        gcd2 = gcd(b, c)
        abcd_gcd = min(gc1, gcd2)
        print(abcd_gcd)
        """
        code_check = ''
        code_check += a // abcd_gcd
        code_check += b // abcd_gcd
        code_check += c // abcd_gcd
        code_check += d // abcd_gcd
        
        origin_code = dict_patterns.get(code_check)
        code = ''
        for j in range(len(origin_code)):
            if j % 2:
                code += origin_code[j]
            else:
                code += origin_code[j] * 3
        
        if code % 10:
            ans = 0
        else:
            ans = sum(origin_code)
        
        print('#{} {}'.format(tc, ans))
        """
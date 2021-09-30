'''
한줄에 암호가 여러개인 경우를 해결하지 못하겠다!!!
'''
def ascii_to_hex(c):
    if c <= '9':
        return ord(c) - ord('0')
    else:
        return ord(c) - ord('A') + 10

def hex_to_binary(x):
    for i in range(4):
        t.append(asc[x][i])


import sys
sys.stdin = open('input.txt')


T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    Secret = [input() for _ in range(N)]
    asc = [[0, 0, 0, 0],  # 0
           [0, 0, 0, 1],  # 1
           [0, 0, 1, 0],  # 2
           [0, 0, 1, 1],  # 3
           [0, 1, 0, 0],  # 4
           [0, 1, 0, 1],  # 5
           [0, 1, 1, 0],  # 6
           [0, 1, 1, 1],  # 7
           [1, 0, 0, 0],  # 8
           [1, 0, 0, 1],  # 9
           [1, 0, 1, 0],  # A
           [1, 0, 1, 1],  # B
           [1, 1, 0, 0],  # C
           [1, 1, 0, 1],  # D
           [1, 1, 1, 0],  # E
           [1, 1, 1, 1]]  # F
    ans = 0
    my_str = []
    for info in Secret:
        new_info = info.strip('0')
        if new_info:
            my_str.append(new_info)
    my_str = list(set(my_str))

    for i in range(len(my_str)):
        t = []
        for j in range(len(my_str[i])):
            hex_to_binary(ascii_to_hex(my_str[i][j]))

        t2 = ''.join(map(str, t))
        t3 = t2.strip('0')
        if len(t3) % 56:
            t3 = '0' * ((len(t3)//56+1)*56-len(t3)) + t3

        a = len(t3)//56
        P = {}

        b = '0' * a + '0' * a + '0' * a + '1' * a + '1' * a + '0' * a + '1' * a
        c = '0' * a + '0' * a + '1' * a + '1' * a + '0' * a + '0' * a + '1' * a
        d = '0' * a + '0' * a + '1' * a + '0' * a + '0' * a + '1' * a + '1' * a
        e = '0' * a + '1' * a + '1' * a + '1' * a + '1' * a + '0' * a + '1' * a
        f = '0' * a + '1' * a + '0' * a + '0' * a + '0' * a + '1' * a + '1' * a
        g = '0' * a + '1' * a + '1' * a + '0' * a + '0' * a + '0' * a + '1' * a
        h = '0' * a + '1' * a + '0' * a + '1' * a + '1' * a + '1' * a + '1' * a
        u = '0' * a + '1' * a + '1' * a + '1' * a + '0' * a + '1' * a + '1' * a
        m = '0' * a + '1' * a + '1' * a + '0' * a + '1' * a + '1' * a + '1' * a
        k = '0' * a + '0' * a + '0' * a + '1' * a + '0' * a + '1' * a + '1' * a

        P[b] = 0
        P[c] = 1
        P[d] = 2
        P[e] = 3
        P[f] = 4
        P[g] = 5
        P[h] = 6
        P[u] = 7
        P[m] = 8
        P[k] = 9
        result = []
        for j in range(8):
            result.append(P[t3[j*(7*a):j*(7*a)+(7*a)]])

        cert = 0
        for j in range(8):
            if j % 2:
                cert += result[j]
            else:
                cert += 3 * result[j]

        if cert % 10:
            r1 = 0
        else:
            r1 = sum(result)

        ans += r1
    print('#{} {}'.format(test_case, ans))


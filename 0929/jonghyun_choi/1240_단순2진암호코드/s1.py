import sys
sys.stdin = open('input.txt')

C = int(input())

num_data = {
    '0001101': 0 ,
    '0011001': 1 ,
    '0010011': 2 ,
    '0111101': 3 ,
    '0100011': 4 ,
    '0110001': 5 ,
    '0101111': 6 ,
    '0111011': 7 ,
    '0110111': 8 ,
    '0001011': 9
}

def seperate(data):
    res = []
    for i in range(0, len(data), 7):
        p = data[i : i + 7]
        res.append(num_data[p])
    return res


def confirm(code):
    ans = 0
    odd = 0
    even = 0
    for i in range(len(code) - 1):
        ans += code[i]
        if i % 2:
            even += code[i]
        else:
            odd += code[i]
    res = odd * 3 + even + code[len(code) - 1]
    ans += code[len(code) - 1]
    if res % 10:
        return False
    else:
        return ans



for case in range(C):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]

    real_data = []
    for i in range(N):
        for j in range(M-1, -1, -1):
            if data[i][j] == '1':
                p = data[i][j-55:j+1]
                real_data.append(p)
                break
    con = []
    ans = 0
    for i in real_data:
        if confirm(seperate(i)) and confirm(seperate(i)) not in con:
            con.append(confirm(seperate(i)))
            ans += confirm(seperate(i))

    print('#{} {}'.format(case + 1, ans))








import sys
sys.stdin = open('input.txt')

# 아직 미완성

C = int(input())

# num_data = {
#     0 : '0001101' ,
#     1 : '0011001' ,
#     2 : '0010011' ,
#     3 : '0111101' ,
#     4 : '0100011' ,
#     5 : '0110001' ,
#     6 : '0101111' ,
#     7 : '0111011' ,
#     8 : '0110111' ,
#     9 : '0001011'
# }

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

hex_data = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111',
}


def interval(data):
    for i in range(len(data)):
        pass


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


for case in range(13):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    change_data = ['' for _ in range(len(data))]
    real_data = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] != '0':
                change_data[i] += hex_data[data[i][j]]
            else:
                change_data[i] += '0'
    for i in change_data:
        tmp = i.rstrip('0')
        if tmp and tmp not in real_data:
            real_data.append(tmp)
    print(real_data)

    for i in range(len(real_data)):
        for j in range(len(real_data[i])-1, -1, -1):
            if data[i][j] == '1':
                p = data[i][j-55:j+1]
                real_data.append(p)
                break
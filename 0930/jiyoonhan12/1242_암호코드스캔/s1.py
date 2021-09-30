import sys
sys.stdin = open('input.txt')


sheet = [
    [2, 1, 1],
    [2, 2, 1],
    [1, 2, 2],
    [4, 1, 1],
    [1, 3, 2],
    [2, 3, 1],
    [1, 1, 4],
    [3, 1, 2],
    [2, 1, 3],
    [1, 1, 2],
]

binary = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111',
}

def verify(code):
    if not ((code[1] + code[3] + code[5] + code[7]) * 3 + code[0] + code[2] + code[4] + code[6]) % 10:
        return 1
    else:
        return 0


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(set(input().strip() for _ in range(N)))
    codenum = []
    ans = 0

    for i in range(len(arr)):
        temp = ''
        for j in range(M):
            temp += binary[arr[i][j]]
        temp = temp.rstrip('0')

        code = []
        z1, o1, z2, o2 = 0, 0, 0, 0
        for k in range(len(temp)-1, -1, -1):
            if temp[k] == '1' and not z2:
                o2 += 1
            elif temp[k] == '0' and not o1:
                z2 += 1
            elif temp[k] == '1' and not z1:
                o1 += 1
            elif temp[k] == '0':
                if temp[k-1] == '1':# 다음 암호 끝 지점 = 잠깐 멈춤
                    n = min(o1, z2, o2) # 암호당 숫자 몇 번 곱해졌는지 (길이 관련)
                    code.append((sheet.index([o1 // n, z2 // n, o2 // n])))
                    o1, z2, o2 = 0, 0, 0
                    if len(code) == 8:
                        if verify(code) and code not in codenum:
                            ans += sum(code)
                            codenum.append(code)
                        code = []

    print('#{} {}'.format(t, ans))
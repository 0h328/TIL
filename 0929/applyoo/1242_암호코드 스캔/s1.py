import sys
sys.stdin = open('input.txt')


t1 = {'211': 0, '221': 1, '122': 2, '411': 3,
      '132': 4, '231': 5, '114': 6, '312': 7,
      '213': 8, '112': 9}
t2 = {}
for i in range(0, 16):  # 16진수 => 2진수 변환 딕셔너리 생성
    if i < 10: t2[str(i)] = '{0:0>4}'.format(str(bin(i))[2:])
    else: t2[chr(55+i)] = '{0:0>4}'.format(str(bin(i))[2:])

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]

    binary = [''] * N
    for i in range(N):  # 16 => 2진수 변환
        for var in arr[i]:
            binary[i] += t2[var]

    ans = 0
    v, key = [], []
    for n in range(N):
        a = b = c = 0
        if '1' in binary[n]:  # 암호가 있는 경우
            for m in range(M*4-1,-1,-1):
                if b == 0 and c == 0 and binary[n][m] == '1':  # 맨 뒤의 1의 개수
                    a += 1
                elif a and c == 0 and binary[n][m] == '0':  # 1 다음 0의 개수
                    b += 1
                elif a and b and binary[n][m] == '1':  # 1, 0 다음의 1 개수
                    c += 1
                elif c and binary[n][m] == '0':  # 다시 0이 나온 경우
                    w = min(a, b, c)  # 최솟값(가중치)
                    key.append(t1[str(c//w) + str(b//w) + str(a//w)])  # 3개 자리수만으로 판별
                    a = b = c = 0  # 0으로 초기화
                    if len(key) == 8:  # 암호 해독 시도가 가능한 경우
                        if key not in v:  # 반드시 37 line이랑 개행되어 있어야 함
                            if ((key[7]+key[5]+key[3]+key[1])*3 + key[0]+key[2]+key[4]+key[6]) % 10 == 0:  # 암호 검증
                                ans += sum(key)
                            v.append(key)
                        key = []
    print('#{} {}'.format(test_case, ans))
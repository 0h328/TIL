import sys
sys.stdin = open('input.txt')


t1 = {'211': 0, '221': 1, '122': 2, '411': 3,
      '132': 4, '231': 5, '114': 6, '312': 7,
      '213': 8, '112': 9}

T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input()[:M] for _ in range(N)]

    ans = 0
    v, key = [], []
    for n in range(N):
        a = b = c = 0
        if '1' not in arr[n]:
            continue
        for m in range(M - 1, -1, -1):
            if b == 0 and c == 0 and arr[n][m] == '1':
                a += 1
            elif a and c == 0 and arr[n][m] == '0':
                b += 1
            elif a and b and arr[n][m] == '1':
                c += 1
            elif c and arr[n][m] == '0':
                key.append(t1[str(c) + str(b) + str(a)])
                a = b = c = 0
                if len(key) == 8:
                    if key not in v:
                        if ((key[7] + key[5] + key[3] + key[1]) * 3 + key[0] + key[2] + key[4] + key[6]) % 10 == 0:
                            ans += sum(key)
                        v.append(key)
                    key = []
    print('#{} {}'.format(test_case, ans))

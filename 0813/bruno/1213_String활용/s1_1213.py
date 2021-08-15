# 엣지케이스 포섭 필요.. 왜 9개만 정답??

import sys
sys.stdin = open('input.txt')

for _ in range(10):
    T = int(input())
    search = input()
    string = input()
    cnt = 0

    for i in range(len(string) - len(search)):
        if string[i:i+len(search)] == search:
            cnt += 1
    print('#{} {}'.format(T, cnt))

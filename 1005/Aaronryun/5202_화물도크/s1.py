import sys

sys.stdin = open('input.txt')

for test in range(1, 1 + int(input())):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data.sort(key=lambda x: (x[1], x[0]))
    data.reverse()

    s, e = data.pop()
    answer = 1
    while data:
        ns, ne = data.pop()
        if e <= ns:
            s, e = ns, ne
            answer += 1

    print('#{} {}'.format(test, answer))

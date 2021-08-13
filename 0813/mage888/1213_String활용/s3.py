import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    n = int(input())
    p = input()
    t = input()

    print('#{} {}'.format(n, t.count(p)))


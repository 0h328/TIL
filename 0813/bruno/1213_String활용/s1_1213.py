
import sys
sys.stdin = open('input.txt', encoding='UTF-8')

for _ in range(10):
    T = int(input())
    search = input()
    string = input()
    cnt = 0

    for i in range(len(string) - len(search) + 1):
        if string[i:i+len(search)] == search:
            cnt += 1
    print('#{} {}'.format(T, cnt))

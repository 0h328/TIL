import sys
# 그냥 입력받으니 에러발생해서 encoding 방식 변경
sys.stdin = open('input.txt', 'rt', encoding='UTF8')

for _ in range(10):
    tc = input()
    target = input()
    data = input()

    ans = data.count(target)
    print('#{} {}'.format(tc, ans))
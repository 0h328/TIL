import sys
sys.stdin = open('input.txt', encoding='utf-8')


def call(depth):
    if depth == N:
        return
    a = '__'*depth
    b = arr[depth][1]
    c = num[depth]

    print('{0}{1}님 안녕하세요! {3}{0}{1}님 숫자가 어떻게 되시나요? {3}{0}{1}: 제 숫자는 {2} 입니다!'.format(a, b, c, '\n'))

    if depth != N-1:
        d = arr[depth + 1][1]
        print('{0}앗 그러면 {1}님께 전화해서 숫자좀 여쭤보고 올게요! 통화 유지해주세요!'.format(a, d))

    call(depth+1)

    if depth != N-1:
        print('{0}{1}님, 기다리셨죠?'.format(a, b))

    print('{0}숫자의 합은 {1} 입니다!'.format(a, sum(num[depth:])))


N = 10
arr = [list(input().split()) for _ in range(N)]
num = list(map(int, input().split()))

call(0)

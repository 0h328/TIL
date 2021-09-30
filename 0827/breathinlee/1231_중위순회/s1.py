import sys
sys.stdin = open('input.txt')

# 중위순회
# 1 W 2 3 : W가 1번 정점에 해당하며, 자식이 2, 3번
# 2 F 4 5
# 3 R 6 7
# 4 O 8
# 5 T
# 6 A
# 7 E
# 8 S

def in_order(i):
    global ans
    if i <= N:
        in_order(i*2)
        ans += alphabet[i]
        in_order(i*2+1)

for tc in range(1, 11):
    N = int(input())
    alphabet = [0] * (N+1)
    ans = ''

    for k in range(N):
        temp = input().split()
        alphabet[k+1] = temp[1]

    in_order(1)

    print('#{} {}'.format(tc, ans))
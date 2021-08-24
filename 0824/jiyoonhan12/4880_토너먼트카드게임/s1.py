import sys
sys.stdin = open('input.txt')

# 1가위 2바위 3보 / 같은 카드면 숫자 적은 사람이 승

def solve(start, end):
    if start == end: # 리스트에 숫자 1개 남을 때까지 반복해서 그 idx 반환
        return start

    left = solve(start, (start+end)//2)
    right = solve((start+end)//2 + 1, end)

    if (cards[left] == 1 and cards[right] == 2 or
        cards[left] == 2 and cards[right] == 3 or
        cards[left] == 3 and cards[right] == 1
    ):
        return right
    else: # 무승부여도 앞사람이 이김
        return left

T = int(input())
for t in range(1, T+1):
    N = int(input())
    cards = [0] + list(map(int, input().split()))
    print('#{} {}'.format(t, solve(1, N)))
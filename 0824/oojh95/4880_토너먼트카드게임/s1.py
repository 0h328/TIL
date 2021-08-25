import sys
sys.stdin = open('input.txt')

def check(arr,N):
    stack = []
    if len(arr) == 1:
        return winner.pop()
    else:
        for i in range(0, N-1, 2):
            if card[i] - card[i+1] == 1 or card[i] - card[i+1] == 0 or card[i] - card[i+1] == -2:
                winner.append(i)
                stack.append(card[i])
            else:
                winner.append(i+1)
                stack.append(card[i+1])
        check(stack, len(stack))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(int, input().split()))
    winner = []

    print(check(card, N))

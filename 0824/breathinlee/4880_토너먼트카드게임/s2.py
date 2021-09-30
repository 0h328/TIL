import sys
sys.stdin = open('input.txt')



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    card = []
    for i in range(N):
        card.append((i+1, arr[i]))
    print(card)

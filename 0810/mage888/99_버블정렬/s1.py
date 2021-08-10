import sys
sys.stdin = open('input.txt')

T = int(input())
Numbers = list(map(int,input().split()))


for i in range(0, T-1):
# for i in range(len(Numbers)-1, 0, -1):
    for j in range(i+1, T):
        if Numbers[i] > Numbers[j]:
            Numbers[i], Numbers[j] = Numbers[j], Numbers[i]

print(Numbers)
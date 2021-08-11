import sys
sys.stdin = open('input.txt')

T = int(input())
N = int(input())
# N = list(map,int(input().split()))
Card_idx = [0] * (T + 1)

# for j in range(1, T+1):
for test_case in range(1, T + 1):
    Card_idx[N % 10] += 1
    N //= 10

i = 0
run = trp = 0

while i < 10:

    if Card_idx[i] >= 3:
        Card_idx[i] -= 3
        trp += 1
        continue

    if Card_idx[i] >= 1 and Card_idx[i+1] >= 1 and Card_idx[i+2] >= 1:
        Card_idx[i] -= 1
        Card_idx[i+1] -= 1
        Card_idx[i+2] -= 1
        run += 1
        continue

    i += 1

for test_case in range(1, T + 1):
    if trp + run == 2:
        print('#{} 1'.format(test_case))
    else:
        print('#{} 0'.format(test_case))






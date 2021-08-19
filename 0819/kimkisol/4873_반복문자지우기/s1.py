import sys
sys.stdin = open('input.txt')

def Deduplication(chars, idx=0):
    if idx == len(chars)-1:
        return len(chars)
    if chars[idx] == chars[idx+1]:
        if idx == 0:
            return Deduplication(chars[:idx] + chars[idx+2:], idx)
        else:
            return Deduplication(chars[:idx]+chars[idx+2:], idx-1)
    else:
        return Deduplication(chars, idx+1)

T = int(input())

for t in range(1, T+1):
    chars = input()
    print('#{} {}'.format(t, Deduplication(chars)))
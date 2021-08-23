import sys
sys.stdin = open('input.txt')

def solve():
    i = 1
    while i < len(line):
        if line[i-1] != line[i]:
            i += 1
        else:
            line.pop(i) # i 먼저 해줘야 index 안 바뀜
            line.pop(i-1)
            i -= 1 # 바뀐 부분이 i부터니까 재검사는 i-1부터
    return len(line)

T = int(input())
for t in range(1, T+1):
    line = list((input()))
    print('#{} {}'.format(t, solve()))
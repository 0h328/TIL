import sys
sys.stdin = open('input.txt')

def is_included(target, search):
    for idx in range(len(target) - len(search) + 1):
        for idx2 in range(len(search)):
            if target[idx + idx2] != search[idx2]:
                break
        else:
            return 1
    return 0

T = int(input())

for t in range(1, T + 1):
    search = input()
    target = input()
    print('#{} {}'.format(t, is_included(target, search)))
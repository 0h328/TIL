import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    pattern = set(input())
    sentence = input()
    result = 0
    for p in pattern:
        result = max(result, sentence.count(p))

    print('#{} {}'.format((T+1), result))

#1 2
#2 1
#3 3

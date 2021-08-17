import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    words, pattern = input().split()
    result = len(words)-words.count(pattern)*(len(pattern)-1)
    print('#{} {}'.format((T+1), result))

#1 3
#2 5
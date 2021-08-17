import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    pattern = input()
    sentence = input()

    print('#{} {}'.format((T+1), int(pattern in sentence)))

#1 1
#2 0
#3 1

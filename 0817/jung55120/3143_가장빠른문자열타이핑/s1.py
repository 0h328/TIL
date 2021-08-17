import sys
sys.stdin = open('input.txt')

num = int(input())

for T in range(1, num+1):
    word, part = input().split()
    cnt = 0

    for i in range(len(word)-len(part)+1):
        if word[i] == part[0]:
            for j in range(len(part)):
                if word[i:i+j] == part[:]:
                    cnt += 1

        else:
            cnt += 1


    print(cnt)


























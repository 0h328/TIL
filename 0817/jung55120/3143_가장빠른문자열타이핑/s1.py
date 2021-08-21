import sys
sys.stdin = open('input.txt')

num = int(input())

for tc in range(1, num+1):
    word, part = input().split()
    cnt = 0
    idx = 0
    for i in range(len(word)-len(part)+1): # word에서 part 길이를 빼고 1을 더해줌
        while idx < len(word):
            if word[idx:idx+len(part)] == part: # 만약 word의 i번째 index와 같다면
                cnt += 1
                idx += len(part)
            else:
                cnt += 1
                idx += 1


    print('#{0} {1}'.format(tc, cnt))


























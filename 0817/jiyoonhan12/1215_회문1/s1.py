import sys
sys.stdin = open('input.txt')

def check(wordlist):
    for i in range(len(wordlist)//2):
        if wordlist[i] != wordlist[len(wordlist)-i-1]:
            return False
    return True

for t in range(1, 11):
    length = int(input())
    arr = [list(map(str, input())) for _ in range(8)]
    turn_arr = list(zip(*arr))
    cnt = 0
    # 한 줄 당 확인해야 할 횟수는 8-length+1회

    for i in range(8):
        wordlist1, wordlist2 = [], []
        for j in range(9-length): # 8-length+1
            wordlist1 = arr[i][j:j+length]
            wordlist2 = turn_arr[i][j:j+length]
            if check(wordlist1) == True:
                cnt += 1
            if check(wordlist2) == True:
                cnt += 1

    print('#{} {}'.format(t, cnt))
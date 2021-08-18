import sys
sys.stdin = open('input.txt')

def check(wordlist):
    for i in range(len(wordlist)//2):
        if wordlist[i] != wordlist[len(wordlist)-i-1]:
            return False
    return True

for t in range(1, 11):
    T = int(input())
    arr = [list(map(str, input())) for _ in range(100)]
    zip_arr = list(zip(*arr))

    res1, res2 = 0, 0
    for i in range(100):
        for j in range(100):
            wordlist1, wordlist2 = [], []
            for k in range(100-j, -1, -1): # 회문 길이 (큰 수부터)
                wordlist1 = arr[i][j:j+k]
                wordlist2 = zip_arr[i][j:j+k]
                if check(wordlist1) == True:
                    res1 = max(res1, len(wordlist1))
                    break
                if check(wordlist2) == True:
                    res2 = max(res2, len(wordlist2))
                    break
                    #flag 써서 값 찾으면 빠져나오기

    res = max(res1, res2)

    print('#{} {}'.format(t, res))
import sys
sys.stdin = open('input.txt')


for num in range(10):
    N = int(input())
    words = [list(map(str, input())) for _ in range(8)]
    col_words = list(zip(*words))
    cnt = 0

    for i in range(8):
        for k in range(8):
            tmp1 = []
            tmp2 = []
            if k+N <= 8:
                tmp1 = words[i][k:k+N]
                tmp2 = col_words[i][k:k+N]
                if list(tmp1) == list(reversed(tmp1)): # 여기서 list() 를 안해주면 결과가 모두 0이 나옴
                # if tmp1 == reversed(tmp1): 조건이 안맞음
                    cnt += 1

                if list(tmp2) == list(reversed(tmp2)):
                    cnt += 1

    print("#{} {}".format(num+1, cnt))

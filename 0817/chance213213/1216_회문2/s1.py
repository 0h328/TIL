import sys
sys.stdin = open('input.txt')


for _ in range(10):
    N = int(input())
    arr = [list(input()) for _ in range(100)] #2차원 행렬로 받아옴, 각 문자 떨어져서 들어옴

    #이제는!! 회문 판별 쓸거임! 오늘 배운거 쓸건데, 글자 길이에 제한 X,
    i = 0
    cnt = 0
    real_ans = {}
    while i < 100:
        for M in range(2, 100):
            for j in range(100-M+1): #0~99 중에서 3글자면 97,98,99 해야함, 98까지 범위 넣으려면 100 - 3 + 1
                for m in range(M//2):
                    if arr[i][j+m] != arr[i][j+M-m-1]:
                        break
                    elif m == M//2 - 1:
                        ans = tuple(arr[i][j:j+M])
                        if ans in real_ans:
                            real_ans[ans] += 1
                        else:
                            real_ans[ans] = 1



        i += 1

    my_len = []
    for key in real_ans.keys():
        a = len(key)
        my_len.append(len(key))
    # print(real_ans)
    print(max(my_len))
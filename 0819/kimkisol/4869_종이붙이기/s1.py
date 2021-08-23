import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    paper_len = int(input()) // 10
    print('paper_len', paper_len)
    result = 1
    box2 = 0
    for i in range(paper_len-1): #두칸짜리 종이 시작 경우의 수
        print('i', i)
        box2 += 1
        result += 1
        print(result)
        for j in range(i+2, paper_len-1): #추가 두칸짜리 종이
            print('j', j)
            box2 += 1
            result += 1
            print(result)
    for k in range(box2):  # 두칸짜리 안에 세로 가로여부
        print('k', k)
        result += 1
        print(result)
    print('box2', box2)
    print('result', result)




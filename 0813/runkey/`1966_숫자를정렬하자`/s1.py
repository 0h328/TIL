import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(t):
    cnt = int(input())
    result = []
    b = map(int, input().split())
    for i in b:
        result.append(i)
    result.sort()


    print("#{0}".format(tc+1), end=" ")
    for r in range(len(result)):  # result의 길이만큼 반복
        if r == len(result) - 1:  # 만약 현재 인덱스가 result길이의 -1과 같으면
            print("{}".format(result[r]))  # result[r]을 출력 후 줄바꿈
        else:  # 현재 인덱스가 마지막 인덱스가 아니면
            print("{}".format(result[r]), end=" ")  # 공백을 사이에 두고 result[r]을 출력
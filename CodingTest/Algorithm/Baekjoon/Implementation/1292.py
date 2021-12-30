import sys
sys.stdin = open('input.txt')

A, B = map(int, input().split())

seq = []

num = 1                         # 수열은 1부터 시작
while seq.count(num) <= num:    # 수열에 넣을 수가 리스트 안에 수의 개수랑 같아질때까지
    if seq.count(num) != num:   # 수열에 넣을 수의 개수가 수랑 같지 않으면
        seq.append(num)         # 계속 넣고
    elif seq.count(num) == num: # 같아지면
        num += 1                # 수열의 수를 +1 해서 계속 진행

    if len(seq) == 1000:        # 범위가 1000까지 이므로 길이가 1000이되면
        break                   # 종료

print(sum(seq[A-1:B]))

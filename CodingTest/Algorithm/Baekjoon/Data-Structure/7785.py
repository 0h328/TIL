import sys
sys.stdin = open('input.txt')

n = int(sys.stdin.readline())
info = dict()

for _ in range(n):
    name, status = map(str, sys.stdin.readline().split())   # 이름과 출퇴근 상태 인풋
    if status == 'enter':       # 상태가 enter면
        info[name] = 1          # key = 이름, value = 1로 저장
    else:                       # enter가 아니면
        del info[name]          # 해당 key 삭제
info = sorted(info.keys(), reverse=True)    # key를 기준으로 사전 순의 역순으로 정렬

for i in info:
    print(i)
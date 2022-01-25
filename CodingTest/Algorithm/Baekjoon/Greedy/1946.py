import sys
sys.stdin = open('input.txt')

def solution(info_list):
    global cnt

    tmp = info_list[0][1]           # 면접 순위를 비교하기 위한 변수
                                    # 서류 순위가 1등인 사람의 면접 순위를 기준으로 해야함
    for i in range(1, N):
        if tmp > info_list[i][1]:   # 다음 사람의 면접 순위가 높으면
            cnt += 1                # 채용
            tmp = info_list[i][1]   # 다음 사람의 면접 순위로 갱신

    return cnt

T = int(input())
for _ in range(T):
    N = int(input())
    info = [tuple(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N)]
    info.sort(key=lambda x: x[0])   # 서류 순위 기준으로 오름차순 정렬
    cnt = 1 # 서류 순위가 1등이면 무조건 채용이므로, cnt = 1부터 시작

    print(solution(info))






import sys
sys.stdin = open('input.txt')
"""
1. 작업 시간을 리스트로 받아서 끝나는 작업 시간 순으로 정렬 시킨 뒤
2. 그 다음 작업 시작 시간이 진행중인 작업이 끝나는 시간보다 크거나 같을 때
3. count + 1을 해주고, 새로운 끝나는 작업 시간을 현재 작업 기준으로 바꿔준다.
"""
tc = int(input())           # 테스트 케이스 갯수

for t in range(1, tc + 1):
    result = 0              # 최종 결과값
    N = int(input())        # 작업 갯수
    job_list = []           # 작업 리스트
    for _ in range(N):
        job_list.append(list(map(int, input().split())))    # 시작, 끝 시간이 담긴 리스트를 담은 리스트
    job_list = sorted(job_list, key=lambda x:x[1])          # 끝나는 시간 기준 정렬

    count = 1               # 일단 시작할 때 1개 있으므로 1로 초기화
    end = job_list[0][1]    # 끝나는 시간을 첫 작업의 끝 시간으로 고정
    for idx in range(1, len(job_list)): # 작업의 갯수 만큼 반복
        if end <= job_list[idx][0]:     # 만약 작업 시작 시간이 끝 시간보다 크거나 같으면
            count += 1                  # count + 1
            end = job_list[idx][1]      # 끝 시간을 현재 인덱스의 끝 시간으로 바꿔줌
    result = count                      # result에 최종 count 값 담아줌

    print("#{} {}".format(t, result))   # 출력
import sys
sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = []
    processor = []                                      # 연결해야 될 프로세서 위치
    for i in range(N):
        line = list(map(int, input().split()))          # 배열 만들기
        arr.append(line)
        if 0 < i < N-1:
            for j in range(1, N-1):
                if line[j]:
                    processor.append((i, j))            # 프로세서 위치 저장 완료

    ans = [0, N*N]                                      # [연결된 개수, 선 길이]
    stack = [(0, 0, 0, arr)]                            # 현재 기준 (확인 중인 pc, 연결된 개수, 선 길이, 배열)
    while stack:
        check, core, wire, arr = stack.pop()
        if check == len(processor):                     # 모든 프로세서를 확인했다면
            if core > ans[0] or (core == ans[0] and wire < ans[1]):
                ans = [core, wire]                      # 최종값 업데이트
        elif N - check + core > ans[0] or (N - check + core == ans[0] and wire <= ans[1]):  # 더 확인할 게 남아있다면
            stack.append((check+1, core, wire, [line[:] for line in arr]))                  # 다음 pc 확인하러 넘어가기
            for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):                               # 빈칸 채우기 위해 방향 설정
                i, j = processor[check]
                i += di
                j += dj
                wire2 = wire
                arr2 = [line[:] for line in arr]
                while 0 <= i < N and 0 <= j < N and arr[i][j] == 0:     # 같은 방향으로 계속 채워나감
                    arr2[i][j] = 1
                    wire2 += 1
                    i += di
                    j += dj
                if i == -1 or i == N or j == -1 or j == N:              # 연결이 되었다면
                    stack.append((check+1, core+1, wire2, arr2))        # 그 상태에서 다음 pc 체크하러 넘어감
    print('#{} {}'.format(t, ans[1]))
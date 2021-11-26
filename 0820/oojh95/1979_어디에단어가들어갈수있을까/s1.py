# N*N 퍼즐에서 검은색 부분(0으로 입력)을 제외하고
# 흰색부분(1으로 입력)에 K길이의 단어를 입력하고자함.
# 단어가 들어갈 수 있는 자리가 몇개인지 출력
import sys
sys.stdin = open('input.txt')
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    puzzle = [[0] * (N + 2)]
    result = 0

    for i in range(1, N + 1):
        test = [0]
        test += (list(map(int, input().split())))
        test.append(0)
        puzzle.append(test)
    puzzle.append([0] * (N + 2))

    for i in range(1, N + 1):
        for j in range(1, N - K + 2):
            if puzzle[i][j] == 1 and puzzle[i][j + K] == 0 and puzzle[i][j - 1] == 0:
                for k in range(1, K):
                    if puzzle[i][j + k] != 1:
                        break
                else:
                    result += 1

            if puzzle[j][i] == 1 and puzzle[j + K][i] == 0 and puzzle[j - 1][i] == 0:
                for k in range(1, K):
                    if puzzle[j + k][i] != 1:
                        break
                else:
                    result += 1

    print(f'#{test_case} {result}')

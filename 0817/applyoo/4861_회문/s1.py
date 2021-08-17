import sys
sys.stdin = open('input.txt')


def palindrome(word):
    for i in range(len(word)//2): # 인덱스 절반까지만
        if word[i] != word[-i-1]: # 앞 뒤로 1개씩 비교가 다른 경우
            return False
    return True


T = int(input())
for test in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(str, list(input()))) for _ in range(N)]
    flag = False # 회문을 찾았는지 여부를 판단할 변수

    for word in arr: # 행 반복
        for idx in range(N-M+1): # 인덱스의 시작점
            if palindrome(word[idx:idx+M]): # 회문인 경우
                flag = True # 찾았으므로 True 변환
                print('#{} {}'.format(test, ''.join(word[idx:idx+M]))) # 결과 출력
                break
        if flag: # 찾은 경우
            break

    if not flag: # 답을 못 찾은 경우
        for word in zip(*arr): # 열 반복
            for idx in range(N-M+1):
                if palindrome(word[idx:idx+M]): # 회문인 경우
                    flag = True
                    print('#{} {}'.format(test, ''.join(word[idx:idx+M]))) # 결과 출력
                    break
            if flag:
                break
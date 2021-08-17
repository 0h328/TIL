import sys
sys.stdin = open('input.txt')


def palindrome(word):
    for i in range(len(word)//2): # 인덱스 절반까지만
        if word[i] != word[-i-1]: # 앞 뒤로 1개씩 비교가 다른 경우
            return False
    return True


for _ in range(10):
    test = int(input())
    arr = [list(map(str, list(input()))) for _ in range(100)]
    flagX, flagY = False, False # 회문을 찾았는지 여부를 판단할 변수(각각 행, 열)
    result = 0 # 초기 0으로

    for N in range(100, 0, -1): # 100~1 반복
        for word in arr: # 행 반복
            for idx in range(100-N+1): # 인덱스의 시작점
                if palindrome(word[idx:idx+N]): # 회문인 경우
                    flagX = True # 찾았으므로 True 변환
                    result = len(word[idx:idx+N]) # 결과 저장
                    break
            if flagX: # 찾은 경우
                break
        if flagX: # 찾은 경우
            break

    for N in range(100, result, -1): # 100~(가로에서 찾은 값 + 1) 반복
        for word in zip(*arr): # 열 반복
            for idx in range(100-N+1): # 인덱스의 시작점
                if palindrome(word[idx:idx+N]): # 회문인 경우
                    flagY = True
                    result = len(word[idx:idx+N])
                    break
            if flagY: # 찾은 경우
                break

    print('#{} {}'.format(test, result))
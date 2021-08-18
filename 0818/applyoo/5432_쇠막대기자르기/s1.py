import sys
sys.stdin = open('input.txt')


def ironCut(arr):
    result = 0
    prev = arr[0] # 문제 조건상 필요없으나 배열이 정상(가로의 쌍이 맞지 않을 경우)적이지 않을 경우를 대비
    stack = []
    for factor in arr:
        if factor =='(': # '('인 경우
            result += 1 # 결과 + 1
            stack.append(factor) # 스택에 쌓기
        else: # ')'인 경우
            stack.pop() # 기존의 '('를 빼기
            if prev == '(': # 이전에 '('가 있었다면(레이저임)
                result -= 1 # 결과 -1
                result += len(stack) # stack의 길이만큼 더해주기
        prev = factor # 이전 값 저장
    return result


T = int(input())
for test in range(T):
    arr = input()
    print('#{} {}'.format(test+1, ironCut(arr)))
import sys

sys.stdin = open('input.txt')


def dfs(cnt):
    global answer
    if cnt == change: # 바꿀 수 있는 횟수를 모두 사용하면
        temp = int(''.join(nums))
        if answer < temp: # 비교 후 값 반환
            answer = temp
        return

    for i in range(N):
        for j in range(i + 1, N):
            nums[i], nums[j] = nums[j], nums[i] # 일단 변환하고

            tmp = ''.join(nums)
            if visited.get((tmp, cnt + 1), 1): # 만약 그 값이 딕셔너리 키값으로 존재하면 그 값을 아니면 1을 조회 즉, 한번도 들어간 적 없다면 1이 나오면서 조건문에 걸린다.
                visited[(tmp, cnt + 1)] = 0 # 해당 키값을 0으로 바꾸면 다음에는 이 조건문에 안걸린다.
                dfs(cnt + 1) # 재귀 실행 그러면 처음 바꾼 것을 기준으로 뒤에를 계속해서 바꾼다.
            nums[i], nums[j] = nums[j], nums[i] # 다시 원상복귀


for test in range(1, 1 + int(input())):
    num, change = input().split()
    nums = list(num) # 리스트 변환
    change = int(change) # 인트 변환
    N = len(num) # 길이 사용해야 함
    answer = 0 # 초기화

    visited = {}

    dfs(0)

    print('#{} {}'.format(test, answer))

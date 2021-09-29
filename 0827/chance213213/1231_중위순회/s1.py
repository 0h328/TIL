import sys

sys.stdin = open('input.txt')
result = ''


def in_order(a):
    global result
    # 왼쪽 자식 있나? 없으면 부모 노드 출력, 오른쪽 자식 있나? 있으면 출력
    if a <= N:  # N이 되는 건, 노드 개수임
        in_order(a * 2)  # 왼쪽 젤 시작은 2의 배수임, 저어기 끝까지 내려가겠다는 거임
        result += nums_st[a]
        print(nums_st[a], end='*')
        in_order(a * 2 + 1)  # 가장 왼쪽 내려간거에서 형제노드임


for tc in range(1, 11):
    N = int(input())
    nums_st = [0] * (N + 1)
    for i in range(N):
        nums = list(input().split())
        nums_st[i + 1] = nums[1]
    print(f'#{tc}', end=' ')
    print(nums_st)
    in_order(1)
    print()

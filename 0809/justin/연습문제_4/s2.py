# Edge case 처리

def solve(numbers):
    counter = [0 for _ in range(10)]
    is_babygin = 0

    for number in numbers:
        counter[number] += 1


    idx = 0
    while idx < len(counter):       # counter의 길이를 넘지 않는 선에서 반복(idx 관리)
        if counter[idx] >= 3:       # triplet 체크
            counter[idx] -= 3
            is_babygin += 1
            continue                # triplet 체크 이후 다시 triplet & run 확인

        if idx < len(counter) - 2:
            if counter[idx] and counter[idx+1] and counter[idx+2]: # run 체크
                counter[idx] -= 1
                counter[idx+1] -= 1
                counter[idx+2] -= 1
                is_babygin += 1
                continue            # run 체크 이후 다시 triplet & run 확인

        if is_babygin == 2:
            return 1
        idx += 1            # 다음 기준 인덱스 확인
    return 0


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    numbers = list(map(int, input()))
    ans = solve(numbers)
    print('#{} {}'.format(tc, ans))
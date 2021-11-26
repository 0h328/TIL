import sys
sys.stdin = open('input.txt')


test_case = int(input())

for tc in range(1, test_case+1):
    in_str = []
    max_len = 0
    answer = ''

    for _ in range(5):
        tmp_str = input()
        in_str.append(tmp_str)

        if max_len < len(tmp_str):          # 반복횟수를 위해 가장 긴 문자열의 길이를 구함
            max_len = len(tmp_str)

    idx = 0
    while idx < max_len:                    # 문자들의 0 번 인덱스부터 가장 긴 문자열 인덱스까지 반복
        for e in in_str:                    # 각 문자열들 호출
            if idx < len(e):                # 길이가 벗어나지 않으면 정답에 추가
                answer += e[idx]
        idx += 1

    print('#{} {}'.format(tc, answer))
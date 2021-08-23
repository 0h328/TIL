import sys
sys.stdin = open('input.txt')


def notDuplicate(word):
    result = [None]  # 10line 인덱스를 맞춰주기 위해 None 입력
    idx = 0  # 인덱스 번호

    while idx < len(word):
        if result[-1] != word[idx]:  # 다른 경우
            result.append(word[idx])  # 그냥 추가함
        else:  # 같은 경우
            if len(result) > 1:  # result가 0이면 에러남(다만, None 들어가 있으므로 1초과 일때만)
                result.pop()
        idx += 1  # 다음 인덱스
    return ''.join(result[1:])


for test in range(10):
    N, password = map(str, input().split())
    print('#{} {}'. format(test+1, notDuplicate(password)))
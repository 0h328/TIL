import sys
sys.stdin = open('input.txt')


def maxInclude(pattern, word):
    result = 0
    visited = set()

    for i in pattern: # pattern 요소의 반복
        if i not in visited: # 방문한 적 없는 경우(pattern 요소를 센 적이 없는 경우)
            visited.add(i) # 방문에 추가
            result = max(result, word.count(i)) # 더 큰 값 저장
    return result


T = int(input())
for test in range(T):
    str1 = input()
    str2 = input()

    print('#{} {}'.format(test+1, maxInclude(str1, str2)))
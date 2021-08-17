import sys

sys.stdin = open('input.txt')


def getPattern(pattern):
    patternl = len(pattern)                 # 패턴길이
    result = [0 for _ in range(patternl)]  # 패턴 반복되는 위치 확인할 초기화
    j = 0  # 첫글자부터 탐색
    for i in range(1, patternl):             # 두번째 글자와 비교하면서 최대 패턴길이만큼 탐색
        while j > 0 and pattern[i] != pattern[j]:  # 만약 탐색위치가 0보다 클때 이것은 탐색위치가 0인데 탐색위치와 현재위치와 값이 다를 경우에는 값을 0으로 그대로 둔다.
            j = result[j - 1]  # 값이 서로 다를 경우 마지막으로 반복되었던 위치를 확인하기 위해 j-1까지 반복된 패턴 값을 j로 할당 이는 다시 탐색되는 위치가 최대 반복위치 부터 시작하도록 만들어준다.

        if pattern[i] == pattern[j]:          # 만약 탐색위치와 현재위치의 값이 같다면
            j += 1                              # 탐색위치를 한 칸 옮겨주고
            result[i] = j                   # 현재위치에 해당되는 반복되는 횟수에 증가한 탐색위치만큼의 값을 할당한다.
    return result                           # 결과값을 반환

def search(target, pattern):
    targetl = len(target)
    patterl = len(pattern)

    find = getPattern(pattern)              # 패턴이 등장하는 위치를 만들어주고
    j = 0                                   # 탐색위치
    for i in range(0, targetl):             # 이건 한 리스트가 아니라 두개의 값을 서로 비교해야 하기 때문에 0부터 시작한다.
        while j > 0 and target[i] != pattern[j]:  # 탐색위치가 0보다 클때로 설정해서 0일때 값이 다른 경우는 그냥 넘어간다 별다른 행동을 하지 않는다.
            j = find[j - 1]                 # 다를 경우에는 한칸 전에 패턴등장위치의 값을 탐색위치로 변경해서 다시 탐색을 시작한다.
        if target[i] == pattern[j]:          # i는 변하지 않은채 변경된 탐색위치로 탐색을 시작한다. 만약 값이 일치하지 않는다면 다음 i 로 넘어가고 연산한다.
            if j == patterl - 1:            # 탐색위치가 패턴 길이의 끝에 도달할 경우 검색에 성공한 것이므로 원하는 값을 출력한다.
                return [i, pattern]
            else:
                j += 1                      # 원하는 값을 아직 찾지 못했을 경우 탐색위치를 늘려서 다시 점검한다.


T = int(input())

for test in range(T):
    t, numbers = input().split()

    data = input().split() # svn zro one two

    target = 'ZROONETWOTHRFORFIVSIXSVNEGTNIN'

    result = []
    for i in data:
        result.append(search(target, i))

    result.sort(key=lambda x: x[0])
    print('#{}'.format(test + 1))
    for i in result:
        print(i[1], end=' ')
    print()


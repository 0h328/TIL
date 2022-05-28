import sys
sys.stdin = open('input.txt')

s = input()
ans = []

# 단어를 3개로 나눔
for i in range(len(s)-2):   # 단어 길이가 1이상이므로, 앞에 단어는 뒤에서 2번째까지
    for j in range(i+1, len(s)-1):  # 앞에 단어 다음부터 맨 뒤 단어 전까지
        for k in range(j+1, len(s)):    # j 다음부터 맨 뒤 단어까지
            tmp = s[:j][::-1] + s[j:k][::-1] + s[k:][::-1]  # [::-1]를 통해 뒤집어준다.
            ans.append(tmp)

print(min(ans)) # min을 문자열을 사전순으로 가장 앞서는 단어를 출력해줌


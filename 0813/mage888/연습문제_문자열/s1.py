# cnt = [0] * 26
# s = 'ssAfy6'
#
# for x in s:
#     if 'a' <= x <= 'z':
#         cnt[ord(x)-ord('a')] += 1
#     elif 'A' <= x <= 'Z':
#         print(x)
#     elif '0' <= x <= '9':
#         print('숫자')
#
# print(cnt)

cnt = [0] * 26
s = list(input())

for x in s:
    if 'a' <= x <= 'z':
        cnt[ord(x)-ord('a')] += 1
    elif 'A' <= x <= 'Z':
        print(x)
    elif '0' <= x <= '9':
        print(x)

print(cnt)
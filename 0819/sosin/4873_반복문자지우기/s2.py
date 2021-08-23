import sys
sys.stdin = open('input.txt')

# Edge Case 1
for T in range(int(input())):
    s = input()
    idx = 0
    while idx < len(s)-1:
        if s[idx] == s[idx+1]:
            s = s[:idx] + s[idx+2:]
            idx-=1
        else:
            idx+=1

    print('#{} {}'.format((T+1), len(s)))
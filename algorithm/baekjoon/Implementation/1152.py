a = str(input())

if ' ' == a[0] and ' ' == a[-1]:
    print(a.count(' ')-1)
elif ' ' == a[0] and ' ' != a[-1]:
    print(a.count(' '))
elif ' ' != a[0] and ' ' == a[-1]:
    print(a.count(' '))
else:
    print(a.count(' ')+1)

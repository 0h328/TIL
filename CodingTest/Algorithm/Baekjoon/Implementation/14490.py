n, m = map(int, input().split(":"))

isSwaped = False
if m > n:
    tmp = m;
    m = n;
    n = tmp;
    isSwaped = True

XX = n
gcd = m
while (XX % gcd != 0):
    reminder = XX % gcd
    XX = gcd
    gcd = reminder

if isSwaped:
    print((str)((int)(m/gcd))+":"+(str)((int)(n/gcd)))
else:
    print((str)((int)(n/gcd))+":"+(str)((int)(m/gcd)))

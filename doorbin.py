a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())
if a == e:
    if b == d:
        print(c, f)
    elif d == f:
        print(c, b)
elif a == c:
    if b == f:
        print(e, d)
    elif d == f:
        print(e, b)
elif c == e:
    if b == f:
        print(a, d)
    if d == b:
        print(a, f)


x, y = map(int, input().split())
x1, y1 = map(int, input().split())

if x > x1:
    if y1 > y or y > y1 or y == y1:
        print("left")
elif x1 > x:
    if y1 > y or y > y1 or y == y1:
        print("right")
elif x == x1:
    if y > y1:
        print("left")
    elif y < y1:
        print("right")

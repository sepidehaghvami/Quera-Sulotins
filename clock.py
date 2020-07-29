h, m = map(int, input().split())
h = (12 - h)*int((h != 0))
m = (60 - m)*int((m != 0))
print("%02d : %02d" % (h, m))



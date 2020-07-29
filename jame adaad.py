num_list = []

while True:
    num = int(input())
    if num == 0:
        break
    num_list += [num]
    a = sum(num_list)

print(a)
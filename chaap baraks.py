num_list = []
while True:
    num = int(input())
    if num == 0:
        break
    num_list += [num]
    arr = num_list[::-1]
for i in range(len(arr)):
    print(arr[i])

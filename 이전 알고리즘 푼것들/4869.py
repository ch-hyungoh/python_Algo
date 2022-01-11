def stack(num):
    if num == 1:
        return 1
    if num == 2:
        return 3
    return stack(num-1) + stack(num-2)*2

for i in range(1, 1+int(input())):
    a = int(input())/10
    print(stack(a))
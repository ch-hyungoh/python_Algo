N = int(input())

first_N = N
num_list = []
result = 0

while N > 0:
    a = N%10
    N = N//10
    num_list.append(a)

k = len(num_list)

start_num = first_N - k*9

while start_num <= first_N:
    list_num = []
    sums = 0
    m = start_num
    result = start_num
    while m > 0:
        a = m % 10
        m = m // 10
        list_num.append(a)

    for z in list_num:
        result += z

    if result == first_N:
        print(start_num)
        break

    start_num += 1

else:
    print("0")

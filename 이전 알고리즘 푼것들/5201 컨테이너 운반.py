for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    arr.reverse()
    arr_list = [0]*N
    bus_list = [0]*M
    bus = list(map(int, input().split()))
    bus.sort()
    bus.reverse()

    for i in range(len(arr)):
        for j in range(len(bus)):
            if (arr[i] <= bus[j]) and not bus_list[j]:
                arr_list[i] = 1
                bus_list[j] = 1
                break

    result = 0
    for i in range(len(arr_list)):
        if arr_list[i] == 1:
            result += arr[i]

    if not arr_list:
        result = 0

    print("#{} {}".format(tc, result))
def dfs(idx, count):
    global max
    print(arr, count)
    if count == N:
        num = ''
        for i in range(len(arr)):
            num += arr[i]
        num = int(num)
        if max < num:
            max = num
        return
    for i in range(len(arr)):
        arr[i], arr[idx] = arr[idx], arr[i]
        dfs(idx+1, count+1)
        arr[i], arr[idx] = arr[idx], arr[i]

for tc in range(1, 1+int(input())):
    arr, N = input().split()
    N = int(N)
    arr = list(arr)
    max = 0
    arr_list = []
    dfs(0, 0)

    print('#{} {}'.format(tc, max))
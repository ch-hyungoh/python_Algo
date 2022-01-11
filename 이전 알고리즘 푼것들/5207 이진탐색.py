def solve(find, start, end, status):
    global number
    if start > end:
        return
    mid = (start + end) // 2

    if find == arr_N[mid]:
        number += 1
        return

    if arr_N[mid] > find:
        if status == 1:
            return
        else:
            solve(find, start, mid-1, 1)

    elif arr_N[mid] < find:
        if status == 2:
            return
        else:
            solve(find, mid+1, end, 2)

for tc in range(1, 1+int(input())):
    N, M = map(int, input().split())
    arr_N = sorted(list(map(int, input().split())))
    arr_M = list(map(int, input().split()))
    number = 0
    status = 0

    for i in range(M):
        solve(arr_M[i], 0, N-1, status)

    print("#{} {}".format(tc, number))
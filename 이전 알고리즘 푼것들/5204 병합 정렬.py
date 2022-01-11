def merge(arr):
    global num
    if len(arr) == 1:
        return arr
    left = merge(arr[:len(arr)//2])
    right = merge(arr[len(arr)//2:])

    new_arr = [0]*len(arr)

    a, b, c = 0, 0, 0
    if left[-1] > right[-1]:
        num += 1

    while True:
        if a >= len(left) or b >= len(right):
            break
        if left[a] < right[b]:
            new_arr[c] = left[a]
            a += 1
            c += 1
        else:
            new_arr[c] = right[b]
            b += 1
            c += 1
    while b < len(right):
        new_arr[c] = right[b]
        b += 1
        c += 1
    while a < len(left):
        new_arr[c] = left[a]
        a += 1
        c += 1
    return new_arr

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    num = 0
    now_arr = merge(arr)
    print("#{} {} {}".format(tc, now_arr[N//2], num))
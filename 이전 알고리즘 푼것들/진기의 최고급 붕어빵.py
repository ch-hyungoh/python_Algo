for tc in range(1, 1+int(input())):
    N, M, K = map(int, input().split())
    arr = list(map(int, input().split()))

    count = 0

    arr.sort()
    max_time = max(arr)
    now = 0
    result = 1
    for i in range(0, arr[-1]):
        if i > 0:
            if i % M == 0:
                count += K
        if now < len(arr):
            if i == arr[now]:
                count -= 1
                now += 1
                if count < 0:
                    result = 0
                    break

    if result:
        print('#{} Possible'.format(tc))
    else:
        print('#{} Impossible'.format(tc))

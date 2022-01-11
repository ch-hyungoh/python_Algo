for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    arr = sorted(arr, key=lambda x: x[1])

    cnt = 0
    now = 0
    for i in range(N):
        s = arr[i][0]
        e = arr[i][1]
        if now <= s:
            cnt += 1
            now = e

    print("#{} {}".format(tc, cnt))
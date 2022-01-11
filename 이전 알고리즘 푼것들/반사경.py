for tc in range(1, 1+int(input())):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]

    nx = 0
    ny = 0
    count = 0
    lay = 1
    while True:
        if lay == 1:
            nx += 1
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                break
            if arr[ny][nx] == 1:
                lay = 4
                count += 1
            if arr[ny][nx] == 2:
                lay = 2
                count += 1

        if lay == 2:
            ny += 1
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                break
            if arr[ny][nx] == 1:
                lay = 3
                count += 1
            if arr[ny][nx] == 2:
                lay = 1
                count += 1

        if lay == 3:
            nx -= 1
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                break
            if arr[ny][nx] == 1:
                lay = 2
                count += 1
            if arr[ny][nx] == 2:
                lay = 4
                count += 1

        if lay == 4:
            ny -= 1
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                break
            if arr[ny][nx] == 1:
                lay = 1
                count += 1
            if arr[ny][nx] == 2:
                lay = 3
                count += 1

    print('#{} {}'.format(tc, count))
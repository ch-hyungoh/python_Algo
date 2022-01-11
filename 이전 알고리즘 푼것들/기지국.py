dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for tc in range(1, 1+int(input())):
    N = int(input())

    arr = [list(input()) for _ in range(N)]
    count = 0
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 'A':
                for i in range(2):
                    for j in range(4):
                        ax = a + (dx[j] * i)
                        by = b + (dy[j] * i)
                        if 0 <= ax < N and 0 <= by < N:
                            if arr[ax][by] == 'H':
                                arr[ax][by] = 'X'
            if arr[a][b] == 'B':
                for i in range(3):
                    for j in range(4):
                        ax = a + (dx[j] * i)
                        by = b + (dy[j] * i)
                        if 0 <= ax < N and 0 <= by < N:
                            if arr[ax][by] == 'H':
                                arr[ax][by] = 'X'
            if arr[a][b] == 'C':
                for i in range(4):
                    for j in range(4):
                        ax = a + (dx[j] * i)
                        by = b + (dy[j] * i)
                        if 0 <= ax < N and 0 <= by < N:
                            if arr[ax][by] == 'H':
                                arr[ax][by] = 'X'

    for a in range(N):
        for b in range(N):
            if arr[a][b] == 'H':
                count += 1

    print('#{} {}'.format(tc, count))
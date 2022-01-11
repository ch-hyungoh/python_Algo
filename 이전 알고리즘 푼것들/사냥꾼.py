dx = [0, 0, -1, 1, -1, -1, 1, 1]
dy = [-1, 1, 0, 0, -1, 1, -1, 1]

for tc in range(1, 1+int(input())):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    count = 0

    for x in range(N):
        for y in range(N):
            if arr[x][y] == 1:
                for i in range(8):
                    for k in range(1, N):
                        nx = x + (dx[i] * k)
                        ny = y + (dy[i] * k)
                        if 0 <= nx < N and 0 <= ny < N:
                            if arr[nx][ny] == 2:
                                count += 1
                                arr[nx][ny] = 0
                            elif arr[nx][ny] == 1 and arr[nx][ny] != arr[x][y]:
                                break
                            elif arr[nx][ny] == 3:
                                break

    print('#{} {}'.format(tc, count))
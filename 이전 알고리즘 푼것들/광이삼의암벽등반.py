dx = [-1, 0]
dy = [0, 1]
def mount(x, y, now, bink):
    global min_bink
    bml = False
    if arr[x][y] == 1:
        now = 0
        bml = True
    elif arr[x][y] == 3:
        if bink < min_bink:
            min_bink = bink
            return
    if now == L:
        return
    for i in range(2):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and ny < M and not visited[nx][ny]:
            if bml:
                visited[nx][ny] = 1
                mount(nx, ny, now + 1, bink+1)
            else:
                visited[nx][ny] = 1
                mount(nx, ny, now + 1, bink)
            visited[nx][ny] = 0
            now -= 1

for tc in range(1, 1+int(input())):
    M, N, L = map(int, input().split())
    arr = []
    visited = [[0]*M for _ in range(M)]
    for _ in range(N):
        arr.append(list(map(int,input().split())))

    min_bink = 0xfffff
    visited[M-1][0] = 1
    mount(M-1, 0, 0, 0)

    if min_bink == 0xfffff:
        min_bink = -1

    print('#{} {}'.format(tc, min_bink))
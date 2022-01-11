rx = [1, 0]
ry = [0, 1]

def dfs(x, y, num):
    global min_num
    if x == (N-1) and (y == N-1):
        if min_num > num:
            min_num = num
    if num > min_num:
        return
    for i in range(2):
        dx = x + rx[i]
        dy = y + ry[i]
        if dx < N and dy < N and not visited[dx][dy]:
            visited[dx][dy] = 1
            dfs(dx, dy, num+arr[dx][dy])
            visited[dx][dy] = 0

for tc in range(1, 1+int(input())):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    min_num = 0xfffffff
    dfs(0, 0, arr[0][0])

    print('#{} {}'.format(tc, min_num))
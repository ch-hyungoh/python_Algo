def prim(start, len):
    global max_lenth
    if len > max_lenth:
        max_lenth = len
    for i in range(1, N+1):
        if arr[start][i] and not visited[i]:
            visited[i] = 1
            prim(i, len+1)
            visited[i] = 0


for tc in range(1, 1+int(input())):
    N, M = map(int,input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    visited = [0]*(N+1)
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x][y] = 1
        arr[y][x] = 1

    max_lenth = 1

    for i in range(N+1):
        visited[i] = 1
        prim(i, 1)
        visited[i] = 0
    print('#{} {}'.format(tc, max_lenth))


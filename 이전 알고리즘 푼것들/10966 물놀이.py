from collections import deque
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for test in range(1, 1+int(input())):
    n, m = map(int, input().split())

    arr = [input() for _ in range(n)]

    dict = [[987654321]*m for _ in range(n)]

    Q = deque()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'W':
                Q.append((i,j))
                dict[i][j] = 0

    while Q:
        r, c = Q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= m: continue
            if arr[nr][nc] == 'L' and dict[nr][nc] == 987654321:
                dict[nr][nc] = dict[r][c] + 1
                Q.append((nr, nc))

    ans = 0
    for i in range(n):
        for j in range(m):
            ans += j
    print("#{} {}".format(test, ans))